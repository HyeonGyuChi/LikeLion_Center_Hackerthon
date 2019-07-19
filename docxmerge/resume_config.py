
'''
{{date}}
{{writer_name}}
{{writer_address}}
{{writer_phone}}
{{writer_email}}
'''
def requests(date, info):
    dic = {
        '{{'+key+'}}':val.value() for key, val in zip(info.fields.keys(), info)
    }
    dic['{{date}}'] = date
    return dic

# AES-256 secret key
SECRET_KEY = "AKdfsrhtOWEad(*uJOEWLRSLDKFjowE8RU0(apfd"