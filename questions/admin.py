from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from videos.models import Video
from .models import OpenQuestion, MultipleChoiceQuestion
# Register your models here.


# class VideoInline(admin.TabularInline):
# 	model = Video

# class OpenQuestionAdmin(admin.ModelAdmin):
# 	inlines = [VideoInline]
# 	class Meta:
# 		model = OpenQuestion

# class MultipleChoiceQuestionAdmin(admin.ModelAdmin):
# 	inlines = [VideoInline]
# 	class Meta:
# 		model = MultipleChoiceQuestion


admin.site.register(OpenQuestion)
admin.site.register(MultipleChoiceQuestion)