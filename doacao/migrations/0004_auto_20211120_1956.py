# Generated by Django 3.2.7 on 2021-11-20 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doacao', '0003_instituicao_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instituicao',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
