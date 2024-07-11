from data_loading import load_data
from data_cleaning import clean_data
from data_visualization import plot_data

def main():
    file_path = 'data/global_temperatures.csv'  # Path to your dataset
    data = load_data(file_path)
    clean_data = clean_data(data)
    plot_data(clean_data)

if __name__ == "__main__":
    main()
