#!/usr/bin/python

import mymodule_123120
import json

class year():
  year_number=2020
  year_status='covid 19'

  def __init__(self, month, event):
    self.month=month
    self.event=event

  def challenge(self, item):
    print('During year like ' + str(y1.year_number) + ' still need to celebrate event like ' + y1.event + ' in ' + y1.month + ' while dealing with ' + item + ' all of the world ') 

y1=year('Dec', 'Xmas')
print(y1.month)

y1.challenge('Covid 19')

# inheritance

class year2(year):
  pass

y2=year2('Nov', 'Thanksgiving')
print(y2.event)

# dict

thisdict={
  'Mon': 'One',
  'Tue': 'Two',
  'Wed': 'Three'
}

# for loop
# print dict key 

for a in thisdict:
  print(a)

# print dict value using braket

for b in thisdict:
  print(thisdict[b])

# adding key/value in dict

thisdict['Thurs']='Four'

for c in thisdict:
  print(c)

# list 

thatlist=['Jan', 'Feb', 'March']

for d in thatlist:
  print(d)

# adding item on list

thatlist.append('April')

for e in thatlist:
  print(e)

# calling method from module

mymodule_123120.greeting('Jordan')

# method

def hello(name):
  print('Happy New Year !!! ' + name)

hello('Family')

# try except

today='Thurs'

try:
  print(todayy)
except:
  print('todayy is NOT defined')

# json

f='{"Mon": "mon","Tue": "tue","Wed": "wed"}'

g=json.loads(f)
print(g['Mon'])

# if else statement

month='Dec'

if month == 'Dec':
  print('It is Dec')
else:
  print('Not Dec')


# while statement

grade=7

print('Attenting grade ' + str(grade) +  ' now' )

while grade < 12:
  grade += 1
  print('Will attending grade ' + str(grade) + ' Next ')

print('Will be attending Collesge Next ')

# join two lists

h=['a', 'b', 'c']
i=['d', 'e', 'f']

for j in i:
  h.append(j)

for k in h:
  print(k)

 
