import pandas as pd

file_name = 'CVQA-2024-07-31-15-27-15.tsv'

df = pd.read_csv('./data/' + file_name, sep='\t')

# 保存前10行到一个新的TSV文件
file_name_10 = 'head_10_' + file_name
df.head(10).to_csv('./data/' + file_name_10, sep='\t', index=True)
