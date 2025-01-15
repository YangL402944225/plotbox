import plotly.graph_objects as go


class Bar(object):

    def __init__(self,fig):
        self.fig = fig


    def bar(self,
                x:list,
                y:list,
                yaxis:str='left',
                text_val:list=None,
                showlegend:bool=True,
                group_name:str=None,
                textposition='outside',
                orientation='v',
                color=None,
                text_size=None,
                opacity=0.9,
                family=None,
                row:int=1,
                col:int=1,
        ):
        """绘制柱状图"""
        secondary_y =False if yaxis == 'left' else True  # 标记副轴
        self.fig.add_trace(
            go.Bar(
                x=x,
                y=y,
                text=y if text_val is None else text_val,
                opacity=opacity,
                textposition=textposition,
                orientation=orientation,
                textfont=dict(
                    size=text_size,
                    family=family,
                    color=color
                ),
                name=group_name,
                legendgroup=group_name,
                marker=dict(
                    color=color,
                    line=dict(
                        color=color,
                        width=0,
                    ),
                ),
                showlegend=showlegend,
            ),
            row=row,
            col=col,
            secondary_y=secondary_y,
        )