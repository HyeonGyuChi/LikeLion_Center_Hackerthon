import os, zipfile
from datetime import datetime
import comtypes.client
from win32com.client import pythoncom

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
def resume(info, username):
    date = datetime.now().strftime("%Y. %m. %d.")
    replace_text = resume_config.requests(date, info)

    try:
        user_path = 'static/resume_users/' + str(username)

        # 작업 실행 시간
        create_time = datetime.today().strftime("%Y%m%d%H%M%S")

        # User 폴더가 없으면(신규 유저이면) User의 폴더 생성
        if not os.path.isdir(user_path):
            os.mkdir(user_path)

        # docx 파일 템플릿 리스트
        templates_path = "static/resume_templates/"
        file_list = os.listdir(templates_path)

        # 생성된 파일 경로 리스트
        export_list = []

        for template_name in file_list:

            # 생성될 파일 경로 및 이름
            # 'static/resume_users/user_path/create_time-template_name'
            new_file_name = user_path + "/" + create_time + "-" + template_name

            # 병합될 파일 이름이 이미 존재한다면(너무 빠른 시간 안에 user가 다시 요청한 상태) 예외 발생
            if os.path.isfile(new_file_name):
                raise FileExistsError

            # 병합될 파일
            new_docx = zipfile.ZipFile(new_file_name, 'a')

            # docx 파일 템플릿
            template_docx = zipfile.ZipFile(templates_path + template_name)

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

            # static/resume_templates/test.docx
            pdf_name = new_file_name[:new_file_name.rfind(".")] + '.pdf'
            docx_to_pdf(new_file_name, pdf_name)
            export_list.append("../" + pdf_name)
    except Exception as ex:
        raise ex
    return export_list

if __name__ == '__main__':
    date = datetime.now().strftime("%y/%m/%d")
    writer_id = "test-id1"
    replace_text = config.requests(
        date, 
        '오정우', 
        '강원도 춘천시 강원대학길1 공6호관', 
        '010-4820-1442', 
        'qwlake@gmail.com',)
    resume(writer_id, replace_text)