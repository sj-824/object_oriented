'''
ポリモーフィズムとは？
「同じインターフェイスでありながら、データ型に合わせて異なる動作をする機能」
インターフェイスは、メソッドのこと
もっと端的に言うと、異なるクラス間の似たインターフェースの名前を同じにしただけ
'''

# ex)

class Hero():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return '私は' + self.name + 'です'

class Enemy():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return '私は' + self.name + 'です'

def introduction(obj):
    print(obj.speak())

object = [Hero('ワンパンマン'),Enemy('魔王')]

for obj in object:
    introduction(obj)

'''
上記の例だと、インタフェースはspeak()
データ型に合わせて異なる動作を可能としているのがintroductionになる

メリット
仮に、Enemyのspeakメソッドが異なる場合、introduction関数はobjectがHero派生なのか、Enemy派生なのかif文などで判断する必要があり、コードが長くなる
'''