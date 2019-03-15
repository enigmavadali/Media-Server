from django.contrib import admin

from .models import Document, History, Lecture, Like, Comment

admin.site.register(Document)
admin.site.register(History)
admin.site.register(Lecture)
admin.site.register(Like)
admin.site.register(Comment)
