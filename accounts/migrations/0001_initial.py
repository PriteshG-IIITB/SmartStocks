# Generated by Django 2.2 on 2019-04-18 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Financials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stocks_owned', models.TextField(blank=True)),
                ('account_num', models.IntegerField(default=0)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=9)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
