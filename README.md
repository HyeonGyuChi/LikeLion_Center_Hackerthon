# LikeLion_Center_Hackerthon
멋쟁이 사자처럼 7기 중앙 해커톤
팀명(가제) : 옷입는 이력서

  
  
## Dependencies:

```python

pip install django

pip install comtypes

pip install pypiwin32

```

  

## Apps informations

project : 프로젝트의 기본 메인 App, Settings 등의 정보 포함.

indexapp : 메인 화면(index) 담당 하는 App.

accountsapp : 유저 로그인 및 정보 관리.

docxmerge : 이력서 템플릿과 사용자 정보를 합쳐서 보여주는 App.

 

## Others

static/resume_templates : 이력서 템플릿이 들어 있는 폴더

static/resume_users : 이력서 템플릿에 사용자 정보를 입힌 파일들이 저장된다.

word : docx > xml or xml to docx 과정에서 생성되는 임시 파일들이 저장되는 장소.
> word는 신경 쓰지 않아도 된다.