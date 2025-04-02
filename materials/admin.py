from django.contrib import admin

# Register your models here.
from materials.models import Course, Lesson, Subscription


@admin.register(Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Lesson)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Subscription)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id",)
