import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# You should use combined.csv file, for now it is
# in order to faster read the file
df = pd.read_csv("../data/processed/year-by-year-data/combined.csv")

# data info
# print(df.info())
# stats about the data
# print(df.describe())


# Groups by industry (technology overrepresented)
# plt.figure(figsize=(14, 6))
# sns.countplot(data=df, x="Industry_Tag", hue="target")
# plt.xticks(rotation=45)
# plt.title("Target Distribution by Industry")
# plt.show()
# numeric = df.select_dtypes(include="number")
# correlations = numeric.corr(method="spearman")["target"].sort_values()
# print(correlations)
# plt.show()


### Data cleaning
# print(df.isnull().sum())  # for me it was 0, so i proceed


### Data modeling
# We modeld growth, growth % and target is based on growth %. Done


### Bridge to production

# Problem 1 Nie możemy używać close high i low z tego samego dnia
#  jeśli przewidujemy ruch akcji przed rozpoczęciem sesji.


# Problem 2. Normalizacja: Cena akcji 200 USD nie oznacza,
#  że jest lepsza od akcji za 20 USD.
#  Powinniśmy operować na zmianach procentowych,
# a nie tylko wartościach bezwzględnych.
# Rozwiązanie?1 Warto stworzyć dodatkowe cechy, np. dzienne stopy zwrotu,
#  zmienność cen i średnie kroczące.
