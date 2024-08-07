import pyshorteners

s = pyshorteners.Shortener(api_key='YOUR_KEY')
s.bitly.short('http://www.google.com')
