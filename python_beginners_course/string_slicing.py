>>> data = 'XBOX 360 | 150 | New'
>>> data.index('|')
9
>>> data[9]
'|'
>>> product = data[:data.index('|')]
>>> product
'XBOX 360 '
>>> data[0:9]
'XBOX 360 '
>>> data[9:16]
'| 150 |'
>>> 
>>> 
>>> # [START : STOP : STEP]
>>> 
>>> greeting = 'Hi, how are you doing, it is very nice to meet you.'
>>> greeting
'Hi, how are you doing, it is very nice to meet you.'
>>> greeting[0:-1]
'Hi, how are you doing, it is very nice to meet you'
>>> greeting[0:-1:2]
'H,hwaeyudig ti eync ome o'
>>> greeting[0:-1:3]
'H wry i,tse ctmto'
>>> hi = 'hello'
>>> hi[::-1]
'olleh'
