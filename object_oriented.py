# オブジェクト指向について学ぶ

# Orangeを用いたクラス、オブジェクト、インスタンス化について
class Orange:

    def __init__(self,color,price): # __init(initialize)__は特殊メソッドと呼ばれる
        self.color = color
        self.price = price

# インスタンス化
or1 = Orange(red,100) 
'''
- selfは自動で渡される
- or1をクラスオレンシのインスタンス (オブジェクト)と呼ぶ
- classに引数を与えることでオブジェクトは生成される？
'''
