# Generated by Django 3.2.10 on 2021-12-19 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_alter_paymentrequest_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentrequest',
            name='date',
            field=models.DateTimeField(verbose_name='Issued on'),
        ),
    ]
