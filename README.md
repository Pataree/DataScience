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

After collecting data from APIs, I store the data into the Amazon Web Service (AWS) Database RDS

Each time, I need data, I will query the database instead of getting it from APIs again.

I then use the semi conductor ETF as benmark, by getting the % return from each shares vesus ETF.

At the end, I can tell which shares I should be purchased to reduce the risk but still getting decent return.

However it does not answer me if I want to know how much each shares are going to be worth, let's say in a year time.


Second approach

I rewrote the code, and now getting live data streamed directly from the APIs for financial data.

I re-wrote code into a class so it can be re-useable and re-called mulitple times

I will not used ETFs as benchmark but considered semi conductor ETFs to be just like any another stock instead

I use the Yahoo Finance - 1 yr target est as my benchmark

To my surprised, the shares I would love to invest in is still ETTs but not a semi conductor ETFs.
This is due to facts that now I can just pluck in any shares price (stock ticker) in to see the forecasts data.

PS>> I love the idea of ETFs having many different stocks inside, so it would lower my risks as well as having diversify porfolios

And now you can you Demo by change the stock name and the start dates/end dates


Summary

* Getting data from APIs, from quandl, yahoo, alpha vantage, and twitter are all different.  I had find web scrapping

* Natural Language Processing (NLP) was fun but I did not manage to integrated it into my project and how it would impact share price due to insufficent data


Though there are lots of other things I would love to experiment, I will need a bit more time to learn and investigate.

This topic is totally new to me and I found it fascinating.



