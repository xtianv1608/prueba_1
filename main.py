import pandas as pd
import numpy as np

def detectar_nulos(df):
	return df.isnull().sum()

def calcular_promedios(df):
	return df.mean()

def calcular_tipos(df):
	for col in df.iteritems():
		print(col.dtype)