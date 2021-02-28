from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# ایجاد دسترسی ویژه برای کاربران
class User(AbstractUser):
	email = models.EmailField(unique=True, verbose_name='ایمیل')

	is_author = models.BooleanField(default=False, verbose_name="وضعیت نویسندگی")
	special_user = models.DateTimeField(default=timezone.now, verbose_name="کاربر ویژه تا")

	def is_special_user(self):
		if self.special_user > timezone.now():
			return True
		else:
			return False
    # برای نمایش به صورت تیک در پنل ادمین
	is_special_user.boolean = True
	is_special_user.short_description = "وضعیت کاربر ویژه"

