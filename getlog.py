import win32evtlog
"""
def get_log():
    h = win32evtlog.OpenEventLog(None, "Application")
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
    records = win32evtlog.ReadEventLog(h, flags, 0)
    #print(len(records))  
    return (records[0])
"""
h = win32evtlog.OpenEventLog(None, "Application")
flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
records = win32evtlog.ReadEventLog(h, flags, 0)
#print(records[0].EventID)

thisdict = {
    "sourceName": records[0].SourceName,
    "eventId" : records[0].EventID
}

def get_log():
    return(thisdict)