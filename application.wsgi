import os, sys

PROJECT_DIR = '/www/tweetmap.goomap.com/TweetMapy'

activate_this = os.path.join(PROJECT_DIR, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from TweetMapy import app as application