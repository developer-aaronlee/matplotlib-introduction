import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0)
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.count())

"""Calculate the total number of post per language."""
posts_per_language = df.groupby(by="TAG").sum(numeric_only=True)
# print(posts_per_language)

"""How many months of data exist per language?"""
languages_exist_months = df.groupby(by="TAG").count()
# print(languages_exist_months)

"""Update DATE column to timestamp datatype"""
# print(type(pd.to_datetime(df.DATE[1])))
df["DATE"] = pd.to_datetime(df["DATE"])
# print(df.head())

"""Create columns for each language"""
reshaped_df = pd.pivot(data=df, index="DATE", columns="TAG", values="POSTS")
# print(reshaped_df.shape)
# print(reshaped_df.head())
# print(reshaped_df.columns)
# print(reshaped_df.count())

"""Replace NaN values with 0"""
reshaped_df.fillna(value=0, inplace=True)
# print(reshaped_df)
# print(reshaped_df.isna().values.any())


"""Create line chart for one language"""
# plt.figure(figsize=(16, 10))
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)
# plt.xlabel("Date", fontsize=12)
# plt.ylabel("Number of Posts", fontsize=12)
# plt.ylim(0, 35000)
# plt.plot(reshaped_df.index, reshaped_df.java)
# plt.show()

"""Create line chart for two languages"""
# plt.figure(figsize=(16, 10))
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)
# plt.xlabel("Date", fontsize=12)
# plt.ylabel("Number of Posts", fontsize=12)
# plt.ylim(0, 35000)
#
# plt.plot(reshaped_df.index, reshaped_df.java)
# plt.plot(reshaped_df.index, reshaped_df.python)
# plt.show()

"""Create line chart for all languages"""
# plt.figure(figsize=(16, 10))
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)
# plt.xlabel("Date", fontsize=12)
# plt.ylabel("Number of Posts", fontsize=12)
# plt.ylim(0, 35000)
#
# for x in reshaped_df.columns:
#     plt.plot(reshaped_df.index, reshaped_df[x], linewidth=3, label=reshaped_df[x].name)
#
# plt.legend(fontsize=15)
# plt.show()

"""Create line chart with rolling mean to smooth time series data"""
roll_df = reshaped_df.rolling(window=12).mean(numeric_only=True)

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Number of Posts", fontsize=12)
plt.ylim(0, 35000)

for x in roll_df.columns:
    plt.plot(roll_df.index, roll_df[x], linewidth=3, label=reshaped_df[x].name)

plt.legend(fontsize=15)
plt.show()

