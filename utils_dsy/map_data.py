# 完整模型名称映射
model_name_map = {
    'ShareGPT4V-7B': 'sharegpt4v_7b',
    'Yi-VL-34B': 'Yi_VL_34B',
    'PandaGPT-13B': 'PandaGPT_13B',
    'OpenFlamingo V2': 'flamingov2',
    'VisualGLM-6B': 'VisualGLM_6b',
    'mPLUG-Owl2': 'mPLUG-Owl2',
    'Emu2 Chat': 'emu2_chat',
    'MMAlaya': 'MMAlaya',
    'OmniLMM-12B': 'OmniLMM_12B',
    'Mini Gemini-7B': 'MGM_7B',
    'Bunny-Llama3-8B': 'Bunny-llama3-8B',
    'VXVERSE-13B': 'VXVERSE',
    'PaliGemma-3B Mix 448': 'paligemma-3b-mix-448',
    '360VL-70B': '360VL-70B',
    'Phi-3-Vision': 'Phi-3-Vision',
    'Video-LLaVA-7B': 'Video-LLaVA-7B',
    'Video-LLaVA-7B-HF': 'Video-LLaVA-7B-HF',
    'TransCore-M': 'TransCore_M',
    'LLaVA v1.5 7B': 'llava_v1.5_7b',
    'LLaVA v1.5 13B': 'llava_v1.5_13b',
    'LLaVA v1 7B': 'llava_v1_7b',
    'ShareGPT4V 13B': 'sharegpt4v_13b',
    'LLaVA Next Vicuna 7B': 'llava_next_vicuna_7b',
    'LLaVA Next Vicuna 13B': 'llava_next_vicuna_13b',
    'LLaVA Next Mistral 7B': 'llava_next_mistral_7b',
    'LLaVA Next Yi 34B': 'llava_next_yi_34b',
    'LLaVA Next Llama 3 8B': 'llava_next_llama3',
    'LLaVA Next 72B': 'llava_next_72b',
    'LLaVA Next 110B': 'llava_next_110b',
    'LLaVA Next Qwen 32B': 'llava_next_qwen_32b',
    'LLaVA Next Interleave 7B': 'llava_next_interleave_7b',
    'LLaVA Next Interleave 7B DPO': 'llava_next_interleave_7b_dpo',
    'InternVL Chat V1.1': 'InternVL-Chat-V1-1',
    'InternVL Chat V1.2': 'InternVL-Chat-V1-2',
    'InternVL Chat V1.2 Plus': 'InternVL-Chat-V1-2-Plus',
    'InternVL Chat V1.5': 'InternVL-Chat-V1-5',
    'Mini InternVL Chat 2B V1.5': 'Mini-InternVL-Chat-2B-V1-5',
    'Mini InternVL Chat 4B V1.5': 'Mini-InternVL-Chat-4B-V1-5',
    'InternVL2 1B': 'InternVL2-1B',
    'InternVL2 2B': 'InternVL2-2B',
    'InternVL2 4B': 'InternVL2-4B',
    'InternVL2 8B': 'InternVL2-8B',
    'InternVL2 26B': 'InternVL2-26B',
    'InternVL2 40B': 'InternVL2-40B',
    'InternVL2 76B': 'InternVL2-76B',
    'Yi VL 6B': 'Yi_VL_6B',
    'XComposer': 'XComposer',
    'ShareCaptioner': 'sharecaptioner',
    'XComposer2': 'XComposer2',
    'XComposer2 1.8B': 'XComposer2_1.8b',
    'XComposer2 4KHD': 'XComposer2_4KHD',
    'XComposer2d5': 'XComposer2d5',
    'Mini GPT-4 V2': 'MiniGPT-4-v2',
    'Mini GPT-4 V1 7B': 'MiniGPT-4-v1-7B',
    'Mini GPT-4 V1 13B': 'MiniGPT-4-v1-13B',
    'IDEFICS 9B Instruct': 'idefics_9b_instruct',
    'IDEFICS 80B Instruct': 'idefics_80b_instruct',
    'IDEFICS2 8B': 'idefics2_8b',
    'InstructBLIP 7B': 'instructblip_7b',
    'InstructBLIP 13B': 'instructblip_13b',
    'DeepSeek VL 7B': 'deepseek_vl_7b',
    'DeepSeek VL 1.3B': 'deepseek_vl_1.3b',
    'CogVLM Grounding Generalist': 'cogvlm-grounding-generalist',
    'CogVLM Chat': 'cogvlm-chat',
    'CogVLM2 Llama3 Chat 19B': 'cogvlm2-llama3-chat-19B',
    'GLM 4V 9B': 'glm-4v-9b',
    'WeMM': 'WeMM',
    'Cambrian 8B': 'cambrian_8b',
    'Cambrian 13B': 'cambrian_13b',
    'Cambrian 34B': 'cambrian_34b',
    'Chameleon 7B': 'chameleon_7b',
    'Chameleon 30B': 'chameleon_30b',
    'VILA 1.5 3B': 'VILA1.5-3b',
    'Llama 3 VILA 1.5 8B': 'Llama-3-VILA1.5-8b',
    'VILA 1.5 13B': 'VILA1.5-13b',
    'VILA 1.5 40B': 'VILA1.5-40b',
    'Ovis Llama 3 8B': 'Ovis1.5-Llama3-8B',
    'Ovis Gemma 2 9B': 'Ovis1.5-Gemma2-9B'
}

# Transformers versions mapping
transformers_map = {
    'GLM-4v-9B': '4.33.0',
    'IDEFICS series': '4.33.0',
    'InstructBLIP series': '4.33.0',
    'InternLM-XComposer Series': '4.33.0',
    'MMAlaya': '4.33.0',
    'MiniGPT-4 series': '4.33.0',
    'Monkey series': '4.33.0',
    'OpenFlamingo v2': '4.33.0',
    'PandaGPT': '4.33.0',
    'Qwen series': '4.33.0',
    'ShareCaptioner': '4.33.0',
    'VXVERSE': '4.33.0',
    'VisualGLM': '4.33.0',
    'mPLUG-Owl2': '4.33.0',
    'Cambrian Series': '4.37.0',
    'CogVLM Series': '4.37.0',
    'DeepSeek-VL series': '4.37.0',
    'EMU2 Series': '4.37.0',
    'InternVL series': '4.37.0',
    'LLaVA (XTuner)': '4.37.0',
    'LLaVA series': '4.37.0',
    'MiniCPM-[V1/V2]': '4.37.0',
    'OmniLMM-12B': '4.37.0',
    'ShareGPT4V series': '4.37.0',
    'TransCore-M': '4.37.0',
    'VILA Series': '4.37.0',
    'Yi-VL Series': '4.37.0',
    '360VL-70B': '4.40.0',
    'Bunny-Llama3': '4.40.0',
    'IDEFICS2': '4.40.0',
    'MiniCPM-Llama3-V2.5': '4.40.0',
    'Phi-3-Vision': '4.40.0',
    'WeMM': '4.40.0',
    'Chameleon series': 'latest',
    'LLaVA-Next series': 'latest',
    'Ovis series': 'latest',
    'PaliGemma-3B': 'latest',
    'Video-LLaVA-7B-HF': 'latest',
}