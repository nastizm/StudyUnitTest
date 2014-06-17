超初心者向けテストコード勉強会資料
======================


環境構築
------
* python2系
* virtualenvwrapper もしくは pybrew
  
が導入されている事が前提です。  
仮想環境の作成低順は自分の環境に合わせて作ってください。  


1. 仮想環境を作る(再利用するなら飛ばしてください)  
	mkvirtualenv unittest  
	workon unittest
  
	or 
  
	pybrew venv create unittest  
	pybrew venv use unittest  

2. cloneする  
	git clone https://github.com/nastizm/StudyUnitTest.git

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
  


chapter1
--------
* テストコードを書いてみよう  

	src/chapter1/gacha.py # 実装  
	test/chapter1/test_gacha.py # テスト  

* 出来たら以下のコマンドで実行する 

	python test/chapter1/test_gacha.py  
  
時間が余ったらさらにテストをするメソッドを追加してみよう！    
  

chapter2
--------
* テストパターンを作ろう  

	src/chapter2/shop.py # 実装  
	test/chapter2/test_shop.py # テスト  

* 出来たら以下のコマンドで実行する  
	python test/chapter2/test_shop.py  
