import oauth2
import constants
import urllib.parse as urlparse

consumer = oauth2.Consumer(constants.CONSUMER_KEY, constants.CONSUMER_SECRET)


def oauth_authorized():
    client = oauth2.Client(consumer)

    response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')
    if response.status != 200:
        print("An error occurred")

    return dict(urlparse.parse_qsl(content.decode('utf-8')))
