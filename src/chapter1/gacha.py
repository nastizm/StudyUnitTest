# -*- coding: utf-8 -*-
import random

class Gacha(object):
    deck = []

    def __init__(self, params):
        """
        デッキデータで初期化する
        """
        self.deck = params

    def lot(self):
        """
        ガチャを引く
        """
        return random.choice(self.deck)

def main():
    """
    仕様：1から5の整数の中から一つの値を取り出す
    """
    gacha = Gacha([1,2,3,4,5])
    print gacha.lot()

if __name__ == "main":
    main()
