from models.plotmodel import PlotModel

class BarModel(object):
    def __init__(self,
                mode='stack',
                width=2,
                color:str or tuple[str]=PlotModel().colors,
                text_size=15,
                opacity=0.9
                ):
        self.mode = mode
        self.width = width
        self.colors = ((color,) if isinstance(color,str) else color)
        self.text_size = text_size
        self.opacity = opacity
        self.index = 0

    def get_color(self):
        """颜色的迭代器"""
        color = self.colors[self.index]
        self.index = (self.index + 1) % len(self.colors)
        return color