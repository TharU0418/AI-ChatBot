import random
import json
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()

chats = json.loads(open('chat.json').read())