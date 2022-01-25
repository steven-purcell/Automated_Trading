#!/usr/bin/env python
# coding: utf-8


from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys

import smtplib, ssl

import praw

import pandas as pd
import re
import requests

from pandas import json_normalize

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


google_search_template = 'https://www.google.com/search?q={}+site%3Acoinmarketcap.com'

# CoinMarketCap_API_Key = 'daaf6299-d06e-4847-840d-0747dba078c8'

subreddits = ['CryptoCurrency', 'CryptoMarkets', 'CryptoCurrencies', 'AltStreetBets', 'CryptoCurrencyTrading', 'ico', 'BSCMoonShots',
              'defi', 'CryptoMoonShots', 'ShitcoinBets', 'CryptoMarsShots', 'WallStreetBetsCrypto', 'CryptocurrencyICO', 'CryptoMars',
              'Crypto_Currency_News', 'SatoshiBets', 'BSCcryptoListings', 'SatoshiStreetBets', 'CryptoStreetBets', 'ShitCoinMoonShots',
              'CryptoMoon', 'MarsWallStreet', 'AllCryptoBets']

crypto_symbols = []


reddit = praw.Reddit(client_id = client_id,
                     client_secret = client_secret,
                     user_agent = user_ageent)

posts = []
symbols = []
search_list = []

for subreddit in subreddits:
    hot_posts = reddit.subreddit(subreddit).hot(limit=25)
    
    for post in hot_posts:
        symbolRegex = re.compile(r'(\$[A-Z][a-z]{3,})|([A-Z ]{3,})')
        # symbolRegex = re.compile(r'((^$)|[A-Z]{3,})')
        mo = symbolRegex.search(post.title)
        
        if mo != None:
            symbols.append(mo.group().strip())
#     for post in hot_posts:
        posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.created])
        
    
hot_posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'created'])
# hot_posts['created'] = pd.to_datetime(hot_posts['created'])


url = 'https://www.finder.com.au/cryptocurrency-list-all'

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

r = requests.get(url, headers=header)

dfs = pd.read_html(r.text)
dfs = dfs[0]
dfs = dfs.drop(['How to Buy'], axis=1)

remove_terms = ['GMT', 'NFT', 'FUD', 'AND', 'CEO', 'TIME', 'NOV', 'TIL', 'LISTINGS', 'NASDAQ',
                'YOLO', 'NASD', 'HODL', 'ARE', 'SHOULD', 'APY', 'LOL', 'BUY', 'USD', 'GME', 'ETH',
               'LISTING', 'DEFI', 'AMC', 'CAREFUL', 'QUESTION', 'NEWS', 'TPS', 'AIRDROP', 'NASCAR', 'WELCOME',
               'AIRDROP INCOMING', 'RELAUNCHING IN', 'NEW ARTICLE', 'JUST LAUNCHED']

remove_known_symbols = dfs.Symbol.tolist()

symbols = list(set(symbols))

for i in symbols:
    if i.count(' ') > 1:
        symbols.remove(i)

for term in remove_terms:
    while term in symbols: symbols.remove(term)
        
for known_symbol in remove_known_symbols:
    while known_symbol in symbols: symbols.remove(known_symbol)

for symbol in symbols:
    search_list.append(google_search_template.format(symbol.replace(' ', '+')))

result = pd.DataFrame(list(zip(symbols, search_list)), columns =['Possible Symbols / Project Names', 'CoinMarketCap Result'])


###################### Send Email below
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "Daily.Symbol.Research@gmail.com"
password = 'Polyphemus1!'

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)


    # TODO: Send email here
    recipients = ['slayorr.911@gmail.com', 'ChrismonHinsch@gmail.com'] 
    emaillist = [elem.strip().split(',') for elem in recipients]
    msg = MIMEMultipart()
    msg['Subject'] = "Daily Crypto Symbols/Projects"
    msg['From'] = 'Daily.Symbol.Research@gmail.com'


    html = """<html>
    <head></head>
    <body>
        {0}
    </body>
    </html>
    """.format(result.to_html())

    part1 = MIMEText(html, 'html')
    msg.attach(part1)

    server.sendmail(msg['From'], emaillist , msg.as_string())

except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 
