# Scrapes English bc line 66

# Using GetOldTweets3 https://pypi.org/project/GetOldTweets3/
import GetOldTweets3 as got
import csv
import time

time2rest = 0

def get_tweets(query, lang, user):
   
    # specifying tweet search criteria 
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query)\
                                           .setSince("2020-05-11")\
                                           .setUntil("2020-07-05")\
                                           .setLang(lang)\
                                           .setUsername(user)
    
    # scraping tweets based on criteria
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    
    # creating list of tweets with the tweet attributes 
    # specified in the list comprehension
    # adapted from https://medium.com/@AIY/getoldtweets3-830ebb8b2dab
    text_tweets = [[tw.date, tw.username,
                tw.text,
                tw.id,
                tw.hashtags,
                tw.retweets,
                tw.favorites,
                tw.mentions] for tw in tweets]

    # save to file
    src_dir = f'../{lang}/'
    filename = f'{src_dir}/{lang}_{user}.csv'

    with open(filename, "w+", newline="") as output:
        writer = csv.writer(output)
        writer.writerows(text_tweets)

    output.close()

    global time2rest

    if time2rest > 200: 
        time.sleep(960)
        time2rest = 0
    else:
        time2rest += 1

def main():
    # dates=["2020-05-11","2020-05-18","2020-05-25","2020-05-28","2020-06-01","2020-06-03","2020-06-05","2020-06-07","2020-06-09","2020-06-11",\
    # "2020-06-13","2020-06-15","2020-06-17","2020-06-19","2020-06-21","2020-06-23",\
    # "2020-06-25","2020-06-29","2020-07-04"]

    file_usernames = open("allusernames_noduplicates.txt", "r")

    list_of_usernames = []
    for line in file_usernames:
      stripped_line = line.strip()
      name = line.split()
      list_of_usernames.append(name)

    file_usernames.close()

    query="흑인 OR 백인 OR 조지-플로이드 OR 인종-차별 OR 브리오나-테일러 OR 미국-경찰 OR 美-경찰 OR 美-시위 OR 미국-시위 OR 미국-폭동 OR 美-폭동 OR black OR white OR george-floyd OR racist OR racism OR breonna-taylor OR cops OR police OR riot OR protest OR loot OR rally"
    lang="en" #only line that's diff from kor

    for user in list_of_usernames:
        get_tweets(query, lang, user)

if __name__ == "__main__":
    main()


    