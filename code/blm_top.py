#Using GetOldTweets3 https://pypi.org/project/GetOldTweets3/
import GetOldTweets3 as got
import csv
import time


def get_tweets(query, start, end, filename):
   
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query)\
                                           .setSince(start)\
                                           .setUntil(end)\
                                           .setLang("en")\
                                           .setTopTweets(True)
                                           # \
                                           # .setExcludeWords()
    
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
    src_dir = f'./{filename}/'
    filename = f'{src_dir}/{filename}_{start}_to_{end}.csv'

    with open(filename, "w+", newline="") as output:
        writer = csv.writer(output)
        writer.writerows(text_tweets)

    output.close()

    time.sleep(960)


def main():
    dates=["2020-05-25","2020-05-26","2020-05-27","2020-05-28","2020-05-29","2020-05-30","2020-05-31",\
    "2020-06-01","2020-06-02","2020-06-03","2020-06-04","2020-06-05","2020-06-06",\
    "2020-06-07","2020-06-08","2020-06-09","2020-06-10","2020-06-11","2020-06-12",\
    "2020-06-13","2020-06-14","2020-06-15","2020-06-16","2020-06-17","2020-06-18","2020-06-19",\
    "2020-06-20","2020-06-21","2020-06-22","2020-06-23","2020-06-24","2020-06-25","2020-06-26",\
    "2020-06-27","2020-06-28","2020-06-29","2020-06-30","2020-07-01","2020-07-02","2020-07-03"\
    "2020-07-04","2020-07-05"]

    query="black-lives-matter OR blm"
    folder="enTopBlackLivesMatter"

    for i in range(len(dates)-1):
        get_tweets(query,dates[i],dates[i+1],folder)

if __name__ == "__main__":
    main()


    