# decision-table-to-test-procedure

## これは何？

Excelのデシジョンテーブルを読込み、  
標準出力にテスト手順を出力するスクリプトです。


## 入出力例
入力：デシジョンテーブル（Excelファイル）  
![デシジョンテーブル](https://user-images.githubusercontent.com/42476527/50581515-b6245700-0e9d-11e9-8c6b-352a97800346.PNG)

↓　↓　↓

出力：テスト手順（標準出力）  
![テスト手順](https://user-images.githubusercontent.com/42476527/50581517-bc1a3800-0e9d-11e9-9b7d-93448d0303e3.png)


## 使用方法
1. read_excel.pyを任意のディレクトリに配置します。
2. 入力用のExcelを作成し、任意のディレクトリに配置します。
3. read_excel.py内の設定値を編集します。
4. read_excel.pyを実行します。
5. 標準出力にテスト手順が出力されます。


## 制限事項
1. Pythonパッケージ
    - `xlrd` が必要になります（Excelファイル読み込みのため）
