from django.urls import path
from .views import MenuView, SubMenuView


app_name = 'menu'

urlpatterns = [
    path('', MenuView.as_view(), name='menu'),
    path('sub_menu/<str:slug>/', SubMenuView.as_view(), name='sub_menu')
]
