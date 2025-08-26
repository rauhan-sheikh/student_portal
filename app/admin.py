from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Staff, Student, Course, Subject


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("id","username","email", "user_type", "is_staff", "is_active")
    list_filter = ("user_type", "is_staff", "is_active")
    ordering = ("id",)
    fieldsets = (
        (None, {"fields": ("username","email", "password", "user_type")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username","email", "password1", "password2", "user_type", "is_staff", "is_active")}
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Subject)
