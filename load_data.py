import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df= pd.read_csv('auto_insurance.csv')
print(df.head())
print(df.info())
#
# print("\n Column Names:")
# print(df.columns)
#
# print("\n Shape of data (Rows, Columns):")
# print(df.shape)
#
# print("\n Missing Values:")
# print(df.isnull().sum())
#
# print("\n Fraud Reported value Counts")
# print(df["fraud_reported"].value_counts())
#
# print("\n Data Types:")
# print(df.dtypes)
#
# print("\nUnique values in 'property_damage':")
# print(df["property_damage"].unique())
#
# print("\nUnique values in 'police_report_available':")
# print(df["police_report_available"].unique())
#
df["property_damage"] = df["property_damage"].replace("?", "Unknown")
df["police_report_available"] = df["police_report_available"].replace("?", "Unknown")
print(df["property_damage"].unique())
print(df["police_report_available"].unique())
#

df.drop("_c39", axis=1, inplace=True)

df["incident_date"] = pd.to_datetime(df["incident_date"])

df["policy_bind_date"] = pd.to_datetime(df["policy_bind_date"])

# print("\n Data Types:")
# print(df.dtypes)

df["authorities_contacted"]=df["authorities_contacted"].fillna("Unknown")

print("\n Missing Values:")
print(df.isnull().sum())

print("\nUnique values in 'property_damage':")
print(df["property_damage"].unique())


print("\nUnique values in 'police_report_available':")
print(df["police_report_available"].unique())

print("\n Fraud reported Value counts")
print(df["fraud_reported"].value_counts())

#creating chart
sns.countplot(x="fraud_reported", data=df)

plt.title("Fraud vs. Non-Fraud Claims")
plt.xlabel("Fraud Reported")
plt.ylabel("Number of Claims")
plt.show()

# Create a grouped bar chart: incident_type vs fraud_reported
plt.figure(figsize=(8, 5))
sns.countplot(x="incident_type", hue="fraud_reported", data=df)
plt.title("Fraud Distribution by Incident Type")
plt.xlabel("Incident Type")
plt.ylabel("Number of Claims")
#plt.xticks(rotation=45)
plt.legend(title="Fraud Reported")
plt.tight_layout()
plt.show()

#Total Claim Amount vs Fraud
plt.figure(figsize=(7, 5))
sns.boxplot(x="fraud_reported", y="total_claim_amount", data=df)
plt.title("Claim Amounts by Fraud Status")
plt.xlabel("Fraud Reported")
plt.ylabel("Total Claim Amount")
plt.show()

#Histogram of Claim Amounts
plt.figure(figsize=(7, 5))
sns.histplot(df["total_claim_amount"], bins=30, kde=True)
plt.title("Distribution of Total Claim Amounts")
plt.xlabel("Total Claim Amount")
plt.ylabel("Frequency")
plt.show()

#Total claim Amount Box plot
plt.figure(figsize=(7, 5))
sns.boxplot(x="fraud_reported", y="total_claim_amount", data=df)
plt.title("Claim Amounts by Fraud Status")
plt.xlabel("Fraud Reported")
plt.ylabel("Total Claim Amount")
plt.show()
