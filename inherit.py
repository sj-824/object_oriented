'''
継承とは？
親の特徴を子が引き継ぐ遺伝的継承と似ている
つまり、クラスを継承することで、継承したクラスのプロパティやメソッドを使用することができる
この時、継承元となるクラスを親クラス、継承先のクラスを子クラスと呼ぶ
'''

# ex)
class Shape:
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

class Triangle(Shape):
    pass

shape = Shape(10,20)
print(shape.area())

triangle = Triangle(10,20)
print(triangle.area())

'''
出力結果
200
200
'''

# 実際には三角形の面積は,底辺×高さ÷2なので
class Triangle2(Shape):
    def area(self):
        return self.height * self.width / 2

triangle2 = Triangle2(10,20)
print(triangle2.area())

'''
出力結果
100.0

上記のように親クラスのメソッドを定義し直すことをオーバーライドと呼ぶ
'''
