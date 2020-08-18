from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)

#Inline listing of Book Items
class BooksInline(admin.TabularInline):
    model = Book
    
#Define admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

#Register the admin class with the associated model
admin.site.register(Author,AuthorAdmin)

#Inline editing
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    
#Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

#Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','id', 'status', 'due_back', 'borrower')
    list_filter = ('status', 'due_back')
    
    fieldsets = (
        (None, {
            'fields':('book', 'imprint', 'id')
        }),
        ('Availability',{
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
    
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'
    
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)