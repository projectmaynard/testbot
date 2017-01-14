#!/usr/bin/env python

import os
import time
from slackclient import SlackClient


BOT_NAME = 'loki'
BOT_API_TOKEN = 'xoxb-120867732932-oxfl8Dg8hh4cGiBePEfpxm7m'
BOT_ID = 'U3JRHMJTE'
AT_BOT = "<@" + BOT_ID +">"
EXAMPLE_COMMAND = "do"

BOT_DIRECT_CHANNEL = 'D3J39J9U1'
VA_GENERAL_CHANNEL = 'C1ZG6Q2VD'
LOKI_TEST_CHANNEL = 'C3N37AZEY'


slack_client = SlackClient(BOT_API_TOKEN)


def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."
    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!"
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
    
        for output in output_list:
            if ('channel' in output.keys()) and ('text' in output.keys()) and (BOT_DIRECT_CHANNEL in output['channel']):
                print("@@@@ DIRECT MESSAGE: %s" % output['text'])
                slack_client.api_call("chat.postMessage", channel=LOKI_TEST_CHANNEL,
                          text=output['text'], as_user=True)


        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None

def start_slackbot(in_q):
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
 
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            msg = in_q.get()
            slack_client.api_call("chat.postMessage", channel=LOKI_TEST_CHANNEL,
                          text=msg, as_user=True)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")