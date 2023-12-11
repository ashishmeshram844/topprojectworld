# Generated by Django 3.2.5 on 2021-07-28 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='student_account_photo')),
                ('fullname', models.CharField(blank=True, max_length=100)),
                ('optional_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('optional_mobile', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('zipcode', models.IntegerField(blank=True, null=True)),
                ('forget_password_token', models.CharField(blank=True, max_length=300, null=True)),
                ('sel_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
