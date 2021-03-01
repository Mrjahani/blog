from django.http import Http404

# نمایش دادن بخش ها طبق دسترسی که دارند
class FieldMixin():
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