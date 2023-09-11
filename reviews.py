# import pandas
import pandas as pd

#read in data
reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")

#create new dataframe grouped by unique country count and average reviews
summary = reviews.groupby("country").agg({
    "country": "count", "points": "mean"}).round(1)

summary = summary.rename(columns = {"country":"count"})
summary = summary.sort_values("count", ascending = False)

#create data frame
summary_df = pd.DataFrame(summary)

#dataframe to csv

summary_df.to_csv("data/reviews-per-country.csv")