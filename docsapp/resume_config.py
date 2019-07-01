# 이력서 템플릿. google drive에 존재하는 file의 ids.
files_ids = {"resume-test-1":"193nzLRXXCc-xCQTe6moQ6LH99H9UB5BFvwB7DYOEq4A",
             "resume-test-2":"1rww_2poRHg6nYGWroU1cUsmo0zp1wXJUywdMCqrTqN8"}

'''
{{date}}
{{writer_name}}
{{writer_address}}
{{writer_phone}}
{{writer_email}}
'''
def requests(date, writer_name, writer_address, writer_phone, writer_email):
    return [
        {
            'replaceAllText': {
                'containsText': {
                    'text': '{{date}}',
                    'matchCase':  'true'
                },
                'replaceText': str(date),
            }
        }, {
            'replaceAllText': {
                'containsText': {
                    'text': '{{writer_name}}',
                    'matchCase':  'true'
                },
                'replaceText': writer_name,
            }
        }, {
            'replaceAllText': {
                'containsText': {
                    'text': '{{writer_address}}',
                    'matchCase':  'true'
                },
                'replaceText': writer_address,
            }
        }
        , {
            'replaceAllText': {
                'containsText': {
                    'text': '{{writer_phone}}',
                    'matchCase':  'true'
                },
                'replaceText': writer_phone,
            }
        }, {
            'replaceAllText': {
                'containsText': {
                    'text': '{{writer_email}}',
                    'matchCase':  'true'
                },
                'replaceText': writer_email,
            }
        }
    ]