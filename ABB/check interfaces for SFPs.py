output = '''
<12500-Prod>display interface ten 1/2/0/7  | in "Media type is"
Media type is optical fiber, Port hardware type is 1000_BASE_T_AN_SFP
<12500-Prod>display interface ten 1/2/0/8  | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 1/2/0/10 | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 1/2/0/14 | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 1/2/0/15 | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 1/2/0/16 | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 1/2/0/17 | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 1/2/0/18 | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 1/2/0/19 | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 1/2/0/24 | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 1/3/0/2  | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 1/3/0/6  | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 1/3/0/7  | in "Media type is"
Media type is optical fiber, Port hardware type is 1000_BASE_T_AN_SFP
<12500-Prod>display interface ten 1/3/0/8  | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 1/3/0/9  | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 1/3/0/20 | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 2/2/0/2  | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 2/2/0/6  | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 2/2/0/8  | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 2/2/0/10 | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 2/2/0/14 | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 2/2/0/15 | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 2/2/0/16 | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 2/2/0/17 | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 2/2/0/18 | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 2/2/0/19 | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 2/2/0/24 | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 2/3/0/2  | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 2/3/0/6  | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 2/3/0/8  | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 2/3/0/9  | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 2/3/0/10 | in "Media type is"
Media type is optical fiber, Port hardware type is 10G_BASE_SR_SFP
<12500-Prod>display interface ten 2/3/0/11 | in "Media type is"
Media type is optical fiber, Port hardware type is 10G_BASE_SR_SFP
<12500-Prod>display interface ten 2/3/0/18 | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 2/3/0/19 | in "Media type is"
Media type is not sure, Port hardware type is No connector
<12500-Prod>display interface ten 2/3/0/20 | in "Media type is"
Media type is not sure, Port hardware type is No connector
'''

port_list = output.split('\n')
port_list = filter(None, port_list)

pairs = []

a = len(port_list)

counter = 0
while counter < a:
  combined = port_list[counter] + port_list[counter +1]
  pairs.append(combined)
  counter +=2

sfps = []
  
for i in pairs:
  if 'Media type is not sure' not in i:
    sfps.append(i)
    
for i in sfps:
  print i
  