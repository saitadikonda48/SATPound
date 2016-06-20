from django.contrib import admin

from .models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','text']
	class Meta:
		model = Comment
admin.site.register(Comment, CommentAdmin)