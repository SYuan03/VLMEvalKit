import pandas as pd

original_file_path = './data/CVQA-2024-07-31-15-44-33.tsv'

df = pd.read_csv(original_file_path, sep='\t')  # 读取原始文件

df['index'] = range(len(df))  # 添加一个名为 'index' 的列，其内容是从 0 开始的连续整数

output_file_path = './data/indexed_' + original_file_path.split('/')[-1]  # 生成输出文件路径
df.to_csv(output_file_path, sep='\t', index=False)  # 保存文件，确保不包括默认的索引列
