# ライブラリの分類


# 関数
# 関数名と引数名で宣言し何かしらの処理をさせる仕組み
'''
関数名(引数, ..., 引数名 = 値, ...)
 位置引数      : 引数の値のみを宣言する
 キーワード引数 : 引数の名前と値を対応させて宣言する
                 (引数が多い関数や自作関数だとどの値がどの引数に対応しているのかが分かりやすい)
'''

# exp. print関数
print("Hello", "World!!", sep=",")  # "Hello"と"World!!""は位置引数, ","はキーワード引数


# 型 : 値の種類を決めるための仕組み
'''
型名 = 値
'''

# インスタンス : 型に基づいた値 オブジェクトとも言う

# exp. str(文字列)型
msg = 'こんにちは'  # str型に'こんにちは'という値を与えてインスタンス化しmsgという名前をつけた

# コンストラクタ : インスタンスを生成するための仕組み
# exp. datatime.date型のコンストラクタ
import datetime
today = datetime.date(2024, 10, 31)


# メソッド : 型(クラス)がもつ関数
'''
インスタンス.メソッド(引数, ...)
'''

# exp1. str型のsortメソッド
data = [25, 3, 49, 67, 14]
data.sort(reverse=True)
print(data)
# 関数の場合はインスタンスを引数に指定する(sorted関数)
print(sorted(data, reverse=True))


# 属性(アトリビュート) : 型(クラス)がもつ変数
'''
インスタンス.属性
'''

# exp. datetime.date型のyear属性
today = datetime.date(2024, 10, 31)
print(today.year)


# クラスメソッド : インスタンスを生成せずに呼び出せるメソッド
'''
型名.メソッド名(引数, ...)
型名.変数
'''

# exp. datetime.date型のtodayメソッド
current = datetime.date.today()
print(current)

# インスタンスメソッド : インスタンスを生成して呼び出すメソッド


# モジュール(ライブラリ)のインポート
'''
import モジュール名
モジュール名.関数()
'''

# exp. mathモジュール
import math
print(math.floor(1.34))