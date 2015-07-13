from django.contrib import admin
from blog.models import *

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
  list_dispaly = ("title","content","id1","user","blogID")

admin.site.register(Blog,BlogAdmin)