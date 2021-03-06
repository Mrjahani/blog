# Generated by Django 3.1.4 on 2021-02-10 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210208_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته بندی')),
                ('slug', models.SlugField(max_length=255, verbose_name='اسلاگ')),
                ('status', models.BooleanField(default=True, verbose_name='نمایش دسته بندی')),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.AlterModelOptions(
            name='expense',
            options={'verbose_name': 'خرج', 'verbose_name_plural': 'مخارج '},
        ),
    ]
