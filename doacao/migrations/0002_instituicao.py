# Generated by Django 3.2.7 on 2021-11-20 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
    ]