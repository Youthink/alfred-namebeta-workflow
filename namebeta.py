#!/usr/bin/python
# encoding: utf-8

import sys

# Workflow3 supports Alfred 3's new features. The `Workflow` class
# is also compatible with Alfred 2.
from workflow import Workflow3, web

def get_web_data(query):
    return web.post('https://namebeta.com/api/query',
            data={'q':query}).json()

def main(wf):

    # The Workflow3 instance will be passed to the function
    # you call from `Workflow3.run`.
    # Not super useful, as the `wf` object created in
    # the `if __name__ ...` clause below is global...
    #
    # Your imports go here if you want to catch import errors, which
    # is not a bad idea, or if the modules/packages are in a directory
    # added via `Workflow3(libraries=...)`

    # Get args from Workflow3, already in normalized Unicode.
    # This is also necessary for "magic" arguments to work.
    args = wf.args

    # Do stuff here ...

    query = args[0]

    wf.add_item(title="Go to the website",
            subtitle="https://namebeta.com",
            arg="https://namebeta.com",
            valid=True)

    data = get_web_data(query)

    # data 2:占用  1:可以注册
    """
    [
        true,"query",
        [
            ["hufy.com",2,"hufy.com"],
            ["hufy.net",1,"hufy.net"],
            ["hufy.org",1,"hufy.org"],
            ["hufy.cn",2,"hufy.cn"],
            ["hufy.me",1,"hufy.me"],
            ["hufy.co",1,"hufy.co"],
            ["hufy.cc",1,"hufy.cc"],
            ["hufy.info",1,"hufy.info"],
            ["hufy.biz",1,"hufy.biz"],
            ["hufy.io",1,"hufy.io"]
        ],
        "hufy"
    ]
    """
    result = '已被注册'
    for datum in data[2]:
        if datum[1] == 2:
            result = '❌ 已被占用'
        else:
            result = '✅ 可以注册'

        wf.add_item(datum[0], result)

    # Add an item to Alfred feedback

    # Send output to Alfred. You can only call this once.
    # Well, you *can* call it multiple times, but subsequent calls
    # are ignored (otherwise the JSON sent to Alfred would be invalid).
    wf.send_feedback()


if __name__ == '__main__':
    # Create a global `Workflow3` object
    wf = Workflow3()
    # Call your entry function via `Workflow3.run()` to enable its
    # helper functions, like exception catching, ARGV normalization,
    # magic arguments etc.
    sys.exit(wf.run(main))
