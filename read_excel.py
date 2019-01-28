import xlrd

# Excelファイルパス
FILE_PATH = "decision_table.xlsx"
# Excelシート名
SHEET_NAME = "デシジョンテーブル"

# デシジョンテーブル開始列数
TABLE_START_INDEX = 1
# デシジョンテーブル内での条件/結果開始行数
CONDITION_COL_INDEX = 3
# デシジョンテーブル内でのテスト項目開始列数
TEST_COL_INDEX = 5


def main():
    # Excelを読込み、シートを取得
    book = xlrd.open_workbook(filename=FILE_PATH)
    sheet = book.sheet_by_name(SHEET_NAME)

    # テスト項目が存在する行のみ取得
    rows = [sheet.row_values(y) for y in range(sheet.nrows)]
    rows = [x[TABLE_START_INDEX:] for x in rows
            if x[TEST_COL_INDEX + TABLE_START_INDEX] in ["Y", "N", "-"]]

    # 条件～次の条件の1つ前の行でテーブルを区切る
    tests = []
    start_index = 0
    for i in range(len(rows)):
        if rows[i][0] != "条件" or start_index == i:
            continue
        tests.append(rows[start_index:i])
        start_index = i
    tests.append(rows[start_index:])

    # 標準出力にテスト手順を出力
    for test in tests:
        print_test_procedure(test)


def print_test_procedure(rows):
    """標準出力にテスト手順を出力"""
    # セル結合により空文字となっている条件を補間する
    for y in range(0, len(rows)):
        for x in range(2, TEST_COL_INDEX):
            if not rows[y][x] and y != 0 and rows[y - 1]:
                rows[y][x] = rows[y - 1][x]

    # テスト項目毎に
    for test_no in range(TEST_COL_INDEX, len(rows[0])):
        if not rows[0][test_no]:
            break
        print("----------------------------------------")
        # デシジョンテーブルの行毎にテスト手順を標準出力する
        for row in rows:
            # 条件/結果
            if row[0]:
                print(f"{row[0]}：")
            # テスト対象
            if row[1]:
                print(f"　[{row[1]}]")
            # テスト内容
            if row[test_no] == "-":
                continue
            print(f"　　{row[test_no]}: {row[2]}", end="")
            for cond_index in range(3, TEST_COL_INDEX):
                if row[cond_index]:
                    print(f": {row[cond_index]}", end="")
            print()


if __name__ == "__main__":
    main()
