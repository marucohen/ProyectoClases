# Generated by Django 4.2.1 on 2023-07-02 20:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pediTuClaseApp', '0003_remove_claseproducto_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='claseproducto',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='claseproducto',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]