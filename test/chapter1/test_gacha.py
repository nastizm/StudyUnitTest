# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../src')

import unittest
from chapter1.gacha import Gacha


class GachaTest(unittest.TestCase):
    """
    Gachaクラスのlotが動く事を確認するテストを書いてみよう！
    # 代表的なチェック関数
    value: テストする値が入っている変数
    expects: なるべき期待値
    self.assertTrue(value) # valueがTrueだったら成功
    self.assertFalse(value) # valueがFalseだったら成功
    self.assertEquals(value, expects) # valueとexpectsが正しければ成功
    
    # 以下サンプルです
    testdata = [1,2] # テストデータ
    gacha = Gacha(testdata) # テスト対象のクラスをインスタンス化
    self.assertTrue(gacha.lot() in testdata) # テスト対象メソッドがテストデータの中から選ばれていることを確認する
    
    他に、テストする内容を自分で考えてassertしてみよう！
    for example:
      テストデータが全部数値なら数値型であること
      テストデータが文字列なら文字列であること
      異常なデータ（配列じゃない）を渡した時、エラーになること
    """
    
    def testLot(self):
        """
        ちゃんと動いているか他の例を試してみよう
        """
        self.fail(u"強制的に失敗") # 実際にコード書くときに消してください
        

if __name__ == "__main__":
    unittest.main()

