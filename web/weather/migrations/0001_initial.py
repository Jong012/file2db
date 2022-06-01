# Generated by Django 4.0.4 on 2022-05-31 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(help_text='지점 코드')),
                ('lon', models.FloatField(help_text='경도')),
                ('lat', models.FloatField(help_text='위도')),
                ('name', models.CharField(help_text='지점 이름', max_length=64)),
                ('obser_begin', models.DateTimeField(help_text='관측 시작일', null=True)),
                ('obser_end', models.DateTimeField(blank=True, help_text='관측 마지막일관측 지점이 이동됐을 경우에도, 값이 채워지고,같은 지점이 생성된다.', null=True)),
                ('type', models.CharField(blank=True, help_text='지점 종류(asos, aws, rda, etc..)', max_length=32, null=True)),
            ],
            options={
                'db_table': 'station',
            },
        ),
        migrations.CreateModel(
            name='AsosWeatherDaily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tm', models.DateField(help_text='기상 관측 시점')),
                ('avg_temp', models.FloatField(blank=True, help_text='평균 기온', null=True)),
                ('max_temp', models.FloatField(blank=True, help_text='최고 기온', null=True)),
                ('min_temp', models.FloatField(blank=True, help_text='최저 기온', null=True)),
                ('pptn', models.FloatField(blank=True, help_text='강수량(precipitation)', null=True)),
                ('ssn_tm', models.FloatField(blank=True, help_text='일조 시간(sunshine_time)', null=True)),
                ('rhum', models.FloatField(blank=True, help_text='상대습도(relative humidity)', null=True)),
                ('avg_wsd', models.FloatField(blank=True, help_text='평균 풍속(avg_wsd)', null=True)),
                ('evp', models.FloatField(blank=True, help_text='증발량(evaporation)', null=True)),
                ('isn', models.FloatField(blank=True, help_text='일사량(insolation)', null=True)),
                ('st', models.ForeignKey(help_text='Station Table Id', on_delete=django.db.models.deletion.CASCADE, to='weather.station')),
            ],
            options={
                'db_table': 'asos_weather_daily',
            },
        ),
    ]
