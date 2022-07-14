import ummodle_calendar

calender = ummodle_calendar.Calendar("279bvbk98jroccctau9u0sgvs4")

student_calender = calender.get_calender() #return calender information:dictionaries
print(student_calender["icalLink"])
print(student_calender["icaljson"])

student_calender_file_path = calender.get_calender_by_file("calender_output/","student1")#return json file path:strint
print(student_calender_file_path)

import ummoodle_basicInfo

basicInfo = ummoodle_basicInfo.basicInfo("279bvbk98jroccctau9u0sgvs4")

#icon_url = basicInfo.get_icon_url() #return icon url:strint
#print(icon_url)

file_path = basicInfo.download_icon("img/","icon2") #return icon path:strint
print(file_path)

student_email = basicInfo.get_student_email() #return student_email:strint
print(student_email)

student_no = basicInfo.get_student_no() #return student_no:strint
print(student_no)

student_name = basicInfo.get_student_name() #return student_name:string
print(student_name)