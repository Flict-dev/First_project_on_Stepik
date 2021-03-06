# Generated by Django 3.1.4 on 2021-01-07 14:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Загаловок')),
                ('text', models.TextField(max_length=500, verbose_name='Текст')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Главаная страница',
                'verbose_name_plural': 'Главные страницы',
            },
        ),
    ]
