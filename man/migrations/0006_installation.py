# Generated by Django 3.1.2 on 2021-01-26 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('man', '0005_auto_20210126_0359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Installation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(null=True, verbose_name='Добавлено')),
                ('description', models.CharField(max_length=100, verbose_name='Описание')),
                ('problem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='man.problem', verbose_name='Проблема')),
            ],
            options={
                'verbose_name': 'Установка',
                'verbose_name_plural': 'Установки',
            },
        ),
    ]
