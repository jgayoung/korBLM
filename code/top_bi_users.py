# Scrape Tweets from Bilingual Authors but Labeled as Korean 07-15-2020

# Using GetOldTweets3 https://pypi.org/project/GetOldTweets3/
import GetOldTweets3 as got
import csv
import time

def get_tweets(lang, user):

    successful = False

    while successful is False:
        try:
            # specifying tweet search criteria 
            tweetCriteria = got.manager.TweetCriteria().setSince("2020-05-11")\
                                                   .setUntil("2020-07-01")\
                                                   .setLang(lang)\
                                                   .setUsername(user)
            
            # scraping tweets based on criteria
            tweets = got.manager.TweetManager.getTweets(tweetCriteria)
            
            text_tweets = [[tw.date, tw.username,
                        tw.text,
                        tw.id,
                        tw.hashtags,
                        tw.retweets,
                        tw.favorites,
                        tw.mentions] for tw in tweets]

            # save to file
            src_dir = f'../en_byuser/'
            filename = f'{src_dir}/{lang}_{user}.csv'

            with open(filename, "w+", newline="") as output:
                writer = csv.writer(output)
                writer.writerows(text_tweets)

            output.close()
            successful = True

        except SystemExit as err:
            print("Sleeping ", err)
            time.sleep(960)
        

def main():

    file_usernames = open("top_bi_users.txt", "r")

    list_of_usernames = []
    for line in file_usernames:
      stripped_line = line.strip()
      name = line.split()
      list_of_usernames.append(name)

    file_usernames.close()

    lang="en" 

    for user in list_of_usernames:
        get_tweets(lang, user)

if __name__ == "__main__":
    main()


    