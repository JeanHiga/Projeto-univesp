# Generated by Django 3.2.7 on 2021-11-22 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doacao', '0009_produto_instituicao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='instituicao',
        ),
        migrations.AddField(
            model_name='instituicao',
            name='produto',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='doacao.produto'),
            preserve_default=False,
        ),
    ]