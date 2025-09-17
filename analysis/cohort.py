import pandas as pd
from datetime import timedelta

def compute_repeat_purchase_rate(df):
    """计算每月回购率"""
    unique_months = df['order_month'].sort_values().unique()
    monthly_repeat_rate = []

    for month in unique_months[:-1]:
        current_users = df[df['order_month'] == month]['CustomerID'].unique()
        next_users = df[df['order_month'] == month + pd.DateOffset(months=1)]['CustomerID'].unique()
        repeat_buyers = len(set(current_users) & set(next_users))
        total_buyers = len(current_users)
        rate = (repeat_buyers / total_buyers * 100) if total_buyers > 0 else 0
        monthly_repeat_rate.append((month, rate))

    return pd.DataFrame(monthly_repeat_rate, columns=['order_month', 'repeat_rate'])

def compute_repeat_buyer_rate(df):
    """计算每月复购率"""
    user_month_counts = df.groupby(['CustomerID', 'order_month'])['order_date'].nunique().reset_index(name='count')
    repeat_buyers = user_month_counts[user_month_counts['count'] > 1]
    monthly_repeat_buyer_rate = (
        repeat_buyers.groupby('order_month')['CustomerID'].nunique() /
        user_month_counts.groupby('order_month')['CustomerID'].nunique() * 100
    ).reset_index(name='repeat_purchase_rate')
    return monthly_repeat_buyer_rate