from django.contrib import admin
from blog.models import Author, Category, SubCategory, Article


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name',)
    fields = ('name', 'text')


class SubCategoryAdmin(admin.ModelAdmin):
    model = SubCategory
    list_display = ('name', 'category')


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('meta_title', 'meta_desc', 'title', 'category', 'subcategory', 'create_date','pub_date', 'author')
    list_filter = ('category',)


class AuthorAdmin(admin.ModelAdmin):
    model = Author
    list_display = ['user', 'author']


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)


#test gita