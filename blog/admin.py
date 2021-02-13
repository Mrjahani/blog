from django.contrib import admin
from .models import *
from extensions.utils import jalali_converter

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	list_display = ('title','body')
	search_fields = ('title','body')

class ExpenseAdmin(admin.ModelAdmin):
	list_display = ['text','amount']
	search_fields = ['text','amount']

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title' , 'status', 'jpublish' , 'category_str')
	list_filter = ('title','status' , 'publish')
	search_fields = ('title','description')
	# با پر کردن عنوان اسلاگ هم پر میشه 
	prepopulated_fields = {'slug':('title',)}

	# نمایش دسته بندی ها در بخش مقالات
	def category_str(self , obj):
		return ", ".join([category.title for category in obj.category.all()])
	category_str.short_description = 'دسته بندی'

class CategoryAdmin(admin.ModelAdmin):
	list_filter = ('title', 'status')
	list_display = ('title', 'status')
	search_fields = ('title',)

	

admin.site.register(Post,BlogAdmin)
admin.site.register(Expense,ExpenseAdmin)
admin.site.register(Token)

admin.site.register(Article , ArticleAdmin)
admin.site.register(Category , CategoryAdmin)
