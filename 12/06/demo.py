class Swan:
    '''天鹅类'''
    _neck_swan = '天鹅的脖子很长'                # 定义私有属性
    def __init__(self):
        print("__init__():", Swan._neck_swan)  # 在实例方法中访问私有属性
swan = Swan()                                     # 创建Swan类的实例
print("直接访问:" , swan._neck_swan)            # 保护属性可以通过实例名访问




















































