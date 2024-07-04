import pandas as pd
import sys
sys.path.append('/Users/chriskim/Desktop/Programming/python/files/App-8-Instant-Dictionary-Webapp')

class Definition:

    def __init__(self, term):
        self.term = term

    def get(self):
        df = pd.read_csv('data.csv')
        return tuple(df.loc[df['word'] == self.term]['definition'])

d = Definition(term='sun')
print(d.get())