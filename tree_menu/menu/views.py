from django.views.generic import ListView, DetailView
from menu.models import mainmenu, menu_lv2, menu_lv3


class All_main_menu(ListView):
    template_name = 'all_main_menu.html'
    model = mainmenu

class main_menu(DetailView):
    template_name = 'main_menu.html'
    model = mainmenu

class menu_lv2(DetailView):
    template_name = 'menu_lv2.html'
    model = menu_lv2

class menu_lv3(DetailView):
    template_name = 'menu_lv3.html'
    model = menu_lv3

