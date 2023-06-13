from django import template
from django.utils.safestring import mark_safe
import markdown
from django.db.models import Count
from blog.models import ArticleModel


register=template.Library()





@register.filter(name='markdown')
def make_markdown(text):
	return mark_safe(markdown.markdown(text))

@register.simple_tag
def get_most_commented_posts(count=3):
    comments=ArticleModel.objects.annotate(total_comment=Count('comments')).exclude(total_comment=0).order_by('-total_comment')
    return comments
    
