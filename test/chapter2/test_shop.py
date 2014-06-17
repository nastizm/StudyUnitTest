import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../src')
import unittest

from chapter2.shop import Item, Shop


class ShopTest(unittest.TestCase):
    """
    ショップのテスト
    """

    def test_price(self):
        """
        値段のテスト
        
        shop.pyのmainメソッドを参考にして
        Shopクラスのpriceメソッドのテストを作ってから実装しましょう！
        
        終わってしまったら20個以上買ったら2割引になる仕様変更が来た場合を考えてみよう！
        ※このときも先にテストを書いてから、実装コードを書く事！
        """
        pass


if __name__ == "__main__":
    unittest.main()

