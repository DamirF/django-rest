# Generated by Django 4.1 on 2022-08-29 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('psg_cse_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calc',
            name='declared_value_rate',
            field=models.IntegerField(null=True, verbose_name='Объявленная стоимость груза'),
        ),
        migrations.AlterField(
            model_name='calc',
            name='delivery_type',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='psg_cse_api.deliverytype', verbose_name='Тип доставки'),
        ),
        migrations.AlterField(
            model_name='calc',
            name='insurance_rate',
            field=models.IntegerField(null=True, verbose_name='Страховая стоимость груза'),
        ),
        migrations.AlterField(
            model_name='calc',
            name='urgency',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='psg_cse_api.urgency', verbose_name='Срочность доставки'),
        ),
    ]
