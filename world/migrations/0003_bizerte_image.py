# Generated by Django 2.2.3 on 2019-07-13 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_bizerte'),
    ]

    operations = [
        migrations.AddField(
            model_name='bizerte',
            name='image',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
