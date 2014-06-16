# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../src')

import unittest
from chapter1.gacha import Gacha


class GachaTest(unittest.TestCase):

    def testLot(self):
        """
        Gachaクラスのlotが動く事を確認するテストを書いてみよう！
        
        # 代表的なチェック関数
        attr: テストする値が入っている変数
        expects: なるべき期待値
        self.assertTrue(attr) # attrがTrueだったら成功
        self.assertFalse(attr) # attrがFalseだったら成功
        self.assertEquals(attr, expects) # attrとexpectsが正しければ成功
        """
        self.fail(u"強制的に失敗")
#         testdata = [1,2]
#         gacha = Gacha(testdata)
#         self.assertTrue(gacha.lot() in testdata)
        
        # ちゃんと動いているか他の例を試してみよう
        pass


if __name__ == "__main__":
    unittest.main()

