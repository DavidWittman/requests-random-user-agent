#!/usr/bin/env python

import requests
import requests_random_user_agent

from lxml import html

def main():
    url = "https://techblog.willshouse.com/2012/01/03/most-common-user-agents/"
    xpath = '//*[@id="post-2229"]/div[2]/textarea[1]'
    resp = requests.get(url)
    xml = html.fromstring(resp.content)
    elem = xml.xpath(xpath)[0]
    print(elem.text_content())


if __name__ == '__main__':
    main()
