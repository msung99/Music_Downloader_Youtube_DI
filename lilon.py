from __future__ import unicode_literals 
#파이썬 3에서 쓰던 문법을 파이썬2에서 쓸수있게 해줌
#from 모듈 import 이름 (from 파일명(라이브러리) import 함수이름)

from selenium import webdriver  #selenuim패키지에서 webdriver
#유튜브는 동적페이지 라서 사용자의 행동에 따라 서버에서 정보가 바뀜
#따라서 selenium 을 사용해야함
from selenium.webdriver.common.keys import Keys
import time



from bs4 import BeautifulSoup
#bs4 라이브러리에서 Beautifulsoup 사용 선언
import lxml
import requests 
\
import pandas
import youtube_dl

import os
import eyed3

import get_info
import Download



#headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

print("Insert the keyword")


keyword=input("")
#url='https://www.youtube.com/results?search_query={}'.format(keyword)
url=f'https://www.youtube.com/results?search_query={keyword}'

# driver = webdriver.Chrome(executable_path='C:\Python27\chromedriver.exe')

# # chromedriver를 본인의 크롬 버전에 맞춰 설치하고 설치한 경로를 path에 써주세요
# driver.get(url)
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# driver.close()

# # 해당 영상에 대한 파싱 작업을 통해, 여러 태그 중에서 원하는 특정 정보를 추출해 낸다.
# name = soup.select('a#video-title')
# video_url = soup.select('a#video-title')
# view = soup.select('a#video-title')

# # name, url, view 정보를 저장할 리스트 생성
# name_list = []
# url_list = []
# view_list = []

# # 해당 비디오(영상)으로 부터 추출해온 정보를 리스트에 저장
# for i in range(len(name)):
#     name_list.append(name[i].text.strip())
#     view_list.append(view[i].get('aria-label').split()[-1])
# for i in video_url:
#     url_list.append('{}{}'.format('https://www.youtube.com',i.get('href')))
    
# youtubeDic = {
#     '제목': name_list,
#     '주소': url_list,
#     '조회수': view_list
# }


# print(name_list[0]) # name_list에 담긴 상위 3개 영상의 이름을 출력
# print(name_list[1])
# print(name_list[2])
# print('옵션 1,2,3 을 선택하세요') 
# o=input()   #옵션 1,2,3 중 하나 선택



# if(o=='1'):        # 입력값에 해당하는 링크 정보를 url_list에서 꺼내 변수 link에 저장
#     link=url_list[0]
# elif(o=='2'):
#     link=url_list[1]
# elif(o=='3'):
#     link=url_list[2] 
# else:      #외에 것을 입력하면 최상단의 영상 다운
#     link=url_list[0]
    

sth = get_info.getVideo()
sth.getURL(url)
names, urls = sth.getINFO()



print(names[0])
print(names[1])
print(names[2])

link = sth.selection(urls)




# link = input ("") # 또는 아래와 같이 직접 유튜브 동영상 주소를 파이썬 스크립트 파일에 복사


# ydl=youtube_dl.YoutubeDL({}) # 주어진옵션에 따라 파일 다운로더 객체 생성 (YoutubeDL 객체 생성)
# with ydl:
#     video=ydl.extract_info(link,download=False)  # 해당 링크에서 정보를 추출하여 video에 저장 (download=False로 다시 음원이 다운되는 것을 방지함)
# print('{}--{}--{}'.format(video['artist'],video['track'],video['album'])) # video 객체에 저장된 노래의 정보 중, 가수, 제목, 앨범명을 순서대로 출력

# a=video['track'] 



# # 옵션 지정
# ydl_opts = {

#     'format': 'bestaudio/best',   # 최고음질 오디오

#     'postprocessors': [{       # 후처리 프로세서 : 후처리적인 계산이나 편집, 교환을 행함

#         'key': 'FFmpegExtractAudio',   # 키 : FFmpeg를 사용

#         'preferredcodec': 'mp3',      # .mp3 형태로 변환
         

#         'preferredquality': '320',   # 품질 : 320k

#     }],
    
#     'outtmpl':f"{os.getcwd()}/{a}.m4a"   #파이썬 문자열안에 변수를 대치시키는 방법 f 와 {} 이용

# # YOUTUBE에서 검색한 영상을 .m4a(영상) 파일을 다운로드 하고 .mp3(오디오) 파일로 변환
# }



# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
   
#     ydl.download([link])    # YOUTUBE에서 검색한 결과의 주소를 통해 youtube-dl을 이용하여 다운로드

# audiofile = eyed3.load(f"{a}.mp3")      # 다운로드 완료한 .mp3 파일을 불러옴
# audiofile.initTag(version=(2,3,0))      # eyed3의 버전
# audiofile.tag.artist = video['artist']  # eyed3를 사용하여 .mp3 파일의 artist 속성 추가 
# audiofile.tag.album = video['album']    # eyed3를 사용하여 .mp3 파일의 album 속성 추가 
# audiofile.tag.title = video['track']    # eyed3를 사용하여 .mp3 파일의 track 속성 추가 
# audiofile.tag.save()                    # 추가된 속성 tag 저장



sth2 = Download.download_mp3()
A = sth2.extractInfo(link)
sth2.setOpition(A)
audio = sth2.download(A,link)
sth2.tags(audio)

