from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(OldManInfo)
class OldManInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'age')


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'content_type')


@admin.register(QrCode)
class QrCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'qrCodeId', 'old_man_info')
