from django import template
from django.utils.safestring import mark_safe
import markdown


register=template.Library()





@register.filter(name='markdown')
def make_markdown(text):
	return mark_safe(markdown.markdown(text))
