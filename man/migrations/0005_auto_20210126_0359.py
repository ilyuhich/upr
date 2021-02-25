# Generated by Django 3.1.2 on 2021-01-26 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('man', '0004_auto_20210126_0333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Размещение', 'verbose_name_plural': 'Размещения'},
        ),
        migrations.AlterModelOptions(
            name='problem',
            options={'verbose_name': 'Проблема', 'verbose_name_plural': 'Проблемы'},
        ),
        migrations.AddField(
            model_name='rig',
            name='ident',
            field=models.CharField(max_length=100, null=True, verbose_name='Идентификатор'),
        ),
    ]