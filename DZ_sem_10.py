
import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.loc[data['whoAmI'] == 'robot', 'robots_class'] = '1'
data.loc[data['whoAmI'] != 'robot', 'robots_class'] = '0'
data.loc[data['whoAmI'] == 'human', 'humans_class'] = '1'
data.loc[data['whoAmI'] != 'human', 'humans_class'] = '0'
data.head(n=20) 
print(data)