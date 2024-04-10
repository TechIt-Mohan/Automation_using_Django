# Generated by Django 5.0.3 on 2024-04-10 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('employee_name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('retirement', models.DecimalField(decimal_places=2, max_digits=10)),
                ('other_benefits', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_benefits', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_compensation', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
