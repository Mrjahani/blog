# Generated by Django 3.1.4 on 2020-12-31 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_expense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(),
        ),
    ]