# Generated by Django 3.1.3 on 2020-12-20 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fact', '0003_auto_20201123_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fact',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='fact.category', verbose_name='Категория'),
            preserve_default=False,
        ),
    ]
