# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mTf49aQECVAod9S3eTY2IjKykX2pJNyO
"""

import numpy as np  # 선형 대수 처리를 위한 라이브러리
import pandas as pd  # 데이터 처리 및 CSV 파일 입출력을 위한 라이브러리 (예: pd.read_csv)

import pandas as pd
data = pd.read_csv("/content/common_passwords.csv")

data.head(10)

# 대소문자를 구분하지 않고 가장 일반적인 50개의 비밀번호

from collections import Counter

data_count_case_insensitive = pd.DataFrame(pd.Series(dict(Counter(','.join(data["password"].str.lower()).split(',')))).sort_values(ascending=False))
data_count_case_insensitive[:50]

# 대소문자를 구분하여 가장 일반적인 50개의 비밀번호

data_count_case_sensitive = pd.DataFrame(pd.Series(dict(Counter(','.join(data["password"]).split(',')))).sort_values(ascending=False))
data_count_case_sensitive[:50]

# 데이터프레임 병합
merged_data = pd.merge(data_count_case_insensitive, data_count_case_sensitive, left_index=True, right_index=True)
# 열 이름 변경
merged_data.columns = ["Count (Case Insensitive)", "Count (Case Sensitive)"]
# 하나의 열로 합치기
merged_data["Combined Count"] = merged_data["Count (Case Insensitive)"] + merged_data["Count (Case Sensitive)"]
# 내림차순 정렬
merged_data = merged_data.sort_values(by="Combined Count", ascending=False)

merged_data[:50]

password_df = pd.DataFrame(merged_data.index, columns=["Password"])
password_df[:50]

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 데이터프레임에서 비밀번호 데이터 추출
password_list = password_df["Password"].tolist()

# 비밀번호 리스트를 공백으로 연결하여 텍스트 생성
password_text = " ".join(password_list)

# WordCloud 객체 생성 및 설정
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(password_text)

# 워드 클라우드 시각화
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Password Word Cloud")
plt.show()

password_df.to_csv("password_list.csv", index=False)