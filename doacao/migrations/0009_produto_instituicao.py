# Generated by Django 3.2.7 on 2021-11-22 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doacao', '0008_alter_produto_quantidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='instituicao',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='doacao.instituicao'),
            preserve_default=False,
        ),
    ]