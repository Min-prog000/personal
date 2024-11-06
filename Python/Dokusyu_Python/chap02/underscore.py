# __name__（モジュール名）
print(__name__)

# __doc__(ドキュメンテーション文字列(docstring))
# docstring：関数やクラスを説明するためのコメント
def test():
    """
    __doc__: This is storing documentaion strings of method test().
    """
    pass
# test()のdocstringを表示
print(test.__doc__)

# __file__（実行ファイルのパス）
print(__file__)

# __builtins__（組み込み関数一覧）
print(__builtins__)