"""
launches the twitter scraper with the arguments

       querysearch: a query text to be matched
          username: a username or a list of usernames (comma or space separated)
                    of a specific twitter account(s) (with or without @)
username-from-file: a file with a list of usernames,
             since: a lower bound date in UTC (yyyy-mm-dd)
             until: an upper bound date in UTC (yyyy-mm-dd) (not included)
              near: a reference location area from where tweets were generated
            within: a distance radius from "near" location (e.g. 15mi)
         toptweets: only the tweets provided as top tweets by Twitter (no parameters required)
         maxtweets: the maximum number of tweets to retrieve
              lang: the language of tweets
            output: a filename to export the results (default is "output_got.csv")

"""



import os

os.system("python get_old_tweets.py --querysearch \"dlsu\" --maxtweets \"400\" --since \"2020-04-01\"")