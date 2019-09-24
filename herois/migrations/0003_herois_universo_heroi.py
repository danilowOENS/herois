# Generated by Django 2.2.5 on 2019-09-24 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('universo', '0001_initial'),
        ('herois', '0002_herois_habilidade_heroi'),
    ]

    operations = [
        migrations.AddField(
            model_name='herois',
            name='universo_heroi',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='universo_heroi', to='universo.Universo'),
            preserve_default=False,
        ),
    ]
