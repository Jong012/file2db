from pprint import pprint

from django.core.management import BaseCommand

from weather.models import Station
from web.settings import BASE_DIR
import pandas as pd
import numpy as np


class Command(BaseCommand):
    def handle(self, *args, **options):
        # 데이터 경로를 입력받는다.
        # 파일을 읽는다
        # 파일을 db 에 넣는다
        # 파일은 두종류 csv 와 xlsx
        # 테이블에 따라 달라진다.
        file_path = f'{BASE_DIR}/data/asos-stations.csv'  # glob 을 활용하여 읽어들일 수 있다.
        df = pd.read_csv(file_path)
        df.replace(np.nan, None, inplace=True)
        pprint(df)

        # 모델 필드 네임과 파일의 header 를 비교.
        field_nm = [f.name for f in Station._meta.get_fields()]
        df_head = df.head()

        # iterrows 보다 itertuples 가 성능이 더좋음
        for row in df.itertuples(index=False):
            pprint(row._asdict())
            st = Station(**row._asdict())
            st.save()