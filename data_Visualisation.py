import matplotlib.pyplot as plt
import seaborn as sns

def plot_data(df):
    sns.set(style="whitegrid")

    # Example: Line plot of global temperatures over time
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='Year', y='Temperature', hue='Country')
    plt.title('Global Temperatures Over Time')
    plt.xlabel('Year')
    plt.ylabel('Temperature (°C)')
    plt.savefig('../global_temperatures_over_time.png')
    plt.show()

    # Example: Heatmap of average temperatures by country and year
    pivot_table = df.pivot('Year', 'Country', 'Temperature')
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_table, cmap='coolwarm', annot=False)
    plt.title('Average Temperatures by Country and Year')
    plt.xlabel('Country')
    plt.ylabel('Year')
    plt.savefig('../average_temperatures_heatmap.png')
    plt.show()

    # Example: Distribution plot of temperatures
    plt.figure(figsize=(12, 6))
    sns.histplot(df['Temperature'], kde=True)
    plt.title('Distribution of Global Temperatures')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Frequency')
    plt.savefig('../temperature_distribution.png')
    plt.show()
