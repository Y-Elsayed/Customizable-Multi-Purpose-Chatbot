import os
import json

class DatabaseController:
    def __init__(self, database):
        self.db = database

    def create_tables(self):
        self.db.execute_query(
            """
                CREATE TABLE IF NOT EXISTS Category (
                    category TEXT PRIMARY KEY
                )
            """
        )
        self.db.execute_query(
            """
                CREATE TABLE IF NOT EXISTS FAQ (
                    category TEXT,
                    question TEXT,
                    answer TEXT,
                    FOREIGN KEY (category) REFERENCES Category(category)
                )
            """
        )

    def fetch_database(self):
        query = """SELECT category, question, answer
            FROM FAQ
            ORDER BY category;
        """
        rows = self.db.fetch_all(query)
        return rows

    def organize_by_category(rows):
        data_by_category = {}
        for category, question, answer in rows:
            if category not in data_by_category:
                data_by_category[category] = []
            data_by_category[category].append({"question": question, "answer": answer})
        return data_by_category

    def export_data_to_json(self, data_by_category={}, file_name="data.json"):
        data_to_json = {"categories": []}
        for k, v in data_by_category:
            temp_dict = {"name": k, "entries": []}
            for entry in v:
                temp_dict["entries"].append(
                    {"question": entry["questions"], "answer": entry["answer"]}
                )
            data_to_json['categories'].append(temp_dict)
            
        json_data = json.dumps(data_to_json)
        return json_data


