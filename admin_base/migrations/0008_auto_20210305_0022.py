# Generated by Django 3.1.4 on 2021-03-04 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_base', '0007_feedback_mst_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback_mst',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]