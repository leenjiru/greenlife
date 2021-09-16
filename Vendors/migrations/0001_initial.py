# Generated by Django 3.2.7 on 2021-09-16 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0004_alter_customer_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.customer')),
            ],
        ),
    ]