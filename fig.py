from plotly.subplots import make_subplots
from models import PlotModel, LineModel ,BarModel
import pandas as pd
from plots import Line,Bar

class Fig(object):
    """
    创建图像对象
    """

    def __init__(self,
                 title:str=None,
                 plot_model:PlotModel=PlotModel(),
                 ):
        self.title = title
        self.plot_model = plot_model

        # 创建图对象
        self.fig = make_subplots(
            rows= self.plot_model.rows,
            cols= self.plot_model.cols,
            specs= self.plot_model.specs,
            vertical_spacing=self.plot_model.vs,
            horizontal_spacing=self.plot_model.hs,
            subplot_titles=self.plot_model.subplot_titles,
            shared_xaxes=self.plot_model.shared_xaxes,
            shared_yaxes=self.plot_model.shared_yaxes,
            print_grid=self.plot_model.print_grid,
        )
        self.title = title
        self.fig.update_layout(title=title)

    def add_line(self,
                 data:pd.DataFrame,
                 x:str,
                 y:str,
                 yaxis='left',
                 text_val:tuple=None,
                 x_name:str=None,
                 y_name:str=None,
                 y_range:tuple=None,
                 group_name:str=None,
                 line_model:LineModel=LineModel(),
                 position:int=1,
                 ):
        row,col = self.plot_model.get_position(position)
        color = line_model.get_color()
        hollow_color ='white' if line_model.is_hollow else color
        group_name = y if group_name is None else group_name
        showlegend = True if group_name not in self.plot_model.legend else False
        if showlegend:
            self.plot_model.legend.append(group_name)
        Line(fig=self.fig).line(
                                x=data[x].values.tolist(),
                                y=data[y].values.tolist(),
                                yaxis=yaxis,
                                text_val=text_val,
                                group_name=group_name,
                                line_model=line_model.mode,
                                hollow_color=hollow_color,
                                marker_size=line_model.marker_size,
                                marker_symbol=line_model.marker_symbol,
                                color=color,
                                shape=line_model.line_shape,
                                width=line_model.width,
                                dash=line_model.line_dash,
                                text_size=line_model.text_size,
                                opacity=line_model.opacity,
                                family=self.plot_model.family,
                                showlegend=showlegend,
                                row=row,
                                col=col,
        )
        self.plot_model.set_x_text(data[x].values.tolist())
        self.__set_axes__(row,
                        col,
                        x_name=x if x_name is None else x_name,
                        x_val=data[x].values.tolist(),
                        y_name=y if y_name is None else y_name,
                        y_range=None if y_range is None else y_range,
                        yaxis=yaxis,
        )

    def add_bar(self,
                data:pd.DataFrame,
                x:str,
                y:str,
                yaxis='left',
                text_val:tuple=None,
                x_name:str=None,
                y_name:str=None,
                y_range:tuple=None,
                group_name:str=None,
                bar_model:BarModel=BarModel(),
                position:int=1,
                ):
        """添加柱状图"""
        row, col = self.plot_model.get_position(position)
        color = bar_model.get_color()
        group_name = y if group_name is None else group_name
        showlegend = True if group_name not in self.plot_model.legend else False
        if showlegend:
            self.plot_model.legend.append(group_name)
        Bar(fig=self.fig).bar(
                x=data[x].values.tolist(),
                y=data[y].values.tolist(),
                yaxis=yaxis,
                text_val=text_val,
                group_name=group_name,
                color=color,
                text_size=bar_model.text_size,
                textposition=bar_model.textposition,
                opacity=bar_model.opacity,
                family=self.plot_model.family,
                showlegend=showlegend,
                row=row,
                col=col,
        )
        self.plot_model.set_x_text(data[x].values.tolist())
        self.__set_axes__(row,
                        col,
                        x_name=x if x_name is None else x_name,
                        x_val=data[x].values.tolist(),
                        y_name=y if y_name is None else y_name,
                        y_range=None if y_range is None else y_range,
                        yaxis=yaxis,
        )


    def add_bar_h(self,
                data: pd.DataFrame,
                x: str,
                y: str,
                yaxis='left',
                text_val: tuple = None,
                x_name: str = None,
                y_name: str = None,
                y_range: tuple = None,
                group_name: str = None,
                bar_model: BarModel = BarModel(),
                position: int = 1,
                ):
        row, col = self.plot_model.get_position(position)
        color = bar_model.get_color()
        group_name = y if group_name is None else group_name
        showlegend = True if group_name not in self.plot_model.legend else False
        if showlegend:
            self.plot_model.legend.append(group_name)
        Bar(fig=self.fig).bar(
                x=data[y].values.tolist(),
                y=data[x].values.tolist(),
                yaxis=yaxis,
                text_val=text_val,
                orientation='h',
                group_name=group_name,
                color=color,
                text_size=bar_model.text_size,
                textposition=bar_model.textposition,
                opacity=bar_model.opacity,
                family=self.plot_model.family,
                showlegend=showlegend,
                row=row,
                col=col,
        )
        self.plot_model.set_x_text(data[x].values.tolist())
        self.__set_axes__(
                        row,
                        col,
                        x_name=x if x_name is None else x_name,
                        #x_val=data[y].values.tolist(),
                        y_name=y if y_name is None else y_name,
                        y_range=None if y_range is None else y_range,
                        yaxis=yaxis,
                        orientation='h'
        )


    def __set_axes__(self,row,col,x_name=None,x_val=None,y_name=None,y_range=None,yaxis='left',orientation='v'):
        if orientation == 'v':
            if str(row)+str(col) not in self.plot_model.axes_list:
                x_name = x_name if self.plot_model.shared_xaxes and row == self.plot_model.rows else None
                if not self.plot_model.shared_xaxes and not self.plot_model.is_x_zero:
                    showticklabels = True
                elif self.plot_model.shared_xaxes and row == self.plot_model.rows and not self.plot_model.is_x_zero:
                    showticklabels = True
                else:
                    showticklabels = False
                self.__set_xaxes__(x=x_val,x_name=x_name,row=row,col=col,showticklabels=showticklabels)
                self.plot_model.axes_list.append(str(row) + str(col))

            if str(yaxis)+str(row)+str(col) not in self.plot_model.axes_list:
                if self.plot_model.shared_yaxes and (col != 1 and yaxis == 'left'):
                    y_name = None
                    showticklabels = False
                elif self.plot_model.shared_yaxes and (col != self.plot_model.cols and yaxis == 'right'):
                    y_name = None
                    showticklabels = False
                else:
                    showticklabels = True
                self.__set_yaxes__(row=row,col=col,yaxis=yaxis,y_name=y_name,y_range=y_range,showticklabels=showticklabels)
                self.plot_model.axes_list.append(str(yaxis)+str(row)+str(col))

            if self.plot_model.rows * self.plot_model.cols == 1 and yaxis == 'right':
                # 如果是1*1的图，切设置了副轴，则图例向右偏移5%，避免遮挡
                self.plot_model.updata_legend_offset_x()
        else:
            if str(yaxis) + str(row) + str(col) not in self.plot_model.axes_list:
                y_name = None
                showticklabels = True
                self.__set_yaxes__(row=row, col=col, yaxis=yaxis, y_name=y_name, y_range=None,
                                   showticklabels=showticklabels)
                self.plot_model.axes_list.append(str(yaxis) + str(row) + str(col))

            #showticklabels = True
            #self.__set_xaxes__(x=None,x_name=None,row=row, col=col,x_range=y_range,showticklabels=showticklabels)

    def __set_xaxes__(self,x,x_name,row:int=1,col:int=1,showticklabels:bool=True,x_range=None):
        self.fig.update_xaxes(
            title=x_name,
            range=x_range,
            showline=not self.plot_model.is_x_zero,
            showticklabels=showticklabels,  # 是否显示X轴
            type='category',  # 禁用自动处理X轴格式
            automargin=True,
            titlefont=dict(size=self.plot_model.ticks_title_size,
                           family=self.plot_model.family,
                           color=self.plot_model.text_color,
            ),
            tickfont=dict(color=self.plot_model.text_color,
                          family=self.plot_model.family,
                          size=self.plot_model.x_ticks_size,
            ),
            tickangle=self.plot_model.tickangle,
            tickvals=None if x is None else list(range(len(x))),
            ticktext=x,
            showgrid=True,
            zeroline=self.plot_model.is_x_zero,
            linecolor=self.plot_model.ticks_color,
            linewidth=self.plot_model.ticks_width,
            ticks='' if self.plot_model.is_x_zero else 'inside',  # 'inside',
            tickcolor=self.plot_model.ticks_color,
            tickwidth=self.plot_model.ticks_width,
            row=row,
            col=col
        )

    def __set_yaxes__(self,row:int=1,col:int=1,y_name:str=None,y_range:tuple[float]=None,yaxis:str='left',
                      showticklabels:bool=True):
        secondary_y = False if yaxis == 'left' else True
        self.fig.update_yaxes(
            title=y_name,
            range=y_range,
            showticklabels=showticklabels,
            titlefont=dict(size=self.plot_model.ticks_title_size,
                           family=self.plot_model.family,
                           color=self.plot_model.text_color,
            ),
            tickfont=dict(color=self.plot_model.text_color,
                          family=self.plot_model.family,
                          size=self.plot_model.y_ticks_size,
            ),
            showgrid=not secondary_y,
            zeroline=self.plot_model.is_x_zero,
            zerolinewidth=self.plot_model.ticks_width,
            zerolinecolor=self.plot_model.ticks_color,
            secondary_y=secondary_y,
            linecolor=self.plot_model.ticks_color,
            linewidth=self.plot_model.ticks_width,
            ticks='inside',
            tickcolor=self.plot_model.ticks_color,
            tickwidth=self.plot_model.ticks_width,
            row=row,
            col=col
        )

    def show(self,side='left'):
        annotations = []
        if self.plot_model.is_x_zero:
            for index, label in enumerate(self.plot_model.x_text):
                annotations.append(
                    dict(
                        x=index,  # 刻度位置
                        y=0,  # 偏移后的位置
                        text=label,  # 自定义标签
                        showarrow=False,  # 不显示箭头
                        font=dict(size=self.plot_model.x_ticks_size,
                                  color=self.plot_model.text_color),
                        side=side,  # 放置在右侧
                        xanchor="right",
                        yanchor="top",  # 标签位置在轴的上方
                        yshift=0,
                        textangle=self.plot_model.tickangle
                    )
                )
        self.fig.update_layout(title = dict(text=self.title,
                                            font=dict(
                                                size=self.plot_model.title_size,
                                                family=self.plot_model.family,
                                                color=self.plot_model.text_color,
                                                )
                                            ),
                               barmode=self.plot_model.bar_mode,
                               legend=dict(title=None,
                                           tracegroupgap=0,
                                           itemclick="toggle",
                                           itemdoubleclick="toggleothers",
                                           font=dict(size=self.plot_model.legend_size,
                                                     family=self.plot_model.family,
                                                     color=self.plot_model.text_color,
                                                     ),
                                           x=self.plot_model.legend_offset_x,
                                           ),
                               width=self.plot_model.size[0],
                               height=self.plot_model.size[1],
            )
        self.fig.show(config={'displaylogo':False})

if __name__ == '__main__':
    # 2024年12月27日18:59:06
    df = pd.DataFrame()
    df['分组'] = ['A','B','C','D','E','F','G']
    df['数据1'] = [3.9, 5.9, 11.1, 18.7, 18.4, 10.3, 5.7]
    df['数据2'] = [0.01, 0.02, 0.01, 0.02, 0.042, 0.039,0.02]
    s = PlotModel(grid=(1,1),size=(1300,1300/1.78),hs=0.03,vs=0.06)
    b1 = BarModel(color=['#51689b'])
    fig = Fig(plot_model=s,title='表的名称',)
    for i in range(1,2):
        fig.add_bar_h(data=df,x='分组',y='数据1',position=i,bar_model=b1)
        fig.add_line(data=df, x='数据2',y='分组',position=i)
    fig.show()