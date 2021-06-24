from django.contrib import admin
from .models import Project, Branch, Language, Status
# Register your models here.

admin.site.register(Project)
admin.site.register(Branch)
admin.site.register(Language)
admin.site.register(Status)

