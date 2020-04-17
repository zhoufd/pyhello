class TVshow:   # 定义电视节目类
    def __init__(self,show):
        self.__show = show
    @property                          # 将方法转换为属性
    def show(self):                    # 定义show()方法
        return self.__show             # 返回私有属性的值
tvshow = TVshow("正在播放《战狼2》")   # 创建类的实例
print("默认：",tvshow.show)            # 获取属性值























































