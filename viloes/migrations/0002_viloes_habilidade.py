# Generated by Django 2.2.5 on 2019-09-24 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habilidade', '0001_initial'),
        ('viloes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='viloes',
            name='habilidade',
            field=models.ManyToManyField(related_name='habilidade', to='habilidade.Habilidade'),
        ),
    ]
