# Generated by Django 4.2.5 on 2023-11-30 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0004_vippersons_delete_workers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Love',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('auther', models.CharField(max_length=70)),
                ('bithday', models.DateField()),
                ('is_interesting', models.BooleanField(default=True)),
                ('year_public', models.DateTimeField()),
                ('genre', models.CharField(max_length=30)),
                ('size', models.IntegerField()),
            ],
        ),
    ]
