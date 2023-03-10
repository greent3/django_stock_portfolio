# Generated by Django 4.1.3 on 2022-12-31 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=6)),
                ('purchase_date', models.DateField()),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('exchange', models.CharField(max_length=10)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('sell_date', models.DateField(blank=True, null=True)),
                ('sell_price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
            ],
            options={
                'ordering': ['-purchase_date'],
            },
        ),
    ]
