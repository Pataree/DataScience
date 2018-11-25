# DataScience
Capstone Project

This is my capstone project about share price analysis

If you wish to use this, the only file you will need is "DEMO" file

I recreate this file into a class where it can be re-usable.

If you specify the name of a stock (share) tradded in the US market, no suffix is required.  
Examples are in AMD, NVDA, INTEL, MICRON TECH share analysis

If you specify the name of a stock (share) tradded in the AUS market, .ax suffix is required.


Lessons learn from this.

Creating Amazon Web Service (AWS) Database Instance, the security need to be adjusted so it can be connected from other locations

Twitter Sentimently Analysis, though end up did not used in the share price analysis, it was pretty interesting how to get the data, 
and was fun to do the Natuarl Language Process (text blob) analysis to know if each tweet has positive, negative or neutral sentiment to it.

Also another fun facts found was that if the tweets are re-tweets, there should be more views, but it does not seem to happen in all cases.

At the begining, I was planning to investigate only 5 stocks in the US which is in the same section - semi conductor

So how should I benchmark each stock against?  

First approach

I with be getting the %return from each shares vesus the semi conductor ETF.
At the end, I can tell which shares I should be purchased

However it does not answer me if I want to know how much each shares are going to be worth, let's say in a year time.


Second approach

I rewrote the whole set, and now getting live data streamed directly from the APIs for financial data

I think re-wrote a class so it can be re-useable and re-called mulitple times

I will not used ETFs as benchmark but will considered it as another stock instead

I use the Yahoo Finance - 1 yr target est as my benchmark

And now you can you Demo by change the stock name and the start dates/end dates


Summary
Though there are lots of other things I would love to experiment, I will need a bit more time to learn and investigate.
NLP was fun but at then end I did not manage it to be integrated into how it would impact share price due to not enough data


