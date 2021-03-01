from django.http import Http404
from django.shortcuts import get_object_or_404
from blog.models import *

# نمایش دادن بخش ها طبق دسترسی که دارند
class FieldMixin():
	# یک ریکوئست رو میگیره و بهش ریسپانس می ده
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_superuser:
			self.fields = ['author','title','slug','category','description','image','status']
		elif request.user.is_author:
			self.fields = ['title','slug','category','description','image']
		else:
			raise Http404
		return super().dispatch(request, *args, **kwargs)

# بعد از ثبت مقاله نویسنده درج شود
class FormValidMixin():
	def form_valid(self , form):
		if self.request.user.is_superuser:
			form.save()
		else:
			self.obj = form.save(commit = False)
			self.obj.author = self.request.user
			self.obj.status = 'd'
		return super().form_valid(form)

# هر مقاله تنها توسط نویسنده خود آن کاربر تغییر داده شود
class AuthorAccessMixin():
	def dispatch(self, request,pk ,  *args, **kwargs):
		article = get_object_or_404(Article , pk = pk)
		if article.author == request.user or request.user.is_superuser:
			return super().dispatch(request, *args, **kwargs)
		else:
			raise Http404

# هر مقاله تنها توسط نویسنده خود آن کاربر حذف شود
class SuperUserAccessMixin():
	def dispatch(self, request ,  *args, **kwargs):
		if request.user.is_superuser:
			return super().dispatch(request, *args, **kwargs)
		else:
			raise Http404	