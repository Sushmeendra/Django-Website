# Generated by Django 2.2.7 on 2019-11-16 17:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20191116_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('investment_amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9223372036854775807)])),
                ('investment_date', models.DateField()),
                ('investment_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('user_Portfolio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='my_app.User')),
                ('port_Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Bonds',
            fields=[
                ('investment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='my_app.Investment')),
                ('bond_Issuer', models.CharField(max_length=50)),
                ('bond_Interest_Rate', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('bond_maturity_date', models.DateField()),
            ],
            bases=('my_app.investment',),
        ),
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('investment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='my_app.Investment')),
            ],
            bases=('my_app.investment',),
        ),
        migrations.CreateModel(
            name='HedgeFunds',
            fields=[
                ('investment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='my_app.Investment')),
                ('fund_Name', models.CharField(max_length=50)),
                ('fund_Provider', models.CharField(max_length=50)),
                ('return_Rate', models.IntegerField(validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(5)])),
            ],
            bases=('my_app.investment',),
        ),
        migrations.CreateModel(
            name='MutualFunds',
            fields=[
                ('investment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='my_app.Investment')),
                ('fund_Name', models.CharField(max_length=50)),
                ('fund_Provider_Bank', models.CharField(max_length=50)),
                ('return_Rate', models.IntegerField(validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(5)])),
            ],
            bases=('my_app.investment',),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('investment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='my_app.Investment')),
                ('stock_CODE', models.CharField(max_length=5)),
                ('expected_Return_Rate', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(200)])),
            ],
            bases=('my_app.investment',),
        ),
        migrations.AddField(
            model_name='investment',
            name='investment_parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.Portfolio'),
        ),
    ]