from django.db import models
from django.urls import reverse


class Menu(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='child',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('menu:sub_menu', args=[self.slug])
