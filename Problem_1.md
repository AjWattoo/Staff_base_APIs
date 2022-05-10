# Problem

A customer has many systems that generate news daily (e.g., WordPress). What would be
your suggestion to integrate it all on the Staffbase App? What steps do you think are
required for that?

## Integration to Staffbase

With the Staffbase [News API](https://developers.staffbase.com/api/api-news#tag/channelschannelIDposts/paths/~1channels~1{channelID}~1posts/post), customer can import all the news content to a specific news channel in the Staffbase platform and publish it immediately. With News Api customer can set up an automation to import the news content on a regular basis.

### Requirments to import the news

1. Customer should first get his/her daily news content from the source in html format.

2. Get the [ChannelID](https://support.staffbase.com/hc/en-us/articles/115002996811-Determine-the-IDs-of-App-Contents) of Staffbase App in which customer want to integerate the news.

3. Make a POST request to endpoint [/channels/{channelID}/posts](https://developers.staffbase.com/api/api-news#tag/channelschannelIDposts/paths/~1channels~1{channelID}~1posts/post) to add a news post to the channel.

## Steps Requiredd for Integration

1. Extract all the news content in html fromat with any scripting language(e.g Python)

2. Write a script to pass this html content to Staffbase News API

3. Load News content on Staffbase

## Python Script for integration of News

Below customer can find script in `Python` for extracting the news and importing it to the Staffbase channel.

```Python

import requests,json
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Etract news from the source


url ='https://hevodata.com/learn/wordpress-python/'
data = urlopen(url)
soup = BeautifulSoup(data, 'html.parser')
content= soup.decode("utf-8")

# Make a POST requestto integerate all news to the Staff base Channel

access_token='Basic API TOKEN'
url='https://backend.staffbase.com/api/channels/{Channel_id}/posts'

headers={'Authorization': access_token,
         'Content-Type':'application/json'}
data={"contents":
          {"en_US":
               {"title": "test",
                "content": content}}}
data=json.dumps(data)
staffbase_news=requests.post(url,data=data,headers=headers)
print(staffbase_news.status_code)
News = json.loads(staffbase_news.text)
print(News)

```
