# Generated by Django 4.0.5 on 2022-07-15 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_sno_post_sno_alter_post_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blogcomment'),
        ),
    ]