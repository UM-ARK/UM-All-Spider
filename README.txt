版本:
    V0.1
要求環境:
    python3
要求模組:(必需安裝)
    BeautifulSoup4-
        >pip3 install Beautifulsoup
    jicson-
        >pip3 install jicson

使用:
    1)在MoodleSession變量中 輸入用戶的 MoodleSession
        如: MoodleSession = "7gv6scaqg7q7tndd5i7295456s"
    2)運行程序

結果輸出:
    輸出名為ical_output的json文件

可用函數:
    get_sesskey:
         通過己知cookie取得sesskey
    get_icalLink:
        通過己知cookie和sesskey取得iCalendar鏈接
    get_ical:
        通過己知iCalendar鏈接取得日曆數據
