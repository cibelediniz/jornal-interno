# Generated by Django 4.0.6 on 2023-07-03 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquete', '0003_rename_pub_data_pergunta_data_pub_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alternativa',
            name='texto',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='pergunta',
            name='enunciado',
            field=models.CharField(max_length=150),
        ),
    ]
