testdata = """登入
註冊
忘記密碼
修改密碼
更改基本資料
肌力測試
肌力訓練
視覺辨識運動測試訓練
檢視測試結果
查看通知
檢視運動計畫
檢視分析資料
更改運動計畫
自動通知
建立預設運動目標
分析資料"""

testdata = testdata.splitlines()

print(testdata)
chapter = '5-3'
diagram = ['Activity','活動']
for index, data in enumerate(testdata, start=1):
    print(
        f"""![](https://raw.githubusercontent.com/111406/UML/main/圖/{chapter}%20{diagram[0]}%20diagram-{data}.png)
**▲圖{chapter}-{index} {data}之{diagram[1]}圖**
""")
