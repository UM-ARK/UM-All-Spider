# UM ALL - Sprider - Public
版本:  
    V0.2  
要求環境:  
    python3  
要求模組:(必需安裝)  
    BeautifulSoup4-  
        >pip3 install Beautifulsoup  
    jicson-  
        >pip3 install jicson  
  
結果輸出:  
    輸出名為ical_output的json文件  

可用函數:  
    get_sesskey:  
         通過己知cookie取得sesskey  
    get_icalLink:  
        通過己知cookie和sesskey取得iCalendar鏈接  
    get_ical:  
        通過己知iCalendar鏈接取得日曆數據  
  
用法:  
    `  
    import ummodle_calendar  
    calender = ummodle_calendar.Calendar([input MoodleSession])  
    calender.get_calender()  
    `  
  
更改日志:  
    2022/6/20 - 封裝成class  
