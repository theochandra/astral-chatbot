dict_data = {'errorCode': '92', 'errorMessage': 'Error in database'}

print dict_data['errorCode']

key = 'errorCode'
if key in dict_data:
    print 'ada'
else:
    print 'tidak ada'

flag = getattr(dict_data, 'errorCode', None)
if flag is None:
    print "masuk none"
    print flag
else:
    print flag