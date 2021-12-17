import os
import pysolr
import pandas as pd
import numpy as np
import datetime

# Create a client instance. The timeout and authentication options are not required.
solr = pysolr.Solr('http://127.0.0.1:8983/solr/lyric_core', always_commit=True)


def secondsToText(secs):
    conversion = datetime.timedelta(seconds=secs)
    return str(conversion)


# Parse csv allowed by SOLR
def load_docs(path="tcc_ceds_music.csv"):
    cols = ["artist_name", "track_name", "release_date", "genre", "lyrics", "len"]

    df = pd.read_csv(path)[cols]
    df["len"] = df["len"].apply(lambda x: secondsToText(int(x)))

    df["corpus"] = df["track_name"] + " " + df['lyrics']

    return df.to_dict('records')


# doc list
doc_list = load_docs()

# send the data to the solr server that is running on my local machine for indexing
solr.add(doc_list)







