# Pandas: Strip whitespace from Column Headers in DataFrame

import pandas as pd


df = pd.DataFrame({
    '  name   ': ['Alice', 'Bobby', 'Carl', 'Dan'],
    ' experience   ': [1, 3, 5, 7],
    'salary    ': [175.1, 179.4, 190.3, 199.3],
})

print(df)

df = df.rename(columns=lambda x: x.strip())

print('-' * 50)

print(df)
