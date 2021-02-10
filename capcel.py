# カプセル化について

'''
カプセル化とは？
データをクラス内に隠蔽し、外から見えないようにすること
'''

# ex)

class Data:
    def __init__(self):
        self.data = [1,2,3,4,5]
    
    def data_changed(self,index,n):
        self.data[index] = n

# 上記class内のdata変数を上書きする方法は、下記の2種類
# 1 : 直接インスタンス変数を変更する
data_one = Data()
data_one.data[0] = 100
print(data_one.data)

# 2 : data_changedを用いる
data_two = Data()
data_two.data_changed(0,100)
print(data_two.data)

'''
カプセル化は、上記1の方法をさせないこと？
上記1の方法で書き換えさせない変数をプライベート変数と呼ぶ
pythonには、プライベート変数はなく (全てパブリック変数) 以下のような名前づけをすることでプライベートと明示する
self.public = 'safe' # パブリック変数
self._private = 'unsafe' # プライベート変数
'''
