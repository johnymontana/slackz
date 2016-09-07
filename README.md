## Slackz

A super simple Python script to pull down all Slack Users, Channels, and Messages. This could be useful for offline analysis.

## Dependencies

This script uses [Slacker](https://github.com/os/slacker), a Python wrapper for the Slack API.

## To Use

1. Generate a Slack API key: https://api.slack.com/docs/oauth-test-tokens
1. Set this key as an environment var: `set -x SLACK_API_KEY your_api_key_here`
1. `pip install slacker`
1. `python slackz.py`

## Results

The `slackz.py` script will fetch all users, messages, and channel information for the Slack team that pertains to the provided key, saving the data as JSON in the following format:

* **all_users.json** - Information about each user (id, name, etc)
* **all_channels.json** - Information about each channel (id, name, members, etc)
* **channelid__ts.json** - Events (including messages) are saved for each channel in batches of 1000 with the file naming convention `channel_id`_`ts` where channel_id is the id of the channel and ts is the timestamp of the last event in that file.
