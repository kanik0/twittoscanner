import tweepy
import csv
from pathlib import Path
from time import sleep

time_delay = 2.5                       # Refresh time. There is a limit of 450 requests per 15 minutes, so don't go below 2 seconds
outputfile = "output.csv"              # Output file name
language = "en"                        # Language selection, use an ISO 639-1 code. Ex. "en" for English

# AUTH

consumer_key = 'null'                                          # Your personal consumer key
consumer_secret = 'null'                                       # Your personal consumer secret
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api=tweepy.API(auth)


# Init file (checks if file exists)

testfile = Path(outputfile)
if testfile.is_file():
  csvfile = open(outputfile, 'a')
  writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

else:
  csvfile = open(outputfile, 'w')
  writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
  writer.writerow(['Day', 'Time', 'Username', 'Text', 'Location'])

## Search

# Init

tweets = api.search(q="*", lang=language, count=100)

for tweet in reversed(tweets):
  if tweet.place:
    print(tweet.created_at.strftime("%d/%m/%Y") + " | " + tweet.created_at.strftime("%H:%M:%S") + " | " + " | " + tweet.user.screen_name + " | " + tweet.text + " | " + tweet.place.name)
    writer.writerow([tweet.created_at.strftime("%d/%m/%Y"), tweet.created_at.strftime("%H:%M:%S"), tweet.user.screen_name, tweet.text, tweet.place.name])
  else:
    print(tweet.created_at.strftime("%d/%m/%Y") + " | " + tweet.created_at.strftime("%H:%M:%S") + " | " + tweet.user.screen_name + " | " + tweet.text + " | " + "Unknown")
    writer.writerow([tweet.created_at.strftime("%d/%m/%Y"), tweet.created_at.strftime("%H:%M:%S"), tweet.user.screen_name, tweet.text, "Unknown"])

mostrecent_id = tweets[0].id

print("--\n Waiting "+str(time_delay)+" seconds.. \n--")
sleep(time_delay)

# While loop

while True:

  tweets = api.search(q="*", since_id=mostrecent_id, lang=language, count=100)
  for tweet in reversed(tweets):
    if tweet.place:
      print(tweet.created_at.strftime("%d/%m/%Y") + " | " + tweet.created_at.strftime("%H:%M:%S") + " | " + tweet.user.screen_name + " | " + tweet.text + " | " + tweet.place.name)
      writer.writerow([tweet.created_at.strftime("%d/%m/%Y"), tweet.created_at.strftime("%H:%M:%S"), tweet.user.screen_name, tweet.text, tweet.place.name])
    else:
      print(tweet.created_at.strftime("%d/%m/%Y") + " | " + tweet.created_at.strftime("%H:%M:%S") + " | " + tweet.user.screen_name + " | " + tweet.text + " | " + "Unknown")
      writer.writerow([tweet.created_at.strftime("%d/%m/%Y"), tweet.created_at.strftime("%H:%M:%S"), tweet.user.screen_name, tweet.text, "Unknown"])

  mostrecent_id = tweets[0].id
  print("--\n Waiting "+str(time_delay)+" seconds.. \n--")
  sleep(time_delay)

csvfile.close()
