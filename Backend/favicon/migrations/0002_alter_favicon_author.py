# Generated by Django 4.0.6 on 2022-08-08 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0001_initial'),
        ('favicon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favicon',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favicons', to='user_control.customuser'),
        ),
    ]
