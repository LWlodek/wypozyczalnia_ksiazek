# Generated by Django 4.2.2 on 2023-06-17 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_borrowedbook_alter_book_availability_userprofile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowedbook',
            name='user_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.userprofile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
