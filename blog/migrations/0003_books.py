# Generated by Django 3.0.3 on 2020-03-22 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200319_0733'),
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookID', models.IntegerField(default=0)),
                ('title', models.CharField(default='', max_length=100)),
                ('authors', models.CharField(default='', max_length=100)),
                ('average_rating', models.CharField(default='', max_length=100)),
                ('isbn', models.CharField(default='', max_length=100)),
                ('isbn13', models.CharField(default='', max_length=100)),
                ('language_code', models.CharField(default='', max_length=100)),
                ('num_pages', models.IntegerField(default=0)),
                ('ratings_count', models.IntegerField(default=0)),
                ('text_reviews_count', models.IntegerField(default=0)),
                ('publication_date', models.CharField(default='', max_length=100)),
                ('publisher', models.CharField(default='', max_length=100)),
            ],
        ),
    ]