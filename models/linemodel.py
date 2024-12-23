from models.plotmodel import PlotModel

class LineModel(object):
    def __init__(self,
                mode = 'lines+markers',
                width=2,
                color:str or tuple[str]=PlotModel().colors,
                line_dash='solid',
                line_shape='spline',
                marker_size=5,
                marker_symbol='circle',
                is_hollow=True,
                text_size=15,
                opacity=0.9
                ):
        self.mode = mode
        self.width = width
        self.colors = ((color,) if isinstance(color,str) else color)
        self.line_dash = line_dash
        self.line_shape = line_shape
        self.marker_size = marker_size
        self.marker_symbol = marker_symbol
        self.is_hollow = is_hollow
        self.text_size = text_size
        self.opacity = opacity
        self.index = 0

    def get_color(self):
        """颜色的迭代器"""
        color = self.colors[self.index]
        self.index = (self.index + 1) % len(self.colors)
        return color

if __name__ == '__main__':
    a = LineModel()
    print(a.get_color())