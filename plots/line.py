from models import LineModel
import plotly.graph_objects as go


class Line(object):

    def __init__(self,fig):
        self.fig = fig


    def add_line(self,
                 x:list,
                 y:list,
                 yaxis:str='left',
                 text_val:list=None,
                 group_name=None,
                 line_model='lines+markesrs',
                 showlegend:bool=True,
                 hollow_color='white',
                 marker_size=None,
                 marker_symbol=None,
                 color=None,
                 shape=None,
                 width=None,
                 dash=None,
                 text_size=None,
                 opacity=0.9,
                 family=None,
                 row:int=1,
                 col:int=1,
                 ):
        """绘制一条曲线"""
        line_model = LineModel() if line_model is None else line_model
        secondary_y =False if yaxis == 'left' else True  # 标记副轴

        self.fig.add_trace(
            go.Scatter(
                x=x,
                y=y,
                marker=dict(
                    color=hollow_color, #如果设置透明，就显示白色
                    size=marker_size,
                    symbol=marker_symbol,
                    line=dict(width=width,color=color),
                ),
                mode=line_model,
                line=dict(color=color,
                          shape=shape,
                          width=width,
                          dash=dash,
                          ),
                name=group_name,
                legendgroup=group_name,
                text=y if text_val is None else text_val,
                opacity=opacity,
                textposition='top center',
                hoverinfo='text+x+y',
                textfont=dict(
                    size=text_size,
                    family=family,
                    color=color
                ),
                showlegend=showlegend,
            ),
            row=row,
            col=col,
            secondary_y=secondary_y,
        )