# -*- coding: utf-8 -*-
"""
仕様: ショップで100円の回復アイテムを10個以上買うと1割引になる

成果物: 
 Shopクラスのpriceメソッドを実装してテストコードを書く
 Shopクラスは以下の設計になっている
 ・Itemクラスで初期化される
 ・購入数を引数にとるpriceメソッドを持っている
 ・priceメソッドは購入数が10個以上の時に通常より１割引の値段を返す。
"""

class Item(object):
    """
    アイテムクラス
    """
    name = "" # 名前
    unit_price = 0 # 単価
    
    def __init__(self, name, unit_price):
        self.name = name
        self.unit_price = unit_price


class Shop(object):
    """
    このクラスはアイテムを登録して、値段を返すメソッドを持つ
    """
    item = None
    
    def __init__(self, item):
        """
        item: Itemクラスを引数に取る
        """
        self.item = item
    
    def price(self, count):
        """
        @todo: ここを実装してテストしてください
        10個買うときは１割引の値段を返す
        
        注意：テストを先に書く事！
        """
        return 0


def main():
    # 実行例
    item = Item(u"回復アイテム", 100)
    shop = Shop(item)
    print shop.price(10)


if __name__ == "__main__":
    main()

