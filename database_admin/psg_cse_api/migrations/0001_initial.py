# Generated by Django 4.1 on 2022-08-29 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Тип доставки')),
            ],
            options={
                'verbose_name': 'Тип доставки',
                'verbose_name_plural': 'Типы доставки',
                'db_table': 'table_007_delivery_type',
            },
        ),
        migrations.CreateModel(
            name='TypeOfCargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Тип груза')),
            ],
            options={
                'verbose_name': 'Тип груза',
                'verbose_name_plural': 'Типы груза',
                'db_table': 'table_006_types_of_cargo',
            },
        ),
        migrations.CreateModel(
            name='Urgency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Срочность доставки')),
            ],
            options={
                'verbose_name': 'Срочность доставки',
                'verbose_name_plural': 'Срочность доставки',
                'db_table': 'table_005_urgencies',
            },
        ),
        migrations.CreateModel(
            name='Calc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sending_point', models.CharField(max_length=150, verbose_name='Город отправки')),
                ('arrival_point', models.CharField(max_length=150, verbose_name='Город прибытия')),
                ('weight', models.FloatField(verbose_name='Вес')),
                ('volume', models.FloatField(verbose_name='Объем')),
                ('declared_value_rate', models.IntegerField(verbose_name='Объявленная стоимость груза')),
                ('insurance_rate', models.IntegerField(verbose_name='Страховая стоимость груза')),
                ('is_test', models.BooleanField(default=False, verbose_name='Выключить тестовую версию')),
                ('delivery_type', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='psg_cse_api.deliverytype', verbose_name='Тип доставки')),
                ('type_of_cargo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='psg_cse_api.typeofcargo', verbose_name='Тип груза')),
                ('urgency', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='psg_cse_api.urgency', verbose_name='Срочность доставки')),
            ],
            options={
                'db_table': 'table_004_calc_parameters',
            },
        ),
    ]
