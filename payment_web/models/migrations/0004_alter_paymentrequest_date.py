# Generated by Django 3.2.10 on 2021-12-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_paymentrequest_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentrequest',
            name='date',
            field=models.DateTimeField(verbose_name='Issue on'),
        ),
    ]