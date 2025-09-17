import pandas as pd

def compute_lifespan(df):
    """计算用户生命周期"""
    user_life = df.groupby('CustomerID')['order_date'].agg(
        first_buy='min',
        last_buy='max'
    ).reset_index()
    user_life['lifespan_days'] = (user_life['last_buy'] - user_life['first_buy']).dt.days
    return user_life