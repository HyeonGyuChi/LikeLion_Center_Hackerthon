# LikeLion_Center_Hackerthon

멋쟁이 사자처럼 7기 중앙 해커톤

서비스명 : 이옷 (이력서 옷입히기)

  
  
## Quitck start:

```python

python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt

```
> Dependencies: comtypes==1.1.7 Django==2.2.3 pycryptodome==3.8.2 pypiwin32==223 django-authtools==1.7.0


## Apps informations

project : 프로젝트의 기본 메인 App, Settings 등의 정보 포함.

indexapp : 메인 화면(index) 담당 하는 App.

accountsapp : 유저 로그인 및 정보 관리.

docxmerge : 이력서 템플릿과 사용자 정보를 합쳐서 보여주는 App.

 

## Others

static/resume_templates : 이력서 템플릿이 들어 있는 폴더

static/resume_users : 이력서 템플릿에 사용자 정보를 입힌 파일들이 저장된다.

word : docx > xml or xml to docx 과정에서 생성되는 임시 파일들이 저장되는 장소.
> 즉, word는 신경 쓰지 않아도 된다.



## Patch note


**2019.07.24 : coin complete.** @rbgus(규현)

```
* ``accountsapp``의 ``user model``을 ``django.contrib.auth.models``이 아닌 커스텀 모델 구현
* ``accountsapp``의 ``user`` 모델에 coin기능 추가
```

***


**2019.07.10 : docx merge 0.1v complete.** @qwlake(정우)

```
* 이력서 템플릿에 사용자 정보 merge 기능 구현
* merge된 docx파일을 pdf로 출력 기능 구현
```

***


**2019.07.20 : detail page 0.1v complete.** @qwlake(정우)

```
* admin 계정의 템플릿 업로드 기능 추가
* 좋아요 기능 추가
* media 파일 경로 암호화(AES-256)
* docx to pdf 과정을 thread 사용으로 병렬화
```
