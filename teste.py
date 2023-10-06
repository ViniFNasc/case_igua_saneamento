import pandas as pd

df = pd.read_csv(fr'streamlit_view\bases_to_view\info_initial.csv',sep=',')

print(df.head(10))