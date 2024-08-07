import pandas as pd
import os
from tqdm import tqdm
import time
import base64

# 定义数据集目录
parquet_dir = '/cpfs01/user/dingshengyuan/mydataset/cvqa/data'

# 获取所有 Parquet 文件路径
parquet_files = [os.path.join(parquet_dir, f) for f in os.listdir(parquet_dir) if f.endswith('.parquet')]

# 读取并处理所有 Parquet 文件
dfs = []
for file in tqdm(parquet_files, desc='Reading Parquet files'):
    df = pd.read_parquet(file)
    # 处理'image'列中的图像数据
    if 'image' in df.columns:
        df['image'] = df['image'].apply(lambda x: base64.b64encode(x['bytes']).decode('utf-8') if isinstance(x, dict) and 'bytes' in x else None)
    dfs.append(df)


# 合并所有数据帧
combined_df = pd.concat(dfs, ignore_index=True)

# 添加索引列
combined_df['index'] = range(len(combined_df))

# 将列名转换为小写
combined_df.columns = combined_df.columns.str.lower()

combined_df[['A', 'B', 'C', 'D']] = pd.DataFrame(combined_df['options'].tolist(), index=combined_df.index)


# 保存前10行到一个小文件
output_file = './data/CVQA-' + time.strftime('%Y-%m-%d-%H-%M-%S') + '.tsv'
file_name_10 = 'head_10_' + output_file.split('/')[-1]
combined_df.head(10).to_csv('./data/' + file_name_10, sep='\t', index=False)

# 将整个数据帧以分块方式写入TSV文件
chunksize = 100
with tqdm(total=combined_df.shape[0], desc='Writing to TSV file') as pbar:
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        combined_df.head(0).to_csv(f, sep='\t', index=False)  # 写入列名
        for i in range(0, combined_df.shape[0], chunksize):
            combined_df.iloc[i:i+chunksize].to_csv(f, sep='\t', index=False, header=False)
            pbar.update(chunksize)

print('Data processing and saving completed.')
