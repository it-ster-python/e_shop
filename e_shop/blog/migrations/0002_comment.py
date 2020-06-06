# Generated by Django 3.0.3 on 2020-03-29 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=20, verbose_name='Comment author name.')),
                ('comment_text', models.CharField(max_length=255, verbose_name='Comment text.')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Comment post time.')),
                ('comment_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article')),
            ],
            options={
                'verbose_name': 'Comment for article',
                'verbose_name_plural': 'Comments for article',
                'db_table': 'articles_comments',
            },
        ),
    ]