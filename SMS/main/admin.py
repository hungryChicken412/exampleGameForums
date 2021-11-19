from django.contrib import admin
from .models import BlogPost, Game, Screenshots, LandingPageDetails
from tinymce.widgets import TinyMCE
from django.db import models


# Register your models here.

class NiceText(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}

#CourseAdmin
admin.site.register(Game, NiceText)
admin.site.register(Screenshots)
admin.site.register(LandingPageDetails)
admin.site.register(BlogPost, NiceText)
