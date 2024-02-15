from django.db import models

# Create your models here.
class mainmenu(models.Model):
    name = models.TextField(verbose_name='меню')

    class Meta:
        verbose_name_plural = 'Меню'
        verbose_name = 'Меню'


    def __str__(self):
        return self.name

class menu_lv2(models.Model):
    name = models.TextField(verbose_name='под_меню')
    parent_menu = models.ForeignKey(mainmenu, verbose_name='меню', on_delete=models.CASCADE,blank=False)

    class Meta:
        verbose_name_plural = 'Под_Меню'
        verbose_name = 'Под_Меню'

    def __str__(self):
        return self.name

class menu_lv3(models.Model):
    name = models.TextField(verbose_name='под_под_меню')
    parent_menu = models.ForeignKey(menu_lv2, verbose_name='под_меню', on_delete=models.CASCADE,blank=False)


    class Meta:
        verbose_name_plural = 'Под_Под_Меню'
        verbose_name = 'Под_Под_Меню'

    def __str__(self):
        return self.name