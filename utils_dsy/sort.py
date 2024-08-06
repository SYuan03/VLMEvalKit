from collections import defaultdict

# Transformers versions mapping
transformers_map = {
    'Qwen series': '4.33.0',
    'Monkey series': '4.33.0',
    'InternLM-XComposer Series': '4.33.0',
    'mPLUG-Owl2': '4.33.0',
    'OpenFlamingo v2': '4.33.0',
    'IDEFICS series': '4.33.0',
    'VisualGLM': '4.33.0',
    'MMAlaya': '4.33.0',
    'ShareCaptioner': '4.33.0',
    'MiniGPT-4 series': '4.33.0',
    'InstructBLIP series': '4.33.0',
    'PandaGPT': '4.33.0',
    'VXVERSE': '4.33.0',
    'GLM-4v-9B': '4.33.0',
    'LLaVA series': '4.37.0',
    'ShareGPT4V series': '4.37.0',
    'TransCore-M': '4.37.0',
    'LLaVA (XTuner)': '4.37.0',
    'CogVLM Series': '4.37.0',
    'EMU2 Series': '4.37.0',
    'Yi-VL Series': '4.37.0',
    'MiniCPM-[V1/V2]': '4.37.0',
    'OmniLMM-12B': '4.37.0',
    'DeepSeek-VL series': '4.37.0',
    'InternVL series': '4.37.0',
    'Cambrian Series': '4.37.0',
    'VILA Series': '4.37.0',
    'IDEFICS2': '4.40.0',
    'Bunny-Llama3': '4.40.0',
    'MiniCPM-Llama3-V2.5': '4.40.0',
    '360VL-70B': '4.40.0',
    'Phi-3-Vision': '4.40.0',
    'WeMM': '4.40.0',
    'LLaVA-Next series': 'latest',
    'PaliGemma-3B': 'latest',
    'Chameleon series': 'latest',
    'Video-LLaVA-7B-HF': 'latest',
    'Ovis series': 'latest'
}

# Group by version and sort within each version
version_groups = defaultdict(list)
for series, version in sorted(transformers_map.items()):
    version_groups[version].append(series)

# Sort each group and reconstruct the dictionary
sorted_transformers_map = {}
for version in sorted(version_groups):
    for series in sorted(version_groups[version]):
        sorted_transformers_map[series] = version

# Display the sorted dictionary
for series, version in sorted_transformers_map.items():
    print(f"'{series}': '{version}',")
