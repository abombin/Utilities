import pandas as pd
import argparse


meta=pd.read_csv(filepath_or_buffer='MLS_teammates_meta.tsv', sep='\t')

meta['location']=meta['location'].str.replace(' ', 'NotMls')
meta[['location']]=meta[['location']].fillna('NotMls')

meta['date'] = pd.to_datetime(meta.date)
meta['date'] = meta['date'].dt.strftime("%Y-%m-%d")

meta[['date_submitted']]=meta[['date']]

metaFilt=meta[meta['date'].notna()]

metaFilt.to_csv(path_or_buf='pythonEdited.tsv', sep='\t', index=False)
