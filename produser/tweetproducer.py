import tweepy
from json import dumps
from kafka import KafkaProducer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

access_token ="264630885-y2nJBVa6r5FfbcksmrO6Ixx1IodT6ZtZf2M29eQx"
acces_token_secret = "DL64aX0uelQLJwA9dYYbocCFycekdfQ37xO4aESziGo8J"
api_key = "2wWuJZcgdwM9VaO0l0nmoGVw5"
api_key_secret ="GwHxNyiHzVq6uP9Brvp0JIW0pQSDJ7YBnf6hodO5b3hqKBfONY"

auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,acces_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
# search_key = 'reksadana'
list_search = ['saham']

# c = []
# i = []
# u = []
# t = []

for perlist in list_search:
   #print(perlist)

    for tweet in tweepy.Cursor(api.search_tweets, q=perlist, count=1000, lang='id').items():
        print(tweet.created_at,tweet.id,tweet.user.name,tweet.text)
        lama = tweet.created_at
        baru = lama.strftime('%Y-%m-%dT%H:%M:%SZ')
        output = {"created_at":baru,"id":tweet.id,"username":tweet.user.name,"tweet":tweet.text,"topic":perlist}
        print(output)
        producer.send('twitter', value=output)
