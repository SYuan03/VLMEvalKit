from .image_base import ImageBaseDataset
from .utils import build_judge, DEBUG_MESSAGE
from ..smp import *
from ..utils import track_progress_rich

class CVQADataset(ImageBaseDataset):
    TYPE = 'MCQ'

    DATASET_URL = {
        'CVQA_TEST': 'CVQA_TEST.tsv'
    }

    DATASET_MD5 = {
        'CVQA_TEST': None
    }

    def build_prompt(self, line):

        if isinstance(line, int):
            line = self.data.iloc[line]

        print('line', line)

        if self.meta_only:
            tgt_path = toliststr(line['image_path'])
        else:
            tgt_path = self.dump_image(line)

        question = line['question']

        prompt = ''
        prompt += f'Question: {question}\n'

        options_str = line['Options']  # 这是一个选项字符串
        options = options_str.strip("[]").strip("'").replace("\n", "").split("' '")
        options_prompt = 'Options:\n'
        for idx, item in enumerate(options):
            options_prompt += f'{idx}. {item}\n'
            
        if len(options):
            prompt += options_prompt
            prompt += (
                "Please select the correct answer from the options above.\n"
                "Answer with the option's number from the given choices directly.\n"
                "Do not include any extra characters or text.\n"
            )


        msgs = []
        if isinstance(tgt_path, list):
            msgs.extend([dict(type='image', value=p) for p in tgt_path])
        else:
            msgs = [dict(type='image', value=tgt_path)]
        msgs.append(dict(type='text', value=prompt))

        print('prompt', prompt)

        return msgs
    
    @classmethod
    def evaluate(self, eval_file, **judge_kwargs):
        print('CVQA_TEST evaluation')
        print('Got eval_file:', eval_file)

    