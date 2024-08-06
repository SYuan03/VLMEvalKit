import pandas as pd
import matplotlib.pyplot as plt

# 加载数据
old_data = pd.read_csv('old_TextVQA_VAL_combined.csv')
new_data = pd.read_csv('TextVQA_VAL_combined.csv')

# 合并数据集以便比较
data = pd.merge(old_data, new_data, on='Model', suffixes=('_old', '_new'))

# 创建散点图
plt.figure(figsize=(10, 8))
plt.scatter(data['Overall_old'], data['Overall_new'], color='blue', alpha=0.5)

# 添加参考线
plt.plot([0, 100], [0, 100], 'k--')  # 假设准确率范围是0到100

# 添加标签和标题
plt.xlabel('Old Overall Accuracy')
plt.ylabel('New Overall Accuracy')
plt.title('Comparison of Model Accuracies: Old vs. New Dataset')
plt.grid(True)

# 标注点
for i, txt in enumerate(data['Model']):
    plt.annotate(txt, (data['Overall_old'][i], data['Overall_new'][i]))

# 显示图形
plt.show()
