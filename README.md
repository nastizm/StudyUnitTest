超初心者向けテストコード勉強会資料
======================


環境構築
------
1. 仮想環境を作る(再利用でもかまいません)  
	pybrew venv create unittest  

2. cloneする  
	git clone git@github.com:nastizm/StudyUnitTest.git

3. cloneした教材のルートパスへ  
	cd path/to/StudyUnitTest

4. テストモジュールをインストール  
	pip install -r pyfile

以下のコマンドを打って、下の画面になればOK!!  
	python test/chapter1/test_gacha.py

	F  
	======================================================================  
	FAIL: testLot (__main__.GachaTest)  
	----------------------------------------------------------------------  
	Traceback (most recent call last):  
	  File "test/chapter1/test_gacha.py", line 17, in testLot  
	    self.fail(u"強制的に失敗")  
	AssertionError: \u5f37\u5236\u7684\u306b\u5931\u6557  
	  
	----------------------------------------------------------------------  
	Ran 1 test in 0.001s  
  


チャプター1
------
# テストコードを書いてみよう  

出来たら以下のコマンドで実行する  
	python test/chapter1/test_gacha.py


■チャプター2
------
# テストパターンを作ろう  

出来たら以下のコマンドで実行する  
	python test/chapter2/test_shop.py

