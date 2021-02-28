from django.db import models
# برای استفاده auth خود جنگو
# from django.contrib.auth.models import User
# برای استفاده از سطج دسترسی های خودمون
from account.models import User
# برای url استفاده می شود 
from django.urls import reverse
from django.utils import timezone
from extensions.utils import jalali_converter
from django.utils.html import format_html
from ckeditor_uploader.fields import RichTextUploadingField

class Token(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    token = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.user}-{self.token}" 


class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.CharField(max_length=200)
    text = models.TextField()
    def __str__(self):
    	return self.title

    def get_absolute_url(self):
        return reverse('blog:posts',kwargs={'id':self.id})
    
class Expense(models.Model):
    text = models.CharField(max_length=255)    
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'خرج'
        verbose_name_plural = 'مخارج '
    def __str__(self):
    	return "{}-{}".format(self.date,self.text)   

    
class Category(models.Model):
    parent = models.ForeignKey('self', default=None,null=True , blank=True,on_delete=models.CASCADE , related_name='children',verbose_name='دسته بندی مادر')
    title = models.CharField(max_length=200 , verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=255 , verbose_name='اسلاگ', allow_unicode=True)
    status = models.BooleanField(default=True , verbose_name='نمایش دسته بندی')
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = ' دسته بندی ها'
        ordering = ['parent__id']
    def __str__(self):
        return self.title

class Article(models.Model):
    STATUS_CHOICES = (
        ('d','پیش نویس'), 
        ('p' , 'منتشر شده' ) 
    )
    author = models.ForeignKey(User , null=True , on_delete=models.SET_NULL , related_name='articles' , verbose_name='نویسنده')
    title = models.CharField(max_length=255 , verbose_name='عنوان')
    slug = models.SlugField(max_length=255,unique=True, allow_unicode=True , verbose_name='آدرس')
    category = models.ManyToManyField(Category , verbose_name='دسته بندی' , related_name="articles")
    description = RichTextUploadingField(config_name='default', verbose_name='توضیحات')
    image = models.ImageField(upload_to="images",null=True , verbose_name='تصویر')
    publish = models.DateTimeField(default=timezone.now , verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES , verbose_name='وضعیت')

    # برای فارسی کردن اسم در پنل مدیریت 
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title
    # فارسی سازی تاریخ 
    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار"
    # نمایش عکس در پنل مدیریت
    def thumbnail_image(self):
        return format_html("<img width=100 src='{}'>".format(self.image.url))
    thumbnail_image.short_description = 'تصویر'

    # نمایش دسته بندی ها در بخش مقالات
    def category_str(self):
        return ", ".join([category.title for category in self.category.all()])
    category_str.short_description = 'دسته بندی'
    # برای ریدایرکت شدن به صفحه مقاله ها در پنل اکانت
    def get_absolute_url(self):
        return reverse("account:articles")