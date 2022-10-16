### 본 프로젝트는 [Youtube-dl](https://github.com/ytdl-org/youtube-dl)과 BeautifulSoup을 이용하여 나만의 음악 다운로더 프로그램을 만드는 것입니다.
      
- 원하는 음원 사이트에서 상위 10개의 음원을 Youtube-dl을 통해 *.mp3 확장자 형태로 다운로드 받고 [eyeD3](https://eyed3.readthedocs.io/en/latest/) 등으로 ID3 태그를 음원 사이트에서 "제목", "가수", "앨범", "앨범아트" 정보를 파싱하여 설정합니다.
    
- 특정 음악을 검색하여 검색 결과 상에서 해당하는 음악을 Youtube-dl을 통해 *.mp3 확장자 형태로 다운로드 받고 [eyeD3](https://eyed3.readthedocs.io/en/latest/) 등으로 ID3 태그를 음원 사이트에서 "제목", "가수", "앨범", "앨범아트" 정보를 파싱하여 설정합니다.
    
- 위 라이브러리를 통해 *.mp3로 변환하기 위하여 [FFmpeg](https://ffmpeg.org/)가 요구됩니다.

---

### module

사용한 모듈을 아래와 같습니다.

![image](https://user-images.githubusercontent.com/88240193/167802697-ea6aefe6-af92-45a1-a404-b5033f03c96b.png)




---

## 클래스

사용자 정의 클래스는 2가지입니다.

1. class download_mp3() 
2. class getVideo() 

---

## 클래스별 메소드 수행기능

### download-mp3 클래스

#### 1. extractInfo 

> input 값으로 주어진 링크에서 정보를 추출

#### 2. setOpition 

> 다운로드 받을 영상의 설정값을 지정. (format / postprocessors / key / preferredcodec / preferredquality ) 

> 유튜브에서 검색한 영상을 .m4a(영상) 파일을 다운로드 하고 .mp3(오디오) 파일로 변환

#### 3. download

> 지정된 해당 주소에 대한 영상을 다운로드 실행

> 다운로드가 완료된 파일은 tags 메소드에서 속성을 지정해줍니다.

#### 4. tags

> eyed3 를 통한 .mp3 파일의 속성 지정

> 지정할 속성은 아래 3가지입니다

> 가수 : artist, 엘범 : album, 제목 : title

> 지정한 속성에 대한 저장을 위해 save() 선언

---

### get_video 클래스


#### getURL

> Beautifulsoup 객체를 선언하여 파싱을 시작할 경로를 지정해줍니다.


#### getINFO

> 해당 영상에 대한 파싱 작업을 통해, 여러 태그 중에서 원하는 특정 정보를 추출해 냅니다.

> 해당 영상으로 부터 추출해낸 정보를 각 정보에 적합한 리스트에 저장합니다.


#### selection

> 상위 3개의 음악중 다운로드 받을 음악의 순번을 입력받습니다. (INPUT: 1~3 사의의 정수)

> 이 외의 값을 입력받는다면 1번째 음악을 다운로드 받을 수 있습니다.




























