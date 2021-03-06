# LikeLion_Center_Hackerthon

멋쟁이 사자처럼 7기 중앙 해커톤

서비스명 : 이옷 (이력서 옷입히기)

  
  
## Quitck start:

```python

python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic

```
## Quick Start Bug handler
``` shell
DLL 을 참조할 수 없습니다
```
증상원인 - Pywin32 모듈문제

해결방법 - 관련 확장 종속라이브러리 설치하기
[github link](https://github.com/mhammond/pywin32/releases/tag/b224)




## Apps informations

project : 프로젝트의 기본 메인 App, Settings 등의 정보 포함.

indexapp : 메인 화면(index) 담당 하는 App.

users : 유저 로그인 및 정보 관리.

docxmerge : 이력서 템플릿과 사용자 정보를 합쳐서 보여주는 App.

 

## Others

`media/resume_templates` : 이력서 템플릿이 들어 있는 폴더

`media/resume_users` : 이력서 템플릿에 사용자 정보를 입힌 파일들이 저장된다.

`word` : docx > xml or xml to docx 과정에서 생성되는 임시 파일들이 저장되는 장소.
> 즉, word는 신경 쓰지 않아도 된다.

`Demo_Assets` : Demo test용 자원, demo templates으로 사용할 수 있는 템플릿 docx파일.
> 해당, demo_templates.docx를 이용해 파일업로드 후 작동테스트




## Patch note

**2019.08.03 : login page style complete.** @qwlake(정우)

* `result` 페이지 모달로 변경
* `detail` 페이지 삭제

***


**2019.08.03 : login page style complete.** @paekjiyeon(지연)

* `login` 로그인 페이지 스타일 변경

***


**2019.08.02 : loading page complete.** @qwlake(정우)

* `resume_make` 로딩중에 gif파일 띄워주는 기능 추가
* `resume_resule`, `resume_detail` 페이지에서 본인 외에는 접근 불가하게 보안성 강화

***


**2019.08.01 : resumelist complete.** @qwlake(정우)

* `resume_result` 페이지에 좋아요순, 다운로드순 정렬 및 오름차순, 내림차순 정렬 기능 추가
* `base.html` 디자인 변경
* 기타 버그 수정

***


**2019.07.26 : mypage complete.** @qwlake(정우)

* ``mypage``앱 완성 및 페이지(html) 완성
* 기존의 ``accountsapp`` 삭제 후, ``django-authtools``를 이용한 ``users`` 앱 생성
* ``result.html``과 ``detail.html``에서 ``Resume``의 다운로드 수 및 좋아요 수 보기 기능 추가

***


**2019.07.24 : coin complete.** @rbgus(규현)

* ``accountsapp``의 ``user model``을 ``django.contrib.auth.models``이 아닌 커스텀 모델 구현
* ``accountsapp``의 ``user`` 모델에 coin기능 추가

***


**2019.07.20 : detail page 0.1v complete.** @qwlake(정우)

* admin 계정의 템플릿 업로드 기능 추가
* 좋아요 기능 추가
* media 파일 경로 암호화(AES-256)
* docx to pdf 과정을 thread 사용으로 병렬화

***


**2019.07.10 : docx merge 0.1v complete.** @qwlake(정우)

* 이력서 템플릿에 사용자 정보 merge 기능 구현
* merge된 docx파일을 pdf로 출력 기능 구현

***
