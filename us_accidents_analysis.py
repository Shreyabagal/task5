import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

file_path = 'Highway-Rail_Grade_Crossing_Accident_Data.csv'
df = pd.read_csv(file_path)

os.makedirs("images", exist_ok=True)

print("Columns in dataset:", df.columns.tolist())

if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Day_of_Week'] = df['Date'].dt.day_name()
else:
    print("Column 'Date' not found.")

if 'Time' in df.columns:
    df['Hour'] = pd.to_datetime(df['Time'], errors='coerce').dt.hour
else:
    print("Column 'Time' not found.")

if 'Hour' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Hour', data=df, palette='viridis')
    plt.title('Accidents by Hour')
    plt.xlabel('Hour')
    plt.ylabel('Number of Accidents')
    plt.tight_layout()
    plt.savefig('images/accidents_by_hour.png')
    plt.close()

if 'Day_of_Week' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Day_of_Week', data=df,
                  order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                  palette='Set2')
    plt.title('Accidents by Day of the Week')
    plt.xlabel('Day')
    plt.ylabel('Number of Accidents')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('images/accidents_by_day.png')
    plt.close()

possible_city_cols = ['City', 'County', 'Location']

for col in possible_city_cols:
    if col in df.columns:
        plt.figure(figsize=(12, 6))
        df[col].value_counts().head(10).plot(kind='bar', color='skyblue')
        plt.title(f'Top 10 {col}s with Most Accidents')
        plt.xlabel(col)
        plt.ylabel('Accidents')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f'images/top_{col.lower()}s.png')
        plt.close()

for type_col in ['Type', 'Accident Type', 'Cause']:
    if type_col in df.columns:
        plt.figure(figsize=(10, 6))
        df[type_col].value_counts().head(10).plot(kind='bar', color='salmon')
        plt.title(f'Accidents by {type_col}')
        plt.xlabel(type_col)
        plt.ylabel('Count')
        plt.tight_layout()
        plt.savefig(f'images/accidents_by_{type_col.lower().replace(" ", "_")}.png')
        plt.close()


