from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Menu

class MenuView(TemplateView):
    template_name = 'menu/index.html'

    def get(self, request):
        menus = Menu.objects.filter(parent=None)
        context = {'menus': menus}
        return render(request, self.template_name, context)

    def push(self, request):
        return render(request, self.template_name)

class SubMenuView(TemplateView):
    template_name = 'menu/sub_menu.html'

    def get(self, request, slug):
        menu = Menu.objects.filter(slug=slug).first().title
        context={'menu':menu}
        return render(request, self.template_name, context)