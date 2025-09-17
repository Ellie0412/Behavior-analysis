import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from visualization.plots import save_fig

def plot_cycle_distribution(df):
    order_day = (df[['CustomerID', 'order_date']]
                 .drop_duplicates()
                 .sort_values(['CustomerID', 'order_date']))
    order_day['prev_date'] = order_day.groupby('CustomerID')['order_date'].shift(1)
    order_day['cycle_days'] = (order_day['order_date'] - order_day['prev_date']).dt.days
    cycle_df = order_day.dropna(subset=['cycle_days'])

    plt.figure(figsize=(10, 4))
    sns.histplot(cycle_df['cycle_days'], bins=30, kde=True, color='teal')
    plt.title('用户购买周期分布（相邻两次订单间隔）')
    plt.xlabel('间隔天数'); plt.ylabel('频次')
    save_fig("用户购买周期分布（相邻两次订单间隔）")