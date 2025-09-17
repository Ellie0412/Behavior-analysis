import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from visualization.plots import save_fig

def plot_user_status(df):
    # 透视：用户×月份 是否购买
    pivoted = df.pivot_table(
        index='CustomerID',
        columns='order_month',
        values='order_date',
        aggfunc='count'
    ).fillna(0)
    purchased = pivoted.applymap(lambda x: 1 if x > 0 else 0)

    def active_status(row):
        status = []
        for i, val in enumerate(row):
            if val == 0:
                if len(status) == 0 or status[-1] == 'unreg':
                    status.append('unreg')
                else:
                    status.append('unactive')
            else:
                if len(status) == 0 or status[-1] == 'unreg':
                    status.append('new')
                elif status[-1] == 'unactive':
                    status.append('return')
                else:
                    status.append('active')
        return pd.Series(status, index=row.index)

    states = purchased.apply(active_status, axis=1)
    state_counts = states.replace('unreg', np.nan).apply(pd.Series.value_counts).fillna(0).astype(int)

    plt.figure(figsize=(15, 6))
    for state, color in zip(state_counts.index, ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']):
        plt.plot(state_counts.columns.astype(str), state_counts.loc[state],
                 marker='o', label=state, color=color)
    plt.title('每月用户状态趋势曲线')
    plt.xlabel('月份'); plt.ylabel('用户数')
    plt.legend(); plt.grid(alpha=.4)
    save_fig("用户状态曲线图")

    # 回流/积极占比
    ratio_df = state_counts.T
    ratio_df['returning_ratio'] = ratio_df['return'] / ratio_df.sum(axis=1)
    ratio_df['active_ratio']    = ratio_df['active'] / ratio_df.sum(axis=1)

    plt.figure(figsize=(15, 5))
    plt.plot(ratio_df.index.astype(str), ratio_df['returning_ratio'],
             marker='o', label='回流用户占比')
    plt.plot(ratio_df.index.astype(str), ratio_df['active_ratio'],
             marker='o', label='积极用户占比')
    plt.ylim(0, 1); plt.grid(alpha=.4)
    plt.title('每月回流/积极用户占比')
    plt.xlabel('月份'); plt.ylabel('占比'); plt.legend()
    save_fig("回流积极用户占比折线图")