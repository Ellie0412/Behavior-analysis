import os
from matplotlib.font_manager import FontProperties

# 字体配置
FONT_PATH = '/Users/ellie/arial-unicode-ms.ttf'
FONT = FontProperties(fname=FONT_PATH)

# 数据路径
DATA_PATH = '/Users/ellie/Documents/Assets/csv/data.csv'

# 保存图像路径
SAVE_DIR = '/Users/ellie/Documents/Assets/photo/user_analysis'
os.makedirs(SAVE_DIR, exist_ok=True)