# Generated by Django 4.1 on 2022-08-29 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('psg_cse_api', '0003_alter_calc_declared_value_rate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calc',
            name='delivery_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psg_cse_api.deliverytype', verbose_name='Тип доставки'),
        ),
        migrations.AlterField(
            model_name='calc',
            name='type_of_cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psg_cse_api.typeofcargo', verbose_name='Тип груза'),
        ),
        migrations.AlterField(
            model_name='calc',
            name='urgency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psg_cse_api.urgency', verbose_name='Срочность доставки'),
        ),
    ]