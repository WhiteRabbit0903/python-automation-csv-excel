import pandas as pd


def process_file(input_path, output_path):
    """
    Load CSV file, clean data, remove duplicates,
    and export processed file.
    """

    # Load file
    df = pd.read_csv(input_path)

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna("")

    # Example transformation (optional)
    # Convert column names to lowercase
    df.columns = [col.lower() for col in df.columns]

    # Save processed file
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    process_file("input.csv", "output.csv")
