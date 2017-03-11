from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import Config
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


def createEvent(info):
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store, flags) \
                if flags else tools.run(flow, store)
    CAL = build('calendar', 'v3', http=creds.authorize(Http()))

    GMT_OFF = '-07:00'      # PDT/MST/GMT-7
    EVENT = {
        'summary': "",
        'start':  {'dateTime': ""+'%s' % GMT_OFF},
        'end':    {'dateTime': ""+'%s' % GMT_OFF},
        'attendees': [
            {'email': Config.email},
        ],
    }
    CAL.events().quickAdd(
    calendarId='primary',
    text=info).execute()

    """
    e = CAL.events().insert(calendarId='primary',
            sendNotifications=True, body=EVENT).execute()

    print('''*** %r event added:
        Start: %s
        End:   %s''' % (e['summary'].encode('utf-8'),
            e['start']['dateTime'], e['end']['dateTime']))
    """

#createEvent()


#getDate("2016-10-04 17:57:29.542450","")

