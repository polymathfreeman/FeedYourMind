# Importing pandas
import pandas as pd

sample_series = pd.Series()
print(sample_series)

# Creating a Pandas series with data
sample_series = pd.Series(['Nik', 'Kate', 'Jane', 'Jim'])
print(sample_series)

# Creating a Pandas Series with an Index
sample_series = pd.Series(data = [33, 32, 40, 20], index=['Nik', 'Kate', 'Jane', 'Jim'])
print(sample_series)

# Accessing a Pandas series item
print(sample_series['Nik'])


# Creating a DataFrame from Scratch
df = pd.DataFrame({
    'Name': ['Nik', 'Kate', 'Jane', 'Evan', 'Jim', 'Moe', 'Samira'],
    'Age': [33, 32, 20, 40, 22, 50, 76]
})

print(df)

# Returning the first five records of a Pandas DataFrame
print(df.head())

# Returning the first two records of a Pandas DataFrame
print(df.head(2))

# Returning the last three records of a Pandas DataFrame
print(df.tail(3))

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print(df)
print(df["Age"])
ages = pd.Series([22, 35, 58], name="Age")
print(ages)
ages2 = df["Age"]
print(ages2)
print(df["Age"].max())
print(ages.max())
print(df.describe())

titanic = pd.read_csv("titanic.csv")