from django.contrib import admin
from .models import Member
class MemberAdmi(admin.ModelAdmin):
  list_display = ("firstname", "lastname","dateofbirth","gender","address","phonenumber","email","nationality","maritalstatus","occupation","emergencycontact","insuranceinformation")
# Register your models here.

admin.site.register(Member,MemberAdmi)

