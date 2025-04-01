from django.contrib import admin
from .models import Reviews, Ratings, Favourites, User


class ReviewsInline(admin.StackedInline):
    model = Reviews


class RatingsInline(admin.TabularInline):
    model = Ratings

class FavouritesInline(admin.TabularInline):
    model = Favourites


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    search_fields = ('id', 'email')
    list_filter = ('id', 'email')

    inlines = [
        ReviewsInline, RatingsInline, FavouritesInline,
    ]


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'film', 'user', 'reviews_body')
    search_fields = ('film', 'user')
    list_filter = ('film', 'user')


@admin.register(Ratings)
class RatingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'film', 'user', 'rating')
    search_fields = ('film', 'user', 'rating')
    list_filter = ('film', 'user', 'rating')

@admin.register(Favourites)
class FavouritesAdmin(admin.ModelAdmin):
    list_display = ('id', 'film', 'user')
    search_fields = ('film', 'user')
    list_filter = ('film', 'user')