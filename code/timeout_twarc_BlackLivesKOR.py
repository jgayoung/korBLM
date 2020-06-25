import datetime
import time
import os
import subprocess

while True:
    src_dir = '../data/BlackLivesKOR/'
    now = datetime.datetime.now()
    timestr = now.strftime("%Y-%m-%d_%H%M")
    filename = f'{src_dir}/blacklivesKOR_{timestr}.jsonl'
    filename_replies = f'{src_dir}/cc_{timestr}_replies.jsonl'

    # cmd = f'twarc filter coronavirus,covid19 --lang en > cc_{timestr}.jsonl'
    # cmd = ['/usr/local/bin/twarc', 'filter', '#BlackLivesMatter', '--lang', 'en']
    # cmd2 = ['/usr/local/bin/twarc', 'filter', '#흑인의_목숨은_소중하다,#흑인의목숨은소중하다,#흑인의_생명은_소중하다,#흑인의생명은소중하다,#조지플로이드,#조지_플로이드']
    cmd3 = ['/usr/local/bin/twarc', 'filter', '흑인']

    output = open(filename, 'w+')

    try:
        subprocess.call(cmd3, stdout=output, timeout=60*60)
    except subprocess.TimeoutExpired as e:
        pass

    output.close()
