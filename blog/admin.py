from django.contrib import admin
from .models import *
from extensions.utils import jalali_converter

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	list_display = ('title','body')
	search_fields = ('title','body')

admin.site.register(Post,BlogAdmin)

class ExpenseAdmin(admin.ModelAdmin):
	list_display = ['text','amount']
	search_fields = ['text','amount']

admin.site.register(Expense,ExpenseAdmin)


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title' , 'status', 'jpublish' , 'category_str')
	list_filter = ('status' , 'publish')
	search_fields = ('title','description')
	# با پر کردن عنوان اسلاگ هم پر میشه 
	prepopulated_fields = {'slug':('title',)}

	# نمایش دسته بندی ها در بخش مقالات
	def category_str(self , obj):
		return ", ".join([category.title for category in obj.category.all()])
	category_str.short_description = 'دسته بندی'

admin.site.register(Article , ArticleAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_filter = ('title', 'status')
	list_display = ('title', 'parent' ,'status')
	search_fields = ('title',)

admin.site.register(Category , CategoryAdmin)
	

admin.site.register(Token)

