# Generated by Django 4.0.5 on 2023-02-06 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date'),
        ),
    ]