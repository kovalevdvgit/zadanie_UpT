# Generated by Django 4.2.2 on 2024-02-15 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mainmenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='меню')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='menu_lv2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='под_меню')),
                ('parent_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.mainmenu', verbose_name='меню')),
            ],
            options={
                'verbose_name': 'Под_Меню',
                'verbose_name_plural': 'Под_Меню',
            },
        ),
        migrations.CreateModel(
            name='menu_lv3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='под_под_меню')),
                ('parent_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menu_lv2', verbose_name='под_меню')),
            ],
            options={
                'verbose_name': 'Под_Под_Меню',
                'verbose_name_plural': 'Под_Под_Меню',
            },
        ),
    ]
