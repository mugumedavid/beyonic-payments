# Generated by Django 3.2.10 on 2021-12-19 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0006_alter_payment_payment_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_request',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='models.paymentrequest'),
        ),
    ]
