from django.contrib import admin
from .models import Project, Task, Profile,Comment

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Profile)
admin.site.register(Comment)