import os, zipfile
from datetime import datetime
import comtypes.client
from win32com.client import pythoncom

from .models import Resume
from . import resume_config

def docx_to_pdf(docx, pdf):
    pythoncom.CoInitialize()
    wdFormatPDF = 17

    in_file = os.path.abspath(docx)
    out_file = os.path.abspath(pdf)

    print(in_file)
    print(out_file)

    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()

# Main
def merge(info, username):
    date = datetime.now().strftime("%Y. %m. %d.")
    replace_text = resume_config.requests(date, info)

    try:
        user_path = 'static/resume_users/' + str(username)

        # 작업 실행 시간
        create_time = datetime.today().strftime("%Y%m%d%H%M%S")

        # User 폴더가 없으면(신규 유저이면) User의 폴더 생성
        if not os.path.isdir('static/resume_users/'):
            os.mkdir('static/resume_users/')
        if not os.path.isdir(user_path):
            os.mkdir(user_path)
        if not os.path.isdir(user_path + '/docx'):
            os.mkdir(user_path + '/docx')
        if not os.path.isdir(user_path + '/pdf'):
            os.mkdir(user_path + '/pdf')

        # docx 파일 템플릿 리스트
        # media/resume_templates/template.docx
        template_url_list = []
        resume_list = []
        for res in Resume.objects.all():
            template_url_list.append(res.file.url[1:])
            resume_list.append(res)

        template_name_list = []
        new_name_list = []
        pdf_name_list = []
        export_url_list = []

        for template_url in template_url_list:
            template_name_list.append(template_url[template_url.rfind("/")+1:])

        for template_name, template_url in zip(template_name_list, template_url_list):

            # 생성될 파일 경로 및 이름
            # 'static/resume_users/{user_path}/docx/{create_time}-{template_name}'
            new_name = user_path + "/docx/" + create_time + "-" + template_name
            pdf_name = user_path + "/pdf/" + create_time + "-" + template_name[:template_name.rfind(".")] + '.pdf'
            new_name_list.append(new_name)
            pdf_name_list.append(pdf_name)

            # 병합될 파일 이름이 이미 존재한다면(너무 빠른 시간 안에 user가 다시 요청한 상태) 예외 발생
            if os.path.isfile(new_name):
                raise FileExistsError

            # 병합될 파일
            new_docx = zipfile.ZipFile(new_name, 'a')

            # docx 파일 템플릿
            template_docx = zipfile.ZipFile(template_url)

            # 템플릿 파일을 xml 포맷으로 압축 해제
            with open(template_docx.extract("word/document.xml"), encoding='UTF8') as temp_xml_file:
                temp_xml_str = temp_xml_file.read()

            # 템플릿의 변수들을 user의 정보로 교체
            for key in replace_text.keys():
                temp_xml_str = temp_xml_str.replace(str(key), str(replace_text.get(key)))

            # 병합된 정보를 xml 파일로 임시 저장
            with open("word/temp.xml", "w+", encoding='UTF8') as temp_xml_file:
                temp_xml_file.write(temp_xml_str)

            # 임시저장된 병합정보를 파일에 쓰기
            for file in template_docx.filelist:
                if not file.filename == "word/document.xml":
                    new_docx.writestr(file.filename, template_docx.read(file))
            new_docx.write("word/temp.xml", "word/document.xml")
            template_docx.close()
            new_docx.close()
        print("-----------------------------Merge complete------------------------------------")

        for new_name, pdf_name in zip(new_name_list, pdf_name_list):
            # pdf로 변환 및 static 경로 저장
            docx_to_pdf(new_name, pdf_name)
            export_url_list.append("../" + pdf_name)
        print("-------------------------Convert to pdf complete-------------------------------")

    except Exception as ex:
        raise ex
    return export_url_list, resume_list

# if __name__ == '__main__':
#     date = datetime.now().strftime("%y/%m/%d")
#     writer_id = "test-id1"
#     replace_text = config.requests(
#         date, 
#         '오정우', 
#         '강원도 춘천시 강원대학길1 공6호관', 
#         '010-4820-1442', 
#         'qwlake@gmail.com',)
#     resume(writer_id, replace_text)