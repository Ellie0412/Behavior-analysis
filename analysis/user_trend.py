import pandas as pd
import matplotlib.pyplot as plt
from visualization.plots import save_fig

def plot_monthly_trend(df):
    monthly = df.groupby('order_month').agg(
        total_qty=('Quantity', 'sum'),
        total_amt=('amount', 'sum'),
        order_cnt=('InvoiceNo', 'nunique'),
        user_cnt=('CustomerID', 'nunique')
    )

    plt.figure(figsize=(18, 10))
    for i, col in enumerate(['total_qty', 'total_amt', 'order_cnt', 'user_cnt'], 1):
        plt.subplot(2, 2, i)
        monthly[col].plot(marker='o')
        titles = ['每月产品购买数量', '每月消费金额', '每月订单数', '每月消费人数']
        plt.title(titles[i-1])
    plt.tight_layout()
    save_fig("用户整体消费趋势（月度）")