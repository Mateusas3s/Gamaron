# Generated by Django 2.1.3 on 2018-11-15 19:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('avatar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Name')),
                ('description', models.TextField(max_length=250, verbose_name='Description')),
                ('avatar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='avatar.Avatar', verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itens', models.ManyToManyField(blank=True, to='itens.Iten', verbose_name='Itens')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserPlayer', verbose_name='Player')),
            ],
        ),
    ]
