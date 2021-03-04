# Generated by Django 3.1.4 on 2021-03-04 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usr_base', '0001_initial'),
        ('admin_base', '0002_auto_20210304_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='professional_mst',
            name='Postcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='professional_mst',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='booking_slot',
            name='UserName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='usr_base.user_mst'),
        ),
    ]