def null_count(df):
    '''Return NaN value counts in passed df'''
    return df.isnull().sum()

def randomize(df, seed):
    '''Randomize all cells in a df'''
    return shuffle(df, random_state=seed)
