
'''
{{date}}
{{writer_name}}
{{writer_address}}
{{writer_phone}}
{{writer_email}}
'''
def requests(date, writer_name, writer_address, writer_phone, writer_email):
    return {
        '{{date}}':date,
        '{{writer_name}}':writer_name,
        '{{writer_address}}':writer_address,
        '{{writer_phone}}':writer_phone,
        '{{writer_email}}':writer_email,
        }