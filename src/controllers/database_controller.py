import os

class DatabaseController:
    def __init__(self, database):
        self.db = database

    def export_data_to_json(self, file_name="data.json" ):
        try:
            query = "SELECT * FROM FAQs"  # Assuming the relation will be called FAQs
            self.db.fetch_all(query)
            # Get the path to the current directory where the script is located
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # Construct the path to the data file in the data folder
            file_path = os.path.join(current_dir, f'../../data/{file_name}')
        except Exception as e:
            print(f"Error exporting data to JSON: {e}")
            raise
