from django.contrib import admin
from .models import Author, AuthorProfile, Category, Publisher, Book, Publication


class PublicationInline(admin.TabularInline):
    model = Publication
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    inlines = [PublicationInline]


admin.site.register(Author)
admin.site.register(AuthorProfile)
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Publication)