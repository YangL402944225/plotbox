import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 创建子图 2x2 布局
fig = make_subplots(rows=2, cols=2)

# 添加数据到子图
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6], mode='lines', name='男性 - 类别1'), row=1, col=1)
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[6, 5, 4], mode='lines', name='男性 - 类别2'), row=1, col=2)
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 3, 2], mode='lines', name='男性 - 类别3'), row=2, col=1)
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[2, 3, 4], mode='lines', name='男性 - 类别4'), row=2, col=2)

# 更新整体图布局，合并图例
fig.update_layout(
    legend_title="男性分类",
    legend=dict(
        x=0.5,  # 图例位置
        y=0.5,
        xanchor="center",
        yanchor="middle",
        orientation="h",  # 水平显示
        traceorder="normal"
    ),
    title="2x2 子图示例"
)

fig.show()
