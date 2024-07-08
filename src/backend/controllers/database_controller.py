import src.backend.models.database as database
import json


class DatabaseController:
    def __init__(self, config):
        self.config = config
        self.db = database.Database(db_path=config["database_path"],check_connection=True)

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

    def clear_tables(self):
        self.db.execute_query("DELETE FROM Category;")
        self.db.execute_query("DELETE FROM FAQ;")

    def delete_tables(self):
        self.db.execute_query("DROP TABLE IF EXISTS Category;")
        self.db.execute_query("DROP TABLE IF EXISTS FAQ;")

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

    def export_data_to_json(self, data_by_category):
        data_to_json = {"categories": []}
        for k, v in data_by_category:
            temp_dict = {"name": k, "entries": []}
            for entry in v:
                temp_dict["entries"].append(
                    {"question": entry["questions"], "answer": entry["answer"]}
                )
            data_to_json["categories"].append(temp_dict)

        json_data = json.dumps(data_to_json)
        return json_data

    def fetch_and_export_data(self):
        rows = self.fetch_database()
        organized_data = self.organize_by_category(rows)
        json_data = self.export_data_to_json(organized_data)
        return json_data
