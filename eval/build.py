from vlmeval.config import supported_VLM
from vlmeval.tools import SKIP_MODELS
from colorama import Fore, Back, Style, init

import os

base_path = '/cpfs01/user/dingshengyuan/myfork/VLMEvalKit/eval'

# 创建文件夹
for model_name in supported_VLM.keys():
    if model_name in SKIP_MODELS:
        print(f'{Fore.GREEN}Skipping model: {model_name} {Style.RESET_ALL}')
        continue
    # 创建完整的文件夹路径
    folder_path = os.path.join(base_path, model_name)

    try:
        # 创建文件夹
        os.makedirs(folder_path, exist_ok=True)
        print(f'Created directory: {folder_path}')
    except OSError as e:
        print(f'Error creating directory {folder_path}: {e}')

# 删除当前目录所有目录，保留文件的命令
# find . -mindepth 1 -maxdepth 1 -type d -exec rm -r {} +
