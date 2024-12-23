
class PlotModel(object):
    """配置图像的样式"""
    def __init__(self,
                 size:tuple=(950, 534),
                 grid:tuple=(1,1),
                 specs=None,
                 colors:str or tuple[str]=('#51689b', '#ce5c5c', '#fbc357', '#8fbf8f', '#659d84', '#fb8e6a', '#c77288', '#786090', '#91c4c5', '#6890ba'),
                 vertical_spacing:float=0.1,
                 horizontal_spacing:float=0.08,
                 subplot_titles=None,
                 shared_xaxes=True,
                 shared_yaxes=True,
                 row_order=None,
                 print_grid=False,
                 family='Kaiti',
                 showlegend=True,
                 text_size:tuple[int]=(10,12,14,16),
                 shape_width:float=1.5,
                 fill:str='toself',
                 fit_line=None,
                 log_x=False,
                 log_y=False,
                 ticks_width=1,
                 ticks_colosr:str='black',
                 text_color1:str='black',
                 tickangle:int=-25,
                 bar_mode=None,
                 textposition='outside',
                 textinfo='percent',
                 is_x_zero=False
                 ):
        """
        初始化图像样式配置，用于定义 Plotly 图表的样式和布局。
        """
        # 参数赋值
        self.size = size
        self.rows = grid[0]
        self.cols = grid[1]
        self.specs =[[{'secondary_y':True}] * self.cols] * self.rows if specs is None else specs
        self.colors = colors
        self.vertical_spacing = vertical_spacing
        self.horizontal_spacing = horizontal_spacing
        self.subplot_titles = subplot_titles
        self.shared_xaxes = shared_xaxes
        self.shared_yaxes = shared_yaxes
        self.row_order = row_order
        self.print_grid = print_grid

        self.family = family
        self.showlegend = showlegend
        self.text_color1 = text_color1
        self.text_size = text_size
        self.textinfo = textinfo
        self.shape_width = shape_width
        self.fill = fill
        self.fit_line = fit_line
        self.log_x = log_x
        self.log_y = log_y
        self.ticks_width = ticks_width
        self.ticks_colosr = ticks_colosr
        self.tickangle = tickangle
        self.textposition = textposition
        self.is_x_zero = is_x_zero
        self.bar_mode = bar_mode

        self.x_text = None
        self.legend_offset_x = None  # 图例是否偏移
        self.index = 0
        self.legend = list()
        self.axes_list = list()

    def get_position(self,position):
        """通过制定图像的位置代码，返回  row, col"""
        row = (position - 1) // self.cols + 1
        col = (position - 1) % self.cols + 1
        return row, col

    def updata_legend_offset_x(self):
        """调用副轴时，偏移图例位置，避免与图例重合"""
        self.legend_offset_x = 1.05


    def set_x_text(self,x_text):
        """传入X坐标轴标签"""
        self.x_text = x_text