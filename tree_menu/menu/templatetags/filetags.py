from django.template import Library
from menu.models import mainmenu

register = Library()

#@register.inclusion_tag('menu/templatetags/for_tags/mainmenu.html')
@register.inclusion_tag('for_tags/tag_view.html')
def draw_menu(name):
    try:
        return {'menu':mainmenu.objects.get(name=name)}
    except:
        return {'menu':None}