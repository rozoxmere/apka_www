# Generated by Django 4.1.2 on 2022-10-12 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
    ]
