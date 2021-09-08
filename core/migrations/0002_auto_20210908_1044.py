# Generated by Django 3.2.7 on 2021-09-08 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='food',
            name='food_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='core.foodcategory'),
        ),
    ]
