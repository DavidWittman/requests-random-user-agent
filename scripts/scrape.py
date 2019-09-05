#!/usr/bin/env python

import requests
import requests_random_user_agent   # noqa: F401

from lxml import html


def main():
    # Use Google cache URL because blog has some anti-bot stuff going on
    url = ("https://webcache.googleusercontent.com/"
           "search?q=cache:FxxmQW9XrRcJ:https://techblog.willshouse.com/"
           "2012/01/03/most-common-user-agents/+&cd=4&hl=en&ct=clnk&gl=us")
    xpath = '//*[@id="post-2229"]/div[2]/textarea[1]'
    resp = requests.get(url)
    xml = html.fromstring(resp.content)
    elem = xml.xpath(xpath)[0]
    print(elem.text_content())


if __name__ == '__main__':
    main()
