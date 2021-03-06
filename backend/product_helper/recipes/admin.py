from django.contrib import admin

from .models import Favorite, Ingredient, Recipe, ShoppingCart, Tag

EMPTY_VALUE = '-пусто-'


class RecipeIngredientLine(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 1


class RecipeTagLine(admin.TabularInline):
    model = Recipe.tags.through
    extra = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    search_fields = ('name', 'color', 'slug')
    list_filter = ('color',)
    empty_value_display = EMPTY_VALUE


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name', 'measurement_unit')
    empty_value_display = EMPTY_VALUE


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'text',
                    'cooking_time')
    search_fields = ('name', 'description', )
    inlines = (RecipeIngredientLine, RecipeTagLine)
    list_filter = ('author', 'tags')
    empty_value_display = EMPTY_VALUE

    def show_ingredients(self, obj):
        return '\n'.join([ingr.name for ingr in obj.ingredients.all()])

    def show_tags(self, obj):
        return '\n'.join([tag.name for tag in obj.tags.all()])


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ('user', 'recipe')
    list_filter = ('user', 'recipe')
    empty_value_display = EMPTY_VALUE


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ('user', 'recipe')
    list_filter = ('user', 'recipe')
    empty_value_display = EMPTY_VALUE
