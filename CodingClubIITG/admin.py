from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
	pass

@admin.register(Projects)
class ProjectsAdmin(ImportExportModelAdmin):
	pass

@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
	pass

@admin.register(Members)
class MembersAdmin(ImportExportModelAdmin):
	pass