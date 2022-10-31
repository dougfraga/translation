"""
Script to translate text from excel sheets
Author: Douglas Rodrigues
"""

from googletrans import Translator
import pandas as pd


f = pd.read_excel('sheet.xlsx')


for col in ['Key Words', 'Study Area', 'Available data', 'Main Results']: # Columns to translate
    print(col)
    lines = []
    for line in f[col]:
        trans = Translator()
        trans_text = trans.translate(line, src="pt", dest="en")
        lines.append(trans_text.text)
    f[col] = lines

f.to_excel("output.xlsx", index=False)

