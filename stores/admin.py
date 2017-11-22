from django.contrib import admin
from .models import Store, MenuItem

# Register your models here.

# 注意!!! 此處有坑!!! 宣告 MenuItemInline 這個 class 一定要放前面!!!
# 起碼...要比 inlines = (MenuItemInline,) 這一行要前面!!!
# 否則 inlines = (MenuItemInline,) 這一行會噴錯誤告訴你 MenuItemInline Undefined !!!
class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'notes',)
    inlines = (MenuItemInline,)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)

