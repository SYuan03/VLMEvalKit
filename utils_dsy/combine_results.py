import pandas as pd
import os

model_folders = [
    'sharegpt4v_7b',
    'Yi_VL_34B',
    'OmniLMM_12B',
    'cogvlm2-llama3-chat-19B',
    'idefics_9b_instruct',
    'XComposer',
    'llava_v1.5_7b',
    'llava_v1.5_13b',
    'mPLUG-Owl2',
    'InternVL2-8B',
    'GPT4o_MINI'
]
datasets = ['ChartQA_TEST', 'OCRVQA_TESTCORE', 'TextVQA_VAL']
# datasets = ['ChartQA_TEST']



for dataset in datasets:
    combined_df = pd.DataFrame()

    for model in model_folders:
        root_path = f'/cpfs01/shared/llmeval/dhd/mmeval/'
        csv_path = root_path + f'{model}/{model}_{dataset}_acc.csv'

        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            df['Model'] = model
            # 将 Model 列移动到最前面
            cols = ['Model'] + [col for col in df.columns if col != 'Model']
            df = df[cols]
            combined_df = pd.concat([combined_df, df], ignore_index=True)

    combined_df.to_csv(f'old_{dataset}_combined.csv', index=False)
