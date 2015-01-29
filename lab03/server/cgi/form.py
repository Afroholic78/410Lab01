#!/usr/bin/env python
import cgi

print "Content-type: text/html\r\n"
print "<form method=post action=test_form.py>"
print "First name: <br>"
print "<input type=text name=firstname>"
print "<br/>"
print "Last name: <br>"
print "<input type=text name=lastname>"
print "<br/>"
print "<input type=submit value=Submit>"
print "</form>"



form = cgi.FieldStorage()
val1 = form.getvalue('birthdate')
val2 = form.getvalue('hobbies')


if(val1):
	print "Your birthdate is: " + val1 + ".<br>"
else:
	print "You have no birthdate name <br>"
if(val2):
	print "Your hobbies is/are: " + val2 + ".<br>"
else:
	print "You have no hobbies... get a life <br>"