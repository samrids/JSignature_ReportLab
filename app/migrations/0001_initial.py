# Generated by Django 3.2.4 on 2022-10-27 11:12

from django.db import migrations, models
import jsignature.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', jsignature.fields.JSignatureField(blank=True, null=True, verbose_name='Signature')),
                ('signature_date', models.DateTimeField(blank=True, null=True, verbose_name='Signature date')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]