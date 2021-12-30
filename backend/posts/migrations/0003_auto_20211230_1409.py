# Generated by Django 3.2 on 2021-12-30 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20211230_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='room',
        ),
        migrations.AddField(
            model_name='photo',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='posts.post', verbose_name='해당 게시글'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='caption',
            field=models.TextField(blank=True, verbose_name='설명'),
        ),
    ]
