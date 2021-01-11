def null_count(df):
    '''Return NaN value counts in passed DataFrame'''
    return df.isnull().sum()

def randomize(df, seed):
    '''Randomize all cells in a DataFrame'''
    return shuffle(df, random_state=seed)
