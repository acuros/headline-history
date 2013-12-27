# -*- coding: utf-8 -*-
from django.contrib import admin
from headline.models import *


class HeadlineInline(admin.TabularInline):
    model = Headline
    extra = 0


class PressAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    inlines = (HeadlineInline, )


class HeadlineAdmin(admin.ModelAdmin):
    list_display = ('press', 'title', 'crawled_time', )
    list_filter = ('crawled_time', )
    search_fields = ('press__name', 'title', )


class CrawlLogAdmin(admin.ModelAdmin):
    list_display = ('crawled_time', )


admin.site.register(Press, PressAdmin)
admin.site.register(Headline, HeadlineAdmin)
admin.site.register(CrawlLog, CrawlLogAdmin)