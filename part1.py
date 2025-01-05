import pandas as pd

# data = [1, 2, 3, 4, 5]
# series = pd.Series(data)
# print(series)

data = {
    'Name' : ['Alice', 'Bob', 'Roma', 'Anna'],
    'Age' : [23, 45, 17, 24],
    'City' : ['New York', 'LA', 'Chicago', 'Maskva']
}

df = pd.DataFrame(data)
#
# print(df)

# df = pd.read_csv('World-happiness-report-2024.csv')
#
# print(df[df['Healthy life expectancy']>0.7])

# df = pd.read_csv('hh.csv')
#
# df = pd.read_csv('animal.csv')
#
# # df['test'] = [new for new in range(29)]
# #
# # print(df)
#
# # df.drop(28, axis=0, inplace=True)
#
# print(df)
#
# group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
#
# # df.dropna(inplace=True)
# # df.fillna(0, inplace=True)
#
# print(group)

df.to_csv('output.csv', index=False)