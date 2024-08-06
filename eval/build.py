from vlmeval.config import supported_VLM
import os

base_path = '/cpfs01/user/dingshengyuan/myfork/VLMEvalKit/eval'

# 创建文件夹
for model_name in supported_VLM.keys():
    # 创建完整的文件夹路径
    folder_path = os.path.join(base_path, model_name)
    
    try:
        # 创建文件夹
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created directory: {folder_path}")
    except OSError as e:
        print(f"Error creating directory {folder_path}: {e}")
