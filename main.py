import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Download and inspect the CSV file obtained from World Bank (GDP) & World Health Organization (life expectancy at birth data)
df = pd.read_csv(r"C:\Users\mikek\Desktop\Projects\global_life_expectancy_gdp_analysis\country_year_life_gdp_data.csv")
#df.head()

df.rename(columns={"Life expectancy at birth (years)": "LEABY"}, inplace=True)

df.head()

# Barplot comparing each country's GDP
ax = sns.barplot(x="Country", y="GDP", data=df)
plt.xticks(rotation=90)
plt.show()

# Barplot comparing each country's life expectancy at birth years
ax = sns.barplot(x="Country", y="LEABY", data=df)
plt.xticks(rotation=90)
plt.show()

# Violin plot comparing each country's life expectancy at birth years
fig = plt.subplots(figsize=(15, 10)) 
sns.violinplot(x="Country", y="LEABY", data=df)
plt.show()

# Barplot comparing each country's GDP over time
f, ax = plt.subplots(figsize=(10, 15)) 
ax = sns.barplot(x="Country", y="GDP", hue="Year", data=df)
plt.xticks(rotation=90)
ylabel="GDP in Trillions of U.S. Dollars"
plt.ylabel(ylabel)
plt.show()

# Barplot comparing each country's LEABY over time
f, ax = plt.subplots(figsize=(10, 15)) 
ax = sns.barplot(x="Country", y="LEABY", hue="Year", data=df)
plt.xticks(rotation=90)
plt.ylabel(ylabel)
ax.set(ylabel="Life expectancy at birth in years")
plt.show()

# Grid barplots showing each country's LEABY each year (2000 - 2015)
g1 = sns.FacetGrid(df, col="Year", hue="Country", col_wrap=4)
g1 = (g1.map(plt.scatter, "GDP", "LEABY", edgecolor="w").add_legend())
plt.show()

# Grid line plots showing each country's LEABY over time
g2 = sns.FacetGrid(df, col="Country", col_wrap=3)
g2 = (g2.map(plt.plot, "Year", "LEABY",color="m").add_legend())
plt.show()

# Grid line plots showing each country's GDP over time
g3 = sns.FacetGrid(df, col="Country", col_wrap=3)
g3 = (g3.map(plt.plot, "Year", "GDP").add_legend())
plt.show()
