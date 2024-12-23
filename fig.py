from plotly.subplots import make_subplots
from models import PlotModel, LineModel
import pandas as pd
from plots import Line

class Fig(object):
    """
    创建图像对象
    """

    def __init__(self,
                 title:str='',
                 plot_model:PlotModel=None,
                 ):

        self.plot_model = PlotModel() if plot_model is None else plot_model

        # 创建图对象
        self.fig = make_subplots(
            rows= self.plot_model.rows,
            cols= self.plot_model.cols,
            specs= self.plot_model.specs,
            vertical_spacing=self.plot_model.vertical_spacing,
            horizontal_spacing=self.plot_model.horizontal_spacing,
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
                 y_name:str=None,
                 y_range:tuple=None,
                 group_name:str=None,
                 line_model:LineModel=None,
                 position:int=1,
                 ):
        row,col = self.plot_model.get_position(position)
        color = line_model.get_color()
        hollow_color ='white' if line_model.is_hollow else color
        group_name = y if group_name is None else group_name

        showlegend = True if group_name not in self.plot_model.legend else False
        if showlegend:
            self.plot_model.legend.append(group_name)

        Line(fig=self.fig).add_line(
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

        if str(row) + str(col) not in self.plot_model.axes_list:
            self.__set_xaxes__(row=row,col=col)
            self.plot_model.axes_list.append(str(row) + str(col))

        if yaxis+str(row)+str(col) not in self.plot_model.axes_list:
            self.__set_yaxes__(row=row,col=col,yaxis=yaxis,y_name=y_name,y_range=y_range)
            self.plot_model.axes_list.append(yaxis+str(row)+str(col))

        if self.plot_model.rows * self.plot_model.cols == 1 and yaxis == 'right':
            # 如果是1*1的图，切设置了副轴，则图例向右偏移5%，避免遮挡
            self.plot_model.updata_legend_offset_x()

    def __set_xaxes__(self,row:int=1,col:int=1):
        self.fig.update_xaxes(
            title=None,
            showline=not self.plot_model.is_x_zero,
            showticklabels=not self.plot_model.is_x_zero,

            type='category',  # 禁用自动处理X轴格式
            automargin=True,
            titlefont=dict(size=self.plot_model.text_size[0],
                           family=self.plot_model.family,
                           color=self.plot_model.text_color1,
            ),
            tickfont=dict(color=self.plot_model.text_color1,
                          family=self.plot_model.family,
                          size=self.plot_model.text_size[0],
            ),
            tickangle=self.plot_model.tickangle,
            tickvals=list(range(len(self.plot_model.x_text))),
            ticktext=[str(i) for i in self.plot_model.x_text],
            showgrid=True,
            zeroline=self.plot_model.is_x_zero,
            linecolor=self.plot_model.ticks_colosr,
            linewidth=self.plot_model.ticks_width,
            ticks='' if self.plot_model.is_x_zero else 'inside',  # 'inside',
            tickcolor=self.plot_model.ticks_colosr,
            tickwidth=self.plot_model.ticks_width,
            row=row,
            col=col
        )

    def __set_yaxes__(self,yaxis='left',row:int=1,col:int=1,y_name:str=None,y_range:tuple[float]=None):
        secondary_y = False if yaxis == 'left' else True
        self.fig.update_yaxes(
            title=y_name,
            range=y_range,
            titlefont=dict(size=self.plot_model.text_size[0],
                           family=self.plot_model.family,
                           color=self.plot_model.text_color1,
            ),
            tickfont=dict(color=self.plot_model.text_color1,
                          family=self.plot_model.family,
                          size=self.plot_model.text_size[0],
            ),
            showgrid=not secondary_y,
            zeroline=self.plot_model.is_x_zero,
            zerolinewidth=self.plot_model.ticks_width,
            zerolinecolor=self.plot_model.ticks_colosr,
            secondary_y=secondary_y,
            linecolor=self.plot_model.ticks_colosr,
            linewidth=self.plot_model.ticks_width,
            ticks='inside',
            tickcolor=self.plot_model.ticks_colosr,
            tickwidth=self.plot_model.ticks_width,
            row=row,
            col=col
        )


    def show(self,side='left'):
        annotations = []
        if self.plot_model.is_x_zero:
            for i, label in enumerate(self.plot_model.x_text):
                annotations.append(
                    dict(
                        x=i,  # 刻度位置
                        y=0,  # 偏移后的位置
                        text=label,  # 自定义标签
                        showarrow=False,  # 不显示箭头
                        font=dict(size=self.plot_model.text_size[0],
                                  color=self.plot_model.ticks_colosr),
                        side=side,  # 放置在右侧
                        xanchor="right",
                        yanchor="top",  # 标签位置在轴的上方
                        yshift=0,
                        textangle=self.plot_model.tickangle
                    )
                )
        self.fig.update_layout(title = dict(text=self.title,
                                            font=dict(
                                                size=self.plot_model.text_size[3],
                                                family=self.plot_model.family,
                                                #weight='bold',
                                                color=self.plot_model.text_color1
                                                )
                                            ),
                               barmode=None if self.plot_model.is_x_zero else self.plot_model.bar_mode,
                               legend=dict(title=None,
                                           tracegroupgap=0,
                                           itemclick="toggle",
                                           itemdoubleclick="toggleothers",
                                           font=dict(size=self.plot_model.text_size[1],
                                                     family=self.plot_model.family,
                                                     color=self.plot_model.text_color1
                                                     ),
                                           x=self.plot_model.legend_offset_x,
                                           ),
                               width=self.plot_model.size[0],
                               height=self.plot_model.size[1],
            )

        self.fig.show(config={'displaylogo':False})


if __name__ == '__main__':
    df = pd.DataFrame()
    df['时间'] = ['201501', '201502', '201503', '201504', '201505', '201506',
                   '201507','201508', '201509', '201510', '201511', '201512']
    df['数据1'] = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
    df['数据2'] = [3.9, 5.9, 11.1, 18.7, 48.3, 69.2, 231.6, 46.6, 55.4, 18.4, 10.3, 0.7]
    df['数据3'] = [0.01, 0.02, 0.01, 0.02, 0.01, 0.028, 0.035, 0.047, 0.078, 0.064, 0.042, 0.039]

    s = PlotModel(grid=(2,2))
    fig = Fig(plot_model=s,title='表的名称')

    ls1 = LineModel()
    ls2 = LineModel(color='#ce5c5c')
    ls3 = LineModel(color='#fbc357')

    fig.add_line(df,x='时间',y='数据1',yaxis='left',y_name='数据轴',position=1,y_range=(0,500),line_model=ls1)
    fig.add_line(df,x='时间',y='数据2',yaxis='left',y_name='数据轴',position=1,y_range=(0,500),line_model=ls1)
    fig.add_line(df,x='时间',y='数据3',yaxis='right',position=1,y_range=(0,0.1),line_model=ls1)

    fig.add_line(df,x='时间',y='数据1',yaxis='left',y_name='数据轴',position=2,y_range=(0,500),line_model=ls1)
    fig.add_line(df,x='时间',y='数据2',yaxis='left',y_name='数据轴',position=2,y_range=(0,500),line_model=ls2)
    fig.add_line(df,x='时间',y='数据3',yaxis='right',position=2,y_range=(0,0.1),line_model=ls3)

    fig.add_line(df,x='时间',y='数据1',yaxis='left',y_name='数据轴',position=3,y_range=(0,500),line_model=ls1)
    fig.add_line(df,x='时间',y='数据2',yaxis='left',y_name='数据轴',position=3,y_range=(0,500),line_model=ls2)
    fig.add_line(df,x='时间',y='数据3',yaxis='right',position=3,y_range=(0,0.1),line_model=ls3)

    fig.add_line(df,x='时间',y='数据1',yaxis='left',y_name='数据轴',position=4,y_range=(0,500),line_model=ls1)
    fig.add_line(df,x='时间',y='数据2',yaxis='left',y_name='数据轴',position=4,y_range=(0,500),line_model=ls2)
    fig.add_line(df,x='时间',y='数据3',yaxis='right',position=4,y_name='数据轴2',y_range=(0,0.1),line_model=ls3)

    fig.show()