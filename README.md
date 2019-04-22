# requests-random-user-agent [![Build Status](https://travis-ci.org/DavidWittman/requests-random-user-agent.svg?branch=master)](https://travis-ci.org/DavidWittman/requests-random-user-agent) [![PyPI](https://img.shields.io/pypi/v/requests-random-user-agent.svg)](https://pypi.org/project/requests-random-user-agent/)

Configures the requests library to automatically use a popular desktop User-Agent.

### Installation

```
pip install requests-random-user-agent
```

### Usage

``` python
import requests
import requests_random_user_agent

s = requests.Session()
print(s.headers['User-Agent'])
```
