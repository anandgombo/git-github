# Generated by Django 5.0.3 on 2024-05-31 14:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_remove_item_created_by'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default=3, upload_to='items/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
