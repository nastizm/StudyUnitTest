# -*- coding: utf-8 -*-
"""
仕様: ショップで100円の回復アイテムを10個以上買うと1割引になる
"""

class Shop(object):
    """
    このクラスはアイテムを登録して、値段を返すメソッドを持つ
    """
    item = None
    
    def __init__(self, item):
        '''
        Constructor
        '''
        self.item = item
    
    def price(self, count):
        """
        @todo: ここを実装してテストしてください
        10個買うときは１割引の値段を返す
        
        注意：テストを先に書く事！
        """
        return 0


class Item(object):
    """
    アイテムクラス
    """
    name = ""
    unit_price = 0
    
    def __init__(self, name, unit_price):
        self.name = name
        self.unit_price = unit_price


def main():
    item = Item(u"回復アイテム", 100)
    shop = Shop(item)
    print shop.price(10)


if __name__ == "__main__":
    main()

