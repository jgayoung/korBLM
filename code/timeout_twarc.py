import datetime
import os
import subprocess

src_dir = '../korBLMtweets/data/'
now = datetime.datetime.now()
timestr = now.strftime("%Y-%m-%d_%H%M")
filename = f'{src_dir}/korBlackLivesMatter_{timestr}.jsonl'
filename_replies = f'{src_dir}/cc_{timestr}_replies.jsonl'

# cmd = f'twarc filter coronavirus,covid19 --lang en > cc_{timestr}.jsonl'
cmd = ['/usr/local/bin/twarc', 'filter', '#BlackLivesMatter', '--lang', 'ko']

output = open(filename, 'w+')

try:
    subprocess.call(cmd, stdout=output, timeout=60*60)
except subprocess.TimeoutExpired as e:
    pass

output.close()
