import pickle
import os.path
import io
import datetime
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from django.core.serializers.json import DjangoJSONEncoder
import json
from . import resume_config

# def json_default(value): 
#     if isinstance(value, datetime.datetime): 
#         return value.strftime('%Y/%m/%d') 
#     raise TypeError('not JSON serializable') 

# 웹페이지 서버에서 Google drive api server와 통신하기 위한 Oauth 2.0 인증
def auth():
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/drive']
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

# 이력서 템플릿의 복사본 생성
def drive_copy(creds, FILE_ID):
    service = build('drive', 'v3', credentials=creds)

    file = service.files().get(fileId=FILE_ID).execute()
    body = {
        'name': file.get('name') + "-copied"
    }

    drive_response = service.files().copy(
        fileId=FILE_ID, body=body).execute()
    document_copy_id = drive_response.get('id')
    file = service.files().get(fileId=document_copy_id).execute()
    print('The title of the document is: {}'.format(file.get('name')))
    return {"document_copy_id":document_copy_id, "file":file}

# 템플릿 복사본에 사용자 정보 삽입
def docs_merge(creds, DOCUMENT_ID, info):
    service = build('docs', 'v1', credentials=creds)
    date = datetime.datetime.now().strftime("%y/%m/%d")

    '''
    {{date}}
    {{writer_name}}
    {{writer_address}}
    {{writer_phone}}
    {{writer_email}}
    '''
    requests = resume_config.requests(date, info['writer_name'].value(), 
                                            info['writer_address'].value(), 
                                            info['writer_phone'].value(), 
                                            info['writer_email'].value())
    # requests = json.dumps(requests, indent=4, sort_keys=True, default=str)
    replies = service.documents().batchUpdate(
        documentId=DOCUMENT_ID, body={'requests': requests}).execute()
    result = merge_check(replies)
    print("merge result is: {}".format(result))
    
    return result

# 정보 삽입 무결성 체크
def merge_check(result):
    replies = result["replies"]
    for rep in replies:
        if not rep["replaceAllText"]["occurrencesChanged"] == 1:
            return False
    return True

# 변환된 문서를 pdf 파일로 export.
def drive_export(creds, FILE_ID):
    service = build('drive', 'v3', credentials=creds)

    request = service.files().export_media(fileId=FILE_ID, mimeType='application/pdf')

    orig_file = service.files().get(fileId=FILE_ID).execute()
    export_file_name = orig_file.get('name') + '.pdf'
    export_path = 'downloads/' + export_file_name    # 'downloads/export_file_name'

    fh = io.FileIO(export_path, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    return '../' + export_path

# Main
def resume(info):
    creds = auth()
    ids = resume_config.files_ids.values()
    export_paths = []
    for id in ids:
        copied = drive_copy(creds, id)
        result = docs_merge(creds, copied["document_copy_id"], info)
        if result is False:
            print("merge fail")
            break
        export_paths.append(drive_export(creds, copied["document_copy_id"]))
    return export_paths

# 실행
if __name__ == '__main__':
    resume({'writer_name':"오정우",
        'writer_address':"강원도 춘천시 강원대학길1 공6호관",
        'writer_phone':"010-4820-1442",
        'writer_email':"qwlake@gmail.com"})