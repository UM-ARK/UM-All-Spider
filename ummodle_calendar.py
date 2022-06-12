import urllib.request as req
import urllib.parse as pars
import jicson
import json
import bs4
#V0.1

#>>輸入用戶的MoodleSession<<
MoodleSession = ""


sesskey =""
###建立 header 資料
headers = {
    "cookie": "MoodleSession=" + MoodleSession,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}

def get_sesskey(request_headers):
    url = "https://ummoodle.um.edu.mo/calendar/export.php"
    request = req.Request(url, headers=request_headers)
    ###發送請求
    with req.urlopen(request) as response:
        result = response.read().decode("utf-8")
    root_HTML = bs4.BeautifulSoup(result,"html.parser")
    result=root_HTML.select("input[name='sesskey']")
    return result[0]["value"]

def get_icalLink(request_headers,skey):
    ##取得 iCal link
    url = "https://ummoodle.um.edu.mo/calendar/export.php"

    ###建立 Request 資料
    requestData = {
        "sesskey":skey,
        "_qf__core_calendar_export_form":"1",
        "events[exportevents]":"all",
        "period[timeperiod]": "monthnow",
        "generateurl":"Get calendar URL"
    }
    ###對字段進行編碼:utf-8
    post_data = pars.urlencode(requestData).encode("utf-8")

    ###建立一個Request 物件，附加 Header和表單資料
    request=req.Request(url, headers=request_headers, data=post_data)

    ###發送請求
    with req.urlopen(request) as response:
         result = response.read().decode("utf-8")

    ###用 BeautifulSoup 提取 iCal link
    root_HTML = bs4.BeautifulSoup(result,"html.parser")
    iCal_link = root_HTML.select("div.generalbox.calendarurl")[0].string.replace("Calendar URL: ","")
    return iCal_link

def get_ical(request_headers,url):
    ###建立一個Request 物件，附加 Header
    request = req.Request(url, headers=request_headers)
    ###發送請求
    with req.urlopen(request) as response:
        result = response.read().decode("utf-8")
    return result


##主程式
sesskey = get_sesskey(headers)
icalLink=get_icalLink(headers,sesskey)
data=get_ical(headers,icalLink)
ical_json=jicson.fromText(data)
###輸出結果到文件
file = open("ical_output.json", "w")
file.write(json.dumps(ical_json))
file.close()
print("DONE!!!")
