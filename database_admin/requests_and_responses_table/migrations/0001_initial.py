# Generated by Django 4.1 on 2022-08-27 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_http_request', models.TextField(verbose_name='HTTP-запрос')),
                ('api_http_response', models.TextField(verbose_name='Ответ сервера')),
                ('api_http_request_send_time', models.DateTimeField(verbose_name='Время отправки запроса')),
                ('api_http_response_waiting_time', models.CharField(max_length=10, verbose_name='Время ожидания ответа')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Отправитель')),
            ],
            options={
                'verbose_name': 'HTTP - запрос',
                'verbose_name_plural': 'HTTP - запросы',
                'db_table': 'table_001_request_response',
            },
        ),
    ]