# Generated by Django 3.2 on 2021-12-28 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211228_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_method',
            field=models.CharField(choices=[('카카오', '카카오'), ('이메일', '이메일')], default='이메일', max_length=3),
        ),
    ]