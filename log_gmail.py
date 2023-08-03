from simplegmail import Gmail
from simplegmail.query import construct_query
import time

def pull_code():
    gmail = Gmail()

    query_params = {
        "newer_than": (1, "hour"),
        "unread": True,
        'sender': 'ifood'
    }
    
    while 1:
        try:
            messages = gmail.get_messages(query=construct_query(query_params))
            break
        except:
            time.sleep(3)
            
    ifood_code = messages[0].subject.split(' ')[0]
    
    messages[0].mark_as_read()
    
    return ifood_code