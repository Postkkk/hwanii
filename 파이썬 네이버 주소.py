##순천향대학교라고 입력 받아 순천향대학교 포털에서 주소와 번호, 펙스번호 불러오기
import urllib.request

##순천향대학교 입력 받기
print("컴퓨터 공학과 23학번 김민환")
int = 0
g = input("대학교 이름을 입력하세요: ")
int = str(g)
##순천향대학교 포털 사이트 불러오고, 주소와 번호, 펙스번호 위치 찾기
if int == "순천향대학교":
    page = urllib.request.urlopen("https://portal.sch.ac.kr/p/index.jsp")

    text = page.read().decode("utf8")
    where = text.find("<address>")
    start_of_text = where + 9
    end_of_text = where + 69
    text = text[start_of_text: end_of_text]
    print(text)
else:
    print("")

if int == "오산대학교":
    page = urllib.request.urlopen("https://lms.osan.ac.kr/login.php")

    text = page.read().decode("utf8")
    where = text.find("<address>")
    start_of_text = where + 9
    end_of_text = where + 69
    text = text[start_of_text: end_of_text]
    print(text)
else:
    print("")
