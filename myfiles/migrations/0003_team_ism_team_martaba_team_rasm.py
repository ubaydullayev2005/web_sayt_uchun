# Generated by Django 4.1.3 on 2022-11-26 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0002_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='ism',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='martaba',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='rasm',
            field=models.ImageField(default=0, upload_to='media'),
            preserve_default=False,
        ),
    ]