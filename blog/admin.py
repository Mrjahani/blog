from django.contrib import admin
from .models import *
from extensions.utils import jalali_converter

# Register your models here.
# admin header change
admin.site.site_header = 'پنل مدیریت پرسنال ادمین'

# action admin
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "انتشار مقالات انتخاب شده"

# action admin
def make_draft(modeladmin, request, queryset):
    queryset.update(status='d')
make_draft.short_description = "پیش نویس مقالات انتخاب شده"

class BlogAdmin(admin.ModelAdmin):
	list_display = ('title','body')
	search_fields = ('title','body')

admin.site.register(Post,BlogAdmin)

class ExpenseAdmin(admin.ModelAdmin):
	list_display = ['text','amount']
	search_fields = ['text','amount']

admin.site.register(Expense,ExpenseAdmin)


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('thumbnail_image' , 'title' ,'author', 'status', 'jpublish' , 'category_str')
	list_filter = ('status' , 'publish')
	search_fields = ('title','description')
	# با پر کردن عنوان اسلاگ هم پر میشه 
	prepopulated_fields = {'slug':('title',)}
	# برای بخش اکشن و مدیریت مقاله ها
	actions = [make_published , make_draft]


admin.site.register(Article , ArticleAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_filter = ('title', 'status')
	list_display = ('title', 'parent' ,'status')
	search_fields = ('title',)

admin.site.register(Category , CategoryAdmin)
	

admin.site.register(Token)

