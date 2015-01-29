#!/usr/bin/env python
import cgi


form = cgi.FieldStorage()
val1 = form.getvalue('firstname')
val2 = form.getvalue('lastname')
print "Content-type: text/html\r\n"
if(val1):
	print "Your first name is:" + val1 + ".<br>"
else:
	print "You have no first name <br>"
if(val2):
	print "Your last name is:" + val2 + ".<br>"
else:
	print "You have no first name <br>"

print "<br/>"
print "<form method=post action=form.py>"
print "Birthdate: <br>"
print "<input type=date name=birthdate>"
print "<br/>"
print "Hobbies: <br>"
print "<textarea name=hobbies cols=40 rows=5>"
print "Enter hobbies here..."
print "</textarea>"
print "<br/>"

print "<input type=submit value=Submit>"
print "</form>"


