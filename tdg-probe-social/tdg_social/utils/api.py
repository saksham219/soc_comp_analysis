from datetime import datetime
from dateutil import tz,parser
from tdg_social.models.channel import Channel
import re

def get_page_name(competitor_id):
    name = Channel.query.filter(Channel.id == int(competitor_id)).first().page_name
    return(name)

def get_local_time(timestamp):
    date = datetime.fromtimestamp(timestamp)
    date_utc = date.replace(tzinfo = tz.gettz('UTC'))
    date_local = date_utc.astimezone(tz.tzlocal())
    return(date_local)

def return_datestamp(date_created):
    date_timestamp = parser.parse(date_created).astimezone(tz.tzlocal())
    return(date_timestamp)

def split_day_by_hour(hour_period):
    j=0
    hours_of_day = []
    for i in range(0,int(24/int(hour_period))):
        hours_of_day.append((j,j+ int(hour_period)))
        j = j+int(hour_period)
    return(hours_of_day)

def get_hash(post):
    hashtag_list ={tag.strip("#") for tag in post.post_content.replace('#',' #').split() if tag.startswith("#")}
    hashtag_list = {re.findall(r"[\w]+|[^\s\w]",i)[0] for i in hashtag_list if i!=''}
    return(hashtag_list)


#######for twitter APIS###############

def return_timestamp_twitter(date_created):
    date_timestamp = parser.parse(date_created).timestamp()
    return(date_timestamp)
