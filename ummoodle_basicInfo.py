import urllib.request as req
import bs4


class basicInfo:
    def __init__(self, MoodleSession):
        self.MoodleSession = MoodleSession
        self.headers = {
            "cookie": "MoodleSession=" + self.MoodleSession,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
        }
        self.profile_url = "https://ummoodle.um.edu.mo/user/profile.php"
    pass

    ##icon
    def get_icon_url(self):
        #url = self.profile_url
        request = req.Request(self.profile_url, headers=self.headers)
        ###發送請求
        with req.urlopen(request) as response:
            result = response.read().decode("utf-8")
        ###bs4分析頁面
        root_HTML = bs4.BeautifulSoup(result, "html.parser")
        result = root_HTML.select(".d-inline-block.aabtn img")
        return result[0]["src"]

    def download_icon(self,path,filename):
        #url = self.get_icon_url()
        request = req.Request(self.profile_url, headers=self.headers)
        ###發送請求
        with req.urlopen(request) as file:
            file_data = file.read()
        open(path+filename+".jpg", "wb").write(file_data)
        print("DONE : download ummoodle icon")
        return path+filename+".jpg"



    ##text infomantion
    def cardbody_HTML(self):
        #url = self.profile_url
        request = req.Request(self.profile_url, headers=self.headers)
        ###發送請求
        with req.urlopen(request) as response:
            result = response.read().decode("utf-8")
        ###bs4分析頁面
        root_HTML = bs4.BeautifulSoup(result, "html.parser")
        result = root_HTML.select(".card-body")
        return result

    def get_student_email(self):
        root_html = self.cardbody_HTML()[1]
        result = root_html.select(".contentnode dd a")
        return result[0].get_text()

    def get_student_no(self):
        root_html = self.cardbody_HTML()[1]
        result = root_html.select(".contentnode dd a")
        return result[1].get_text()
    def get_student_name(self):

        root_html = self.cardbody_HTML()[1]
        result = root_html.select(".contentnode dd")
        return result[2].get_text()
