# Generated by Django 4.2.1 on 2023-05-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_detail', '0003_computercomponent'),
    ]

    operations = [
        migrations.AddField(
            model_name='desk',
            name='location',
            field=models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('B4', 'B4'), ('C1', 'C1'), ('C2', 'C2'), ('C3', 'C3'), ('C4', 'C4'), ('D1', 'D1'), ('D2', 'D2'), ('D3', 'D3'), ('D4', 'D4')], default='A1', max_length=2),
            preserve_default=False,
        ),
    ]
