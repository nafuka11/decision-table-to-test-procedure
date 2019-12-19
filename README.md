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


## 必要物
Python 3.4以上

## 使用方法
1. ソースコードをclone
   ```bash
   git clone https://github.com/nafuka11/decision-table-to-test-procedure.git
   ```
2. 仮想環境を作成
   ```bash
   cd decision-table-to-test-procedure
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. `read_excel.py` の設定値を編集
4. `read_excel.py` を実行
   ```bash
   python read_excel.py
   ```
   - 標準出力にテスト手順が出力されます。
