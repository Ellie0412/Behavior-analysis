from preprocessing import load_and_clean
from analysis import compute_rfm, compute_repeat_purchase_rate, compute_repeat_buyer_rate
from visualization import plot_pie, plot_line,plot_pie
from analysis.user_trend import plot_monthly_trend
from analysis.user_scatter import plot_user_scatter
from analysis.user_purchase_hist import plot_purchase_hist
from analysis.pareto import plot_pareto
from analysis.cohort_status import plot_user_status
from analysis.purchase_cycle import plot_cycle_distribution
from analysis.user_lifecycle_dist import plot_lifecycle_dist

# 1. 加载并清洗数据
df = load_and_clean()

# 2. 计算RFM
rfm = compute_rfm(df)

# 3. 用户分层饼图
label_counts = rfm['label'].value_counts()
plot_pie(label_counts)

# 4. 每月回购率
repeat_rate = compute_repeat_purchase_rate(df)
plot_line(repeat_rate, 'order_month', 'repeat_rate', '每月回购率变化趋势')

# 5. 每月复购率
repeat_buyer_rate = compute_repeat_buyer_rate(df)
plot_line(repeat_buyer_rate, 'order_month', 'repeat_purchase_rate', '每月复购率变化趋势')

plot_monthly_trend(df)
plot_user_scatter(df)
plot_purchase_hist(df)
plot_pareto(df)
plot_user_status(df)
plot_cycle_distribution(df)
plot_lifecycle_dist(df)