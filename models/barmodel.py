from models.plotmodel import PlotModel

class BarModel(object):
    def __init__(self,
                width=2,
                color:str or tuple[str]=PlotModel().colors,
                text_size=10,
                opacity=0.9,
                textposition='outside',
                ):
        self.width = width
        self.colors = ((color,) if isinstance(color,str) else color)
        self.text_size = text_size
        self.opacity = opacity
        self.textposition = textposition # 标签位置: 'inside', 'outside', 'auto', 'inside top', 'inside bottom', 'outside top', 'outside bottom'
        self.index = 0

    def get_color(self):
        """颜色的迭代器"""
        color = self.colors[self.index]
        self.index = (self.index + 1) % len(self.colors)
        return color