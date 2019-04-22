# requests-random-user-agent [![Build Status](https://travis-ci.org/DavidWittman/requests-random-user-agent.svg?branch=master)](https://travis-ci.org/DavidWittman/requests-random-user-agent)

Configures the requests library to automatically use a popular desktop User-Agent.

### Usage

``` python
import requests
import requests_random_user_agent

s = requests.Session()
print(s.headers['User-Agent'])
```
