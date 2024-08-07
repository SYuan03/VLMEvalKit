import pandas as pd

file_name = 'head_10_CVQA-2024-07-31-17-10-12.tsv'
# 读取生成的TSV文件
df = pd.read_csv('./data/' + file_name, sep='\t')

# 打印第一行完整的数据
row_data = df.iloc[4]
print(row_data)

# 保存这行数据到新文件
output_file_name = './data/temp.csv'
row_data.to_csv(output_file_name, index=False)
