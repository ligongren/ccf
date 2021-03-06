import icalendar
import datetime
import pytz

cal = icalendar.Calendar()
cal.add('prodid', '-//My calendar product//mxm.dk//')
cal.add('version', '2.0')

event = icalendar.Event()
event.add('summary', 'Python meeting about calendaring')
event.add('dtstart', datetime.datetime(2017, 4, 4, 8, 0, 0, tzinfo=pytz.utc))
event.add('dtend', datetime.datetime(2017, 4, 4, 10, 0, 0, tzinfo=pytz.utc))
event.add('dtstamp', datetime.datetime(2017, 4, 4, 0, 10, 0, tzinfo=pytz.utc))

organizer = icalendar.vCalAddress('MAILTO:noone@example.com')

organizer.params['cn'] = icalendar.vText('Max Rasmussen')
organizer.params['role'] = icalendar.vText('CHAIR')
event['organizer'] = organizer
event['location'] = icalendar.vText('Odense, Denmark')

event['uid'] = '20050115T101010/27346262376@mxm.dk'
event.add('priority', 5)

attendee = icalendar.vCalAddress('MAILTO:maxm@example.com')
attendee.params['cn'] = icalendar.vText('Max Rasmussen')
attendee.params['ROLE'] = icalendar.vText('REQ-PARTICIPANT')
event.add('attendee', attendee, encode=0)

attendee = icalendar.vCalAddress('MAILTO:the-dude@example.com')
attendee.params['cn'] = icalendar.vText('The Dude')
attendee.params['ROLE'] = icalendar.vText('REQ-PARTICIPANT')
event.add('attendee', attendee, encode=0)

cal.add_component(event)

import tempfile, os

directory = 'd:/'
# directory = tempfile.mkdtemp()
f = open(os.path.join(directory, 'example.ics'), 'wb')
f.write(cal.to_ical())
f.close()
