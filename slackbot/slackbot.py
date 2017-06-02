# coding:utf-8
"""This program run bot which tell us kagisys condition."""

import requests
import json
import time
import os


def main():
    """Main."""
    before_toggle = ""
    while True:
	# check not auth
	not_auth_list = check_not_auth()

	if "" != not_auth_list:
	    post(not_auth_list)

        # get new toggle data
        after_toggle = get_toggle()

        # if toggle changed, post to slack.
        if after_toggle != before_toggle:
            post(after_toggle)


        before_toggle = after_toggle
        time.sleep(1)


def post(text):
    """Post to Slack."""
    requests.post(
        # URL
        '''url''',

        # Other Property.
        data=json.dumps({
            'text': "7407:" + text,         # text
            'username': u'kagisys',         # user name
            'icon_emoji': u':kagi:', 	    # profile emoji
        })
    )


def get_toggle():
    """Get kagisys toggle data."""
    # move current directry
    os.chdir("/home/pi/project/kagisys_logic/")

    # read file
    file_ = open("kagisys.toggle", 'r')
    result = file_.read()

    return result


def check_not_auth():
    """check and post slack not to auth id"""
    # move current directry
    os.chdir("/home/pi/project/kagisys_logic/")

    # read file
    read_file = open("not_auth.log","r")
    result = read_file.read()

    print result

    # write file
    write_file = open("not_auth.log","w")
    write_file.write("")

    return result

		


if __name__ == '__main__':
    main()

