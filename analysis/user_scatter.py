import seaborn as sns
import matplotlib.pyplot as plt
from visualization.plots import save_fig

def plot_user_scatter(df):
    user_stats = df.groupby('CustomerID').agg(
        total_amount=('amount', 'sum'),
        total_quantity=('Quantity', 'sum'),
        order_count=('InvoiceNo', 'nunique')
    ).reset_index()

    plt.figure(figsize=(12, 8))
    sns.scatterplot(
        x='order_count', y='total_amount', data=user_stats,
        alpha=0.6, size='total_amount', sizes=(20, 200), legend=False
    )
    plt.title('用户消费金额与消费次数分布', fontsize=16)
    plt.xlabel('消费次数'); plt.ylabel('消费金额')
    plt.grid(True, linestyle='--', alpha=0.6)
    save_fig("用户消费金额与消费次数分布")