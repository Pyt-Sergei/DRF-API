# Generated by Django 3.2.7 on 2021-10-02 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('image', models.ImageField(upload_to='site_media/')),
                ('url', models.URLField(blank=True, null=True)),
                ('path', models.CharField(default='', max_length=200)),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('parent', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
