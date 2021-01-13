"""Exploration of python libraries, packages, and methods."""
import pandas as pd 
import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split as tts


class Helper:
    def __init__(self, df):
        self.df = df.copy()

    def null_count(self):
        """Return NaN value counts in passed DataFrame"""
        return self.df.isnull().sum().sum()

    def train_test_split(self, frac):
        """Perform a train test split"""
        return tts(self.df, train_size=frac)

    def randomize(self, seed):
        """Randomize all cells in a DataFrame"""
        return shuffle(self.df, random_state=seed)

