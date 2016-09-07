import json, os
from slacker import Slacker

key = os.environ['SLACK_API_KEY']

slack = Slacker(key)

# Get users
users = slack.users.list()
u = users.body
with open('data/all_users.json', 'w') as f:
    json.dump(u, f)

# Get channels
channels = slack.channels.list()
c = channels.body
with open('data/all_channels.json', 'w') as f:
    json.dump(c, f)

# Get all events(messages) for each channel
channel_ids = [ch['id'] for ch in c['channels']]

def getMessages(channel_id, latest=None, count=1000):
    r = slack.channels.history(channel=channel_id, latest=latest, count=count)
    latest_ts = r.body['messages'][-1]['ts']
    with open('data/' + channel_id + '_' + str(latest_ts) +'.json', 'w') as f:
        json.dump(r.body, f)
        print("Saving file: " + channel_id + '_' + str(latest_ts))
    if r.body['has_more']:
        return latest_ts
    else:
        return None

for cid in channel_ids:
    r = slack.channels.history(cid)
    has_more = True
    latest = None
    while has_more:
        latest = getMessages(cid, latest)
        has_more=latest
