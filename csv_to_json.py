import sys
import pandas as pd

df_clin, df_cna = pd.read_csv(sys.argv[1], sep='\t'), pd.read_csv(sys.argv[2], sep='\t')

df_cna = df_cna.set_index('Hugo_Symbol').T.reset_index().rename(columns={'index':'Sample ID'})

df = pd.merge(df_clin, df_cna)

df.to_json('./test-prad_msk.json', orient='records', lines=True)