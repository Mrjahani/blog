from django.contrib import admin
from .models import *

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	list_display = ('title','body')
	search_fields = ('title','body')

class ExpenseAdmin(admin.ModelAdmin):
	list_display = ['text','amount']
	search_fields = ['text','amount']

admin.site.register(Post,BlogAdmin)
admin.site.register(Expense,ExpenseAdmin)
admin.site.register(Token)
