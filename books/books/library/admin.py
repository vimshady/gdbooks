from django.contrib import admin

from .models import Book, Request


class BookAdmin(admin.ModelAdmin):
    pass

class RequestAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(Request, RequestAdmin)
