from django.contrib import admin
from blog.models import Blog, Application

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	class Media:
		css = {
			"all": ("css/main.css",)
		}
		js = ("js/blog.js",)

admin.site.register(Blog, BlogAdmin)
admin.site.site_header = "DevLogs Administration"
admin.site.site_title = "DevLogs Admin Portal"
admin.site.index_title = "Dashboard"
admin.site.register(Application)

