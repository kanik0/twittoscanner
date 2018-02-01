# twittoscanner
A Python script that saves all the tweets in a specific language on a CSV file in real time.

# Install
- Go to https://apps.twitter.com/ and create a new app. Write the consumer key and the consumer secret down and be sure to keep them private.

- Install the tweepy module for python:
```
pip install tweepy

# or

easy_install tweepy
```

- Download and configure the python script by adding your key/secret to twittoscanner.py. Change the language variable to one of your choice (default is "en", English), using an ISO 639-1 code.

# Usage
```bash
:~$ python3 twittoscanner.py
```

# Additional parameters
- `time_delay` sets how long the script waits before loading new tweets. The API limits the script to 450 requests every 15 minutes, which means `time_delay` cannot be set below (15x60)/450 = 2 seconds.
- `outputfile` sets the file name for CSV output.
