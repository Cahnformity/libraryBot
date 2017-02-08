from mchenry import *
from imp import *
my_room="3364"
time="2:00pm"
floor="445"
date="2017-02-14"
html=get_html(date, floor)
sid=get_sid(my_room, time, html)
#print(sid)
print (book_room(sid, floor, 'ben', 'cahn', 'bmcahn@ucsc.edu', 'philosphy', 'Undergraduate+student', 'Study+for+a+class'))
#sid, gid, fname, lname, email, nick, q1, q2
