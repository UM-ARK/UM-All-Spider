# 版本:
    V0.3
# 要求環境:
    python3
# 要求模組:(必需安裝)
    BeautifulSoup4-
        >pip3 install Beautifulsoup
    jicson-
        >pip3 install jicson

# ummoodle_basicInfo:
---
## 可用函數:
    get_icon_url():
         通過己知cookie取得用戶頭像網址
    download_icon(<path>,<file name>):
        通過己知cookie下載用戶頭像到指定位置 和 自定圖片名稱
    get_student_email():
        通過己知cookie取得用戶電郵
    get_student_no():
        通過己知cookie取得學生編號
    get_student_name():
        通過己知cookie取得用戶姓名

## 結果輸出:
    get_icon_url():
        返回圖標網址字符串
    download_icon(<path>,<file name>):
        返回圖標指定路徑字符串
    get_student_email():
        返回學生電子郵件字符串
    get_student_no():
        返回學生編號字符串
    get_student_name():
        返回學生姓名：字符串

## 用法:
`import ummoodle_basicInfo`

`basicInfo = ummoodle_basicInfo.basicInfo("279bvbk980000000au9u0sgvs4") #279bvbk980000000au9u0sgvs4 為MoodleSession`
 
 
`icon_url = basicInfo.get_icon_url() #return icon url:strint`

`print(icon_url)`

`file_path = basicInfo.download_icon("img/","icon2") #return icon path:strint`

`print(file_path)`

`student_email = basicInfo.get_student_email() #return student_email:strint`

`print(student_email)`

`student_no = basicInfo.get_student_no() #return student_no:strint`

`print(student_no)`

`student_name = basicInfo.get_student_name() #return student_name:string`

`print(student_name)`



# ummodle_calendar:
---
## 可用函數:
    get_calender():
        通過己知cookie取得用戶日曆資料
        日曆資料包括:ical鏈接,ical資料
    get_calender_by_file(<path>,<file name>):
        通過己知cookie取得用戶日曆資料 並 儲存到指定位置 和 自定文件名稱


## 結果輸出:
    get_calender():
        返回日曆資料字典
        key:icalLink,icaljson

    get_calender_by_file(<path>,<file name>):
        返回文件指定路徑字符串

## 用法:
`import ummodle_calendar
`

`calender = ummodle_calendar.Calendar("279bvbk980000000au9u0sgvs4") #279bvbk980000000au9u0sgvs4 為MoodleSession`
 
 
`student_calender = calender.get_calender() #return calender information:dictionaries`

`print(student_calender["icalLink"])`

`print(student_calender["icaljson"])`
 
 
`student_calender_file_path = calender.get_calender_by_file("calender_output/","student1") #return json file path:strint`

`print(student_calender_file_path)`



# 更改日志:
###    2022/6/20 - 
    封裝成class 
###    2022/7/8 - 
    修改 Calendar 類 用法 和 function回傳的資料 
    增加 basicInfo 類 用於取得用戶基本資料 
	