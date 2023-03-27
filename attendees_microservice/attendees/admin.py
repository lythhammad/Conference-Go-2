from django.contrib import admin

from .models import Attendee, Badge, ConferenceVO


@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    pass


@admin.register(ConferenceVO)
class ConferenceVOAdmin(admin.ModelAdmin):
    pass
