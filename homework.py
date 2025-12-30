import numpy as np
import pandas as pd


pd.read_csv("seoul_lib_202511.csv")
df  = pd.read_csv("seoul_lib_202511.csv",encoding="utf-8-sig")

# # print("shape", df.shape)
# print(df.head(3))


# df.to_csv("test_sample_plus.csv", index=False, encoding="utf-8-sig")
# print("test_sample_plus.csv 생성 완료입니다.")


top10 = df.sort_values(by = "대출건수",ascending=False).head(5)
print(top10)

top10.to_csv("test_sample_plus_top11.csv",index=False,encoding="utf-8-sig")

