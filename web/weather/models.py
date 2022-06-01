from django.db import models


# Create your models here.
class Station(models.Model):
    code = models.IntegerField(help_text='지점 코드')
    lon = models.FloatField(help_text='경도')
    lat = models.FloatField(help_text='위도')
    name = models.CharField(help_text='지점 이름', max_length=64)
    obser_begin = models.DateTimeField(help_text='관측 시작일', null=True)
    obser_end = models.DateTimeField(help_text='관측 마지막일'
                                                 '관측 지점이 이동됐을 경우에도, 값이 채워지고,'
                                                 '같은 지점이 생성된다.', null=True, blank=True)
    type = models.CharField(help_text='지점 종류(asos, aws, rda, etc..)', max_length=32, blank=True, null=True)
    objects = models.Manager()

    class Meta:
        db_table = 'station'


class AsosWeatherDaily(models.Model):
    st = models.ForeignKey(Station, on_delete=models.CASCADE, help_text='Station Table Id')
    tm = models.DateField(help_text='기상 관측 시점')
    avg_temp = models.FloatField(help_text='평균 기온', null=True, blank=True)
    max_temp = models.FloatField(help_text='최고 기온', null=True, blank=True)
    min_temp = models.FloatField(help_text='최저 기온', null=True, blank=True)
    pptn = models.FloatField(help_text='강수량(precipitation)', null=True, blank=True)
    ssn_tm = models.FloatField(help_text='일조 시간(sunshine_time)', null=True, blank=True)
    rhum = models.FloatField(help_text='상대습도(relative humidity)', null=True, blank=True)
    avg_wsd = models.FloatField(help_text='평균 풍속(avg_wsd)', null=True, blank=True)
    evp = models.FloatField(help_text='증발량(evaporation)', null=True, blank=True)
    isn = models.FloatField(help_text='일사량(insolation)', null=True, blank=True)

    class Meta:
        db_table = 'asos_weather_daily'
