# Generated by Django 3.1.2 on 2021-01-16 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr', models.CharField(max_length=200, verbose_name='Адрес')),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=10, verbose_name='Проблема')),
                ('obj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='man.place')),
            ],
        ),
    ]
