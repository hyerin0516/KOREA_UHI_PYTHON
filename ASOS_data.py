# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#package 불러오기
import pandas as pd
from glob import glob
import os

#데이터가 저장되어 있는 폴더명 설정
base_dr = 'SURFACE_ASOS_data/'

#해당 지점 파일 목록읽기
fullnames = sorted(glob(os.path.join(base_dr, '*_100_MI*.zip')))
print("fullnames : {}".format(fullnames))

# 빈 DataFrame 생성
df = pd.DataFrame()

#모든 파일 읽어서 데이터 프레임 만들기
for fullname in fullnames[:] : 
    df1 = pd.read_csv('{}'.format(fullname),
                 thousands = ',',
                 compression='zip',
                 encoding= 'euc-kr')
    print("df1\n {}".format(df1))
    df = df.append(df1)

print("df\n {}".format(df))
print("len(df): {}".format(len(df)))