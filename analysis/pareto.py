import pandas as pd
import matplotlib.pyplot as plt
from visualization.plots import save_fig

def plot_pareto(df):
    user_amt = df.groupby('CustomerID')['amount'].sum().reset_index(name='total_price')
    total_sales = user_amt['total_price'].sum()
    user_amt['contribution_rate'] = user_amt['total_price'] / total_sales
    user_amt = user_amt.sort_values('contribution_rate', ascending=False)
    user_amt['cum_rate'] = user_amt['contribution_rate'].cumsum()

    plt.figure(figsize=(12, 6))
    plt.bar(range(1, len(user_amt)+1), user_amt['contribution_rate']*100, label='单个用户贡献率 (%)')
    plt.plot(range(1, len(user_amt)+1), user_amt['cum_rate']*100,
             color='red', marker='o', label='累计贡献率 (%)')
    plt.axhline(80, color='gray', ls='--', lw=1)
    plt.title('用户消费金额贡献率')
    plt.xlabel('用户排序（由高到低）'); plt.ylabel('贡献率 (%)')
    plt.legend(); plt.grid(True, ls='--', alpha=.4)
    save_fig("用户贡献率帕累托图")