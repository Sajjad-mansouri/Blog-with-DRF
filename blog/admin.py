from django.contrib import admin
from .models import ArticleModel

@admin.register(ArticleModel)
class BlogAdmin(admin.ModelAdmin):
	list_display=['title','slug','author','published','status']
	prepopulated_fields={'slug':('title',)}
	search_fields=['title','author','content']
	list_filter=['author','published','status']
	date_hierarchy='published'