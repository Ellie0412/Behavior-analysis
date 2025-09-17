import pandas as pd
from config import DATA_PATH

def load_and_clean():
    """读取并清洗数据"""
    df = pd.read_csv(DATA_PATH, encoding='latin1')
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    df['order_date'] = pd.to_datetime(df['InvoiceDate'], format='mixed', dayfirst=True, errors='coerce')
    df['order_month'] = df['order_date'].values.astype('datetime64[M]')
    df['amount'] = df['Quantity'] * df['UnitPrice']
    return df.reset_index(drop=True)