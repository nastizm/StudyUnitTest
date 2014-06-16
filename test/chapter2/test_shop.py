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
        """
        pass


if __name__ == "__main__":
    unittest.main()