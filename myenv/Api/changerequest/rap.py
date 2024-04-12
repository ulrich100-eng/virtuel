import pandas as pd

df_list = pd.read_html('rapport_tests.html')

df =  pd.concat(df_list)



df.to_excel('test_results.xlsx', index=False)