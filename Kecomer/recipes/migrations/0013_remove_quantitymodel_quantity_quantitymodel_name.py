# Generated by Django 4.1.1 on 2022-10-17 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_quantitymodel_recipesmodel_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quantitymodel',
            name='quantity',
        ),
        migrations.AddField(
            model_name='quantitymodel',
            name='name',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
