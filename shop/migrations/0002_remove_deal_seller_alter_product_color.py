# Generated by Django 4.2.1 on 2023-05-12 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='seller',
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('WHITE', 'White'), ('ReD', 'Red'), ('YELLOW', 'Yellow'), ('PINK', 'Pink')], default='WHITE', max_length=9),
        ),
    ]
