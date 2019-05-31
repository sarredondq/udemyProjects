from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    #las columnas que quiero mostrar. toca definir metodo por ser many to many
    list_display = ('title', 'author', 'published', 'post_categories')
    #ordenar por (tupla)
    ordering = ('author', 'published')
    #buscar por. author tiene que estar con dos guiones abajo por ser foranea
    search_fields = ('title','content','author__username', 'categories__name')
    #filtra fechas en la parte de arriba
    date_hierarchy = 'published'
    #filtra en la parte derecha, mejor hacerlo por algo relevante
    list_filter = ('author__username','categories__name')

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)