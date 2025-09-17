import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from visualization.plots import save_fig

def plot_lifecycle_dist(df):
    user_life = df.groupby('CustomerID')['order_date'].agg(
        first_buy='min', last_buy='max').reset_index()
    user_life['lifespan_days'] = (user_life['last_buy'] - user_life['first_buy']).dt.days

    user_freq = df.groupby('CustomerID')['order_date'].nunique()
    pie_data = user_freq.map(lambda x: '一次消费' if x == 1 else '多次消费').value_counts()

    plt.figure(figsize=(6, 6))
    colors = sns.color_palette('pastel')[0:2]
    plt.pie(pie_data.values, labels=pie_data.index,
            autopct='%1.1f%%', colors=colors, startangle=90)
    plt.title('一次性 vs 多次消费用户占比')
    save_fig("一次性_vs_多次消费用户占比饼图")

    # 生命周期分布
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    sns.histplot(user_life['lifespan_days'], bins=30, kde=True,
                 color='orangered', ax=axes[0])
    axes[0].set_title('所有用户生命周期分布（天）')

    multi = user_life[user_life['CustomerID'].isin(user_freq[user_freq > 1].index)]
    sns.histplot(multi['lifespan_days'], bins=30, kde=True,
                 color='teal', ax=axes[1])
    axes[1].set_title('多次消费用户生命周期分布（天）')
    save_fig("用户生命周期分布（天）")