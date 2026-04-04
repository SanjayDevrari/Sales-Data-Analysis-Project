# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Configure pandas to display float numbers without scientific notation
pd.options.display.float_format = '{:.0f}'.format

# Define the file path for the dataset stored in Google Drive
path = "/content/drive/MyDrive/500000 Sales Records.csv"

# Load the dataset into a pandas DataFrame
df = pd.read_csv(path, encoding="utf-8")

# Display basic information about the dataset
# This includes number of rows, columns, data types, and null values
df.info()

# ------------------------------------------------------------
# Analysis: Identify the Top 5 Countries by Total Revenue
# ------------------------------------------------------------

# Group the data by 'Country'
# Calculate the total revenue for each country
# Sort the results in descending order
# Select the top 5 countries with the highest revenue
top_Country = (
    df.groupby("Country")["Total Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# ------------------------------------------------------------
# Visualization: Bar Chart of Top 5 Revenue-Generating Countries
# ------------------------------------------------------------

# Create a bar chart
plt.bar(
    top_Country.index,
    top_Country.values,
    color=["red", "blue", "green", "orange", "purple"],
    edgecolor="black"
)

# Add chart title and axis labels
plt.title("Top 5 Countries by Total Revenue")
plt.xlabel("Country")
plt.ylabel("Total Revenue")

# Add grid lines on the y-axis for better readability
plt.grid(axis="y")

# Save the chart as a high-resolution image
plt.savefig(
    "/content/drive/MyDrive/top5_country_revenue.png",
    dpi=300,
    bbox_inches="tight"
)

# ------------------------------------------------------------
# Analysis: Determine the Best-Selling Item Types
# ------------------------------------------------------------

# Group the dataset by 'Item Type'
# Calculate the total number of units sold for each item type
# Sort the results in descending order
# Select the top 5 best-selling items
high_saleing_items = (
    df.groupby("Item Type")["Units Sold"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# ------------------------------------------------------------
# Visualization: Bar Chart of Top 5 Best-Selling Items
# ------------------------------------------------------------

# Create a bar chart to visualize the best-selling item types
plt.bar(
    high_saleing_items.index,
    high_saleing_items.values,
    color=["red", "blue", "green", "orange", "purple"],
    edgecolor="black"
)

# Label the y-axis to represent the number of units sold
plt.ylabel("Units Sold")

# Label the x-axis to represent item categories
plt.xlabel("Item Type")

# Save the chart as a high-resolution image
plt.savefig(
    "/content/drive/MyDrive/high_saleing_items.png",
    dpi=300,
    bbox_inches="tight"
)

# Display the chart
plt.show()
