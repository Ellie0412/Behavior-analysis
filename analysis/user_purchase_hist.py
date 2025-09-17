import pandas as pd
import matplotlib.pyplot as plt
from visualization.plots import save_fig

def plot_purchase_hist(df):
    purchase_counts = df.groupby('CustomerID')['Quantity'].sum()
    summary = purchase_counts.value_counts().sort_index().reset_index(name='user_count')
    summary.columns = ['purchase_count', 'user_count']

    plt.figure(figsize=(12, 6))
    plt.bar(summary['purchase_count'], summary['user_count'], width=1.0, edgecolor='black')
    plt.xlabel('购买数量 (件)')
    plt.ylabel('用户个数')
    plt.title('每个购买数量对应的用户个数')
    save_fig("客户购买数量直方图")