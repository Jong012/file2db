# 리팩토링을 하기 전에 먼저 구현부터
import pandas as pd
from web.settings import BASE_DIR

if __name__ == '__main__':
    # 데이터 경로를 입력받는다.
    # 파일을 읽는다
    # 파일을 db 에 넣는다
    file_path = f'{BASE_DIR}/data/asos-stations.csv' # glob 을 활용하여 읽어들일 수 있다.
    df = pd.read_csv(file_path)





