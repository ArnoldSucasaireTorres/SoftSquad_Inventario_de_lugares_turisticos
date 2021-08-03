from apiclient.discovery import build
from datetime import datetime, timedelta 
import pickle

credentials = pickle.load(open('../token.pkl' , 'rb'))
service = build('calendar', 'v3', credentials=credentials)

result = service.calendarList().list().execute()

calendar_id = result['items'][0]['id']
result = service.events().list(calendarId=calendar_id).execute()

def agregarEvento(destino, inicio, fin):
    event = {
        'summary': str(destino),
        'location': 'Arequipa',
        'description': 'Viaje programado a '(str(destino)),
        'start': 
        {
            'dateTime': inicio,#'2015-05-28T09:00:00-07:00'
            'timeZone': 'America/Lima',
        },
        'end': 
        {
            'dateTime': fin,
            'timeZone': 'America/Lima',
        },
        'reminders': 
        {
            'useDefault': False,
            'overrides': 
            [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    created_calendar_list_entry = service.events().insert(calendarId=calendar_id,body=event).execute()

    print(created_calendar_list_entry['summary'])