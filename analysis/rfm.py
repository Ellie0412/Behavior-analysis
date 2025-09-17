from datetime import timedelta

def compute_rfm(df):
    """计算RFM模型并打标签"""
    today = df['order_date'].max() + timedelta(days=1)
    rfm = df.groupby('CustomerID').agg(
        recency=('order_date', lambda x: (today - x.max()).days),
        frequency=('Quantity', 'sum'),
        monetary=('amount', 'sum')
    ).round({'recency': 1})

    label_map = {
        '111': '重要价值客户', '011': '重要保持客户',
        '101': '重要发展客户', '001': '重要挽留客户',
        '110': '一般价值客户', '010': '一般保持客户',
        '100': '一般发展客户', '000': '一般挽留客户',
    }

    rfm_centered = rfm - rfm.mean()
    rfm['label'] = (
        (rfm_centered >= 0).astype(int)
        .astype(str)
        .agg(''.join, axis=1)
        .map(label_map)
    )
    return rfm