import pandas as pd


class DataFrameGenerator:
    def __init__(self, dataframe):
        if not isinstance(dataframe, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame.")
        self.dataframe = dataframe

    def __iter__(self):
        return self.generator_function()

    def generator_function(self):
        """Generator function to yield rows from the dataframe."""
        try:
            for index, row in self.dataframe.iterrows():
                yield row
        except Exception as e:
            print(f"An error occurred while generating rows: {e}")

    def process_data(self):
        """Process the data using the generator."""
        try:
            for row in self:
                try:
                    processed_data = row['column1'] * row['column2']
                    yield processed_data
                except KeyError as e:
                    print(f"Error processing row: {e}")
                except Exception as e:
                    print(f"An error occurred while processing data: {e}")
        except StopIteration:
            print("Data processing completed.")

    def filter_data(self, condition):
        """Filter the data using a condition and yield the filtered rows."""
        try:
            for row in self:
                try:
                    if condition(row):
                        yield row
                except Exception as e:
                    print(f"Error occurred while filtering data: {e}")
        except StopIteration:
            print("Data filtering completed.")

    def calculate_statistics(self, column_name):
        """Calculate statistics (mean, min, max) for a specified column."""
        try:
            column_values = [row[column_name] for row in self]
            mean_value = sum(column_values) / len(column_values)
            min_value = min(column_values)
            max_value = max(column_values)
            return mean_value, min_value, max_value
        except KeyError as e:
            print(f"Error calculating statistics: {e}")
        except Exception as e:
            print(f"An error occurred while calculating statistics: {e}")


# Create a sample dataframe
df = pd.DataFrame({'column1': [1, 2, 3, 4, 5],
                   'column2': [10, 20, 30, 40, 50]})

# Instantiate the DataFrameGenerator
df_generator = DataFrameGenerator(df)

# Iterate over the generator and print each row
for row in df_generator:
    print(row)

# Process the data using the generator
processed_data_generator = df_generator.process_data()

# Iterate over the processed data generator and print the results
for processed_data in processed_data_generator:
    print(processed_data)

# Create a sample dataframe
df = pd.DataFrame({'column1': [1, 2, 3, 4, 5],
                   'column2': [10, 20, 30, 40, 50],
                   'column3': [100, 200, 300, 400, 500]})

# Instantiate the DataFrameGenerator
df_generator = DataFrameGenerator(df)

# Example usage of filter_data method
filtered_data_generator = df_generator.filter_data(lambda row: row['column1'] > 2)

print("Filtered Data:")
for row in filtered_data_generator:
    print(row)

# Example usage of calculate_statistics method
statistics = df_generator.calculate_statistics('column2')

print("\nStatistics:")
print(f"Mean: {statistics[0]}")
print(f"Min: {statistics[1]}")
print(f"Max: {statistics[2]}")
