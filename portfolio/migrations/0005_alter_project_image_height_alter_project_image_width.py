# Generated by Django 4.0.2 on 2022-03-28 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_project_image_height_project_image_width_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image_height',
            field=models.PositiveIntegerField(blank=True, default='300', editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image_width',
            field=models.PositiveIntegerField(blank=True, default='400', editable=False, null=True),
        ),
    ]
