# Generated by Django 4.0.6 on 2023-07-05 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jornal_interno', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Leitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='autor',
        ),
        migrations.AddField(
            model_name='noticia',
            name='edicao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jornal_interno.edicao'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='conteudo',
            field=models.TextField(max_length=700),
        ),
        migrations.AddField(
            model_name='comentario',
            name='leitor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jornal_interno.leitor'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jornal_interno.autor'),
        ),
    ]