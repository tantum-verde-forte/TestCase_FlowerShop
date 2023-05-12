from django.contrib import admin
from .models import Consumer, Seller, Product, Seller_review, Product_review, Deal


@admin.register(Consumer)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Seller)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Seller_review)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Product_review)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Deal)
class AuthorAdmin(admin.ModelAdmin):
    pass

