import os
import time
from datetime import datetime

def get_latest_mod_time(directory):
    latest_mod_time = None

    for root, dirs, files in os.walk(directory):
        for fname in files:
            path = os.path.join(root, fname)
            file_mod_time = os.path.getmtime(path)
            if latest_mod_time is None or file_mod_time > latest_mod_time:
                latest_mod_time = file_mod_time

    return latest_mod_time if latest_mod_time is not None else 0

def main(base_dir):
    directories = [(d, os.path.join(base_dir, d)) for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    dir_mod_times = [(d, get_latest_mod_time(path)) for d, path in directories]

    sorted_dirs = sorted(dir_mod_times, key=lambda x: x[1], reverse=True)

    max_dir_length = max(len(d) for d, _ in sorted_dirs)  # 获取最长的目录名称长度，用于对齐

    for d, mod_time in sorted_dirs:
        if mod_time:
            mod_time_str = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')
        else:
            mod_time_str = 'No files found'

        print(f'{d.ljust(max_dir_length + 4)}: {mod_time_str}')

if __name__ == '__main__':
    base_dir = '/cpfs01/user/dingshengyuan/myfork/VLMEvalKit/eval'  # 将此处改为你的目录
    main(base_dir)
