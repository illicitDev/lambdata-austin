import pandas as pd
import helper_functions as hf

kep = pd.read_csv('data/kep_observations.csv')

h = hf.Helper(kep)

train, test = h.train_test_split(.80)

kep_rnd = h.randomize(42)

print('HELPER FUNCTIONS TEST')
print('-------------------------------------------')
print('Null Count Test:', h.null_count())
print()
print('Train: {}, Test: {}'.format(len(train), len(test)))
print()
print(kep_rnd.head())
print('-------------------------------------------')
