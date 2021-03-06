# Generated by Django 3.2 on 2021-05-04 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('url', models.URLField(max_length=1024)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.IntegerField(choices=[(0, 'Article'), (1, 'Broadcast'), (2, 'Public Speaking')], default=0)),
                ('date_published', models.DateField()),
            ],
            options={
                'ordering': ['-date_published'],
            },
        ),
    ]
