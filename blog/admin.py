from django.contrib import admin
from .models import ArticleModel,CommentModel

@admin.register(ArticleModel)
class BlogAdmin(admin.ModelAdmin):
	list_display=['title','slug','author','published','status']
	prepopulated_fields={'slug':('title',)}
	search_fields=['title','author','content']
	list_filter=['author','published','status']
	date_hierarchy='published'

@admin.register(CommentModel)
class BlogAdmin(admin.ModelAdmin):
	list_display=['post','name','body','email','active']
	search_fields=['post','name','body']
