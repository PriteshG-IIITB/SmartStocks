# Generated by Django 2.0.7 on 2019-04-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=20)),
                ('company_name', models.CharField(blank=True, max_length=100)),
                ('table_data', models.TextField(blank=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_downloaded', models.BooleanField(default=False)),
            ],
        ),
    ]
