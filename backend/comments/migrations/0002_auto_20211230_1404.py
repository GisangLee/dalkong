# Generated by Django 3.2 on 2021-12-30 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_auto_20211230_1403'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '댓글', 'verbose_name_plural': '댓글'},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='room',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post', verbose_name='게시글'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='desc',
            field=models.CharField(max_length=255, verbose_name='댓글 내용'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
    ]
