class Rect:
    def __init__(self,width,height):
        self.width = width                # 矩形的宽
        self.height = height              # 矩形的高
    @property                           # 将方法转换为属性
    def area(self):                     # 计算矩形的面积的方法
        return self.width*self.height  # 返回矩形的面积
rect = Rect(800,600)                    # 创建类的实例
print("面积为：",rect.area)            # 输出属性的值






















































