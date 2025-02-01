from abc import ABC, abstractmethod


class IDatabaseOperations(ABC):

    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def update(self, record_id, data):
        pass

    @abstractmethod
    def delete(self, record_id):
        pass



class SQLDatabase(IDatabaseOperations):

    def insert(self, data):
        print(f"SQL: Inserting record {data} into relational database.")

    def update(self, record_id, data):
        print(f"SQL: Updating record ID {record_id} with data {data} in relational database.")

    def delete(self, record_id):
        print(f"SQL: Deleting record ID {record_id} from relational database.")



class NoSQLDatabase(IDatabaseOperations):

    def insert(self, data):
        print(f"NoSQL: Inserting document {data} into NoSQL database.")

    def update(self, record_id, data):
        print(f"NoSQL: Updating document ID {record_id} with data {data} in NoSQL database.")

    def delete(self, record_id):
        print(f"NoSQL: Deleting document ID {record_id} from NoSQL database.")



if __name__ == "__main__":
    sql_db = SQLDatabase()
    nosql_db = NoSQLDatabase()

    
    sql_db.insert({"id": 1, "name": "Alice"})
    sql_db.update(1, {"name": "Alice Updated"})
    sql_db.delete(1)

    print("-" * 50)  
    nosql_db.insert({"_id": "abc123", "name": "Bob"})
    nosql_db.update("abc123", {"name": "Bob Updated"})
    nosql_db.delete("abc123")
