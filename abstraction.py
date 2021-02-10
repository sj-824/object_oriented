'''
抽象化とは？
「対象から小さな特徴をのぞいて、本質的な特徴だけを集めた状態」
'''

# ex)
class Person:
    def __init__(self,height,weight,gender):
        self.height = height
        self.weight = weight
        self.gender = gender
        # self.hair_color = hair_color 髪の色は人間の本質的特徴ではないと考え除外