import matplotlib.pyplot as plt
import seaborn as sns
import os
from config import FONT, SAVE_DIR

def save_fig(name):
    """保存图像"""
    path = os.path.join(SAVE_DIR, f"{name}.png")
    plt.savefig(path, dpi=300)
    plt.show()


def plot_pie(label_counts, title="用户分层占比（饼图）"):
    """
    画 RFM 用户分层饼图
    label_counts: pd.Series,索引为标签名,值为计数
    """
    percentages = label_counts / label_counts.sum() * 100

    fig, ax = plt.subplots(figsize=(8, 8))
    wedges = ax.pie(
        label_counts,
        labels=None,               # 内部不显示文字
        autopct=None,              # 内部不显示百分比
        pctdistance=0.8,
        labeldistance=1.15,
        colors=sns.color_palette('Set2', len(label_counts)),
        startangle=90,
        counterclock=False
    )[0]
    
    legend_labels = [f"{label} ({pct:.1f}%)"for label, pct in zip(label_counts.index, percentages)]
    ax.legend(wedges, legend_labels,
              title="用户分层",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1),
              prop=FONT)        # 保证图例中文正常

    ax.set_title(title, fontproperties=FONT, fontsize=12)
    plt.tight_layout()
    save_fig(title)

def plot_line(df, x, y, title, xlabel=None, ylabel=None):
    """画折线图"""
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=x, y=y, data=df, marker='o')
    plt.title(title, fontproperties=FONT)
    plt.xlabel(xlabel or x, fontproperties=FONT)
    plt.ylabel(ylabel or y, fontproperties=FONT)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    save_fig(title)