# Generated by Django 4.0.4 on 2022-05-24 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('barcha', models.IntegerField()),
                ('ish_jarayonida', models.IntegerField()),
                ('bajarildi', models.IntegerField()),
                ('muddati_otgan', models.IntegerField()),
                ('muddati_otin_ijro_etilgan', models.IntegerField()),
            ],
        ),
    ]