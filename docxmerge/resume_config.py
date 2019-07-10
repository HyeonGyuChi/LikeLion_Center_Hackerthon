
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