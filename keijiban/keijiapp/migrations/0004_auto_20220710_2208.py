# Generated by Django 3.2.5 on 2022-07-10 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keijiapp', '0003_auto_20220710_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threadmodel',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, help_text='作成日'),
        ),
        migrations.AlterField(
            model_name='threadmodel',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, help_text='更新日'),
        ),
    ]
