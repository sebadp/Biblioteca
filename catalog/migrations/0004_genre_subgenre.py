# Generated by Django 3.1.3 on 2020-12-05 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20201205_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='subgenre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.subgenre'),
        ),
    ]
