import pandas as pd
df = pd.read_csv("world_development_data.csv")
#print(df)

#print(df.head())
#print(df.describe())
#print(df.shape)
#print(df.info())


df["region"] = df["region"].str.strip().str.title().fillna("Unknown")

df_lit_region = df.groupby("region")["literacy_rate"].mean()
#print(df_lit_region)
df_lowest = df_lit_region.idxmin()
#print(f"Lowest is {df_lowest}")

df_region_population = df.groupby("region")["population_thousands"].sum()
#print(df_region_population)
df_high_to_low = df_region_population.sort_values(ascending=False)
#print(df_high_to_low)

#print(df.groupby("region")["country"].count())

df_max_life_expectancy = df.groupby("region")["life_expectancy"].max()
#print(df_max_life_expectancy)
df_gobal_highest = df_max_life_expectancy.idxmax()
#print(f"Global highest is {df_gobal_highest}")

df["country"] = df["country"].str.title().str.strip().fillna("Unknown")
df["gdp_per_capita"] = pd.to_numeric(df["gdp_per_capita"].astype(str).str.replace(",", ""), errors="coerce")

df_1 = df[df["life_expectancy"] > 70]["gdp_per_capita"].mean()
df_2 = df[df["life_expectancy"] < 60]["gdp_per_capita"].mean()
#print(df_1)
#print(df_2)

df["total_gdp"] = (df["gdp_per_capita"] * df["population_thousands"])
# which region has the highest total gdp
print(df.groupby("region")["total_gdp"].sum().idxmax())


#Null data
#print(df.isnull().sum())

# Sub saharan africa
#ssa = df[df["Region"] == "Sub-Saharan Africa"]
#print(ssa.head())

