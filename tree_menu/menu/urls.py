from django.urls import path

from menu.views import All_main_menu, main_menu, menu_lv2, menu_lv3

urlpatterns = [
    path('menu/', All_main_menu.as_view(),  name='all_main_menu'),
    path('menu/<int:pk>', main_menu.as_view(),  name='main_menu'),
    path('menu/menu_lv2/<int:pk>', menu_lv2.as_view(),  name='menu_lv2'),
    path('menu/menu_lv3/<int:pk>', menu_lv3.as_view(),  name='menu_lv3'),

]
