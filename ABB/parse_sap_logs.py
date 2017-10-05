loglist = log.split('\n')

disconnect_info ={}

a = loglist[5]
b = loglist[6]

#info_list = [log_date, log_time, instance, user, error_code,message_text,counter]
counter = 0
#log_date = b[1]
#log_time = b[2]
#instance = b[3]
#user = b[7]
#error_code = b[9]
#message_text = b[10]
#counter = 0

for i in loglist:
  i = i.split('|')
  
  if len(i) >= 10:
    i[7] = i[7].strip()
    if i[7] not in disconnect_info.keys():
      disconnect_info[i[7]] = {}
      disconnect_info[i[7]]['log_time'] = []
      disconnect_info[i[7]]['log_date'] = i[1].strip()
      disconnect_info[i[7]]['log_time'].append (i[2])
      disconnect_info[i[7]]['instance'] = i[3].strip()
      disconnect_info[i[7]]['error_code'] = i[9].strip()
      disconnect_info[i[7]]['message_text'] = i[10].strip()
      disconnect_info[i[7]]['counter'] = 1
      #print 'finished parsing %s' %i[7]
      #print '********************'
    elif i[7] in disconnect_info.keys():
    #print 'user already disconnected'
      disconnect_info[i[7]]['counter'] += 1
      if type (disconnect_info[i[7]]['log_time']) == list:
        disconnect_info[i[7]]['log_time'].append (i[2].strip())
#print disconnect_info.keys()
#for i in disconnect_info:

#print disconnect_info.keys()

for i in disconnect_info.keys():
  if disconnect_info[i]['counter'] >1:
    counter_str = disconnect_info[i]['counter']
    print 'user %s has %d disconnects' % (i, counter_str)
    print disconnect_info[i]['log_time']
