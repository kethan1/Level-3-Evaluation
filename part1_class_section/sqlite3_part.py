"""

homework: check joins, add union

SQLite3
1.	Give an example of each SQL query with Python
a.	Creating a table ✔
b.	Creating a record ✔
c.	Read all records in a table ✔
d.	Display data with column names ✔
e.	Display all tables in the database ✔
f.	Read a specific record in the table ✔
g.	Update all records in the table ✔
h.	Delete a table ✔
i.	Group by ✔
j.	Max, min ✔
k.	Joining tables - inner join, left join (required), outer join (extra credit)
l.	Update a specific record in the table ✔
m.	Deleting a specific record ✔
n.	Delete the database ✔
o.	Order by ✔
p.	Limit ✔

Extra Credit:
q.	Use a Python class for SQLite3 database with the listed functions
"""

"""
Add formatting flag
"""

import sqlite3
import os

class SQLite3_Class:
    def __init__(self, db_path):
        self.sqlite3_database = sqlite3.connect(db_path)
        self.db_path = db_path

    def create_table(self, table_name, list_of_types):
        sqlite3_connection = self.sqlite3_database.cursor()
        str_of_types = str(tuple(list_of_types)).replace("'", "")
        str_to_execute = f"CREATE TABLE {table_name} {str_of_types}"
        sqlite3_connection.execute(str_to_execute)
        sqlite3_connection.close()
    
    def delete_table(self, table_name):
        sqlite3_connection = self.sqlite3_database.cursor()
        str_to_execute = f"DROP TABLE {table_name}"
        sqlite3_connection.execute(str_to_execute)
        sqlite3_connection.close()

    def insert(self, table_name, values):
        sqlite3_connection = self.sqlite3_database.cursor()
        sqlite3_connection.execute(f"INSERT INTO %s %s VALUES {values}" %(table_name, str(self.column_names(table_name)).replace("'", "").replace('"', "").replace("[", "(").replace("]", ")")))
        sqlite3_connection.close()

    def insert_many(self, table_name, values):
        sqlite3_connection = self.sqlite3_database.cursor()
        for column in values:
            sqlite3_connection.execute(f"INSERT INTO %s %s VALUES {column}" %(table_name, str(self.column_names(table_name)).replace("'", "").replace('"', "").replace("[", "(").replace("]", ")")))
        sqlite3_connection.close()

    def select_all(self, table_name, column_names=False, formatted=False, show_column_nums=False):
        sqlite3_connection = self.sqlite3_database.cursor()
        output = sqlite3_connection.execute("SELECT * FROM %s" % table_name)
        output_final = []
        for i in output:
            output_final.append(i)
        sqlite3_connection.close()
        if column_names:
            output_final.insert(0, tuple(self.column_names(table_name)))
        if not formatted:
            if show_column_nums:
                print(len(output_final))
            return output_final
        else:
            for each in output_final:
                print('|'.join([str(i) for i in each]))
            if show_column_nums:
                print(len(output_final))

    def select_specific(self, table_name, columns="*", query="", order_by="", limit="", join=None, column_names=False, formatted=False, show_column_nums=False):
        sqlite3_connection = self.sqlite3_database.cursor()
        conditions = []
        if join != None and not isinstance(join, dict):
            raise Exception("Please Pass Dict to Join")
        if query != "":
            conditions.append("WHERE %s" %query)
        if order_by != "":
            conditions.append("ORDER BY %s" %order_by)
        if limit != "":
            conditions.append("LIMIT "+str(limit))
        if join != None:
            if len(join["tables"]) == 2:
                if join["type"].upper() == "INNER":
                    tables_join_copy = join['tables'].copy()
                    tables_join_copy.remove(table_name)
                    # SELECT column_name(s) FROM table1 INNER JOIN table2 ON table1.column_name=table2.column_name;
                    conditions.append(f"INNER JOIN {tables_join_copy[0]} ON {table_name}.{join['column_name']}={tables_join_copy[0]}.{join['column_name']}")
                elif join["type"].upper() == "LEFT":
                    tables_join_copy = join['tables'].copy()
                    tables_join_copy.remove(table_name)
                    # SELECT column_name(s) FROM table1 LEFT JOIN table2 ON table1.column_name=table2.column;
                    conditions.append(f"LEFT JOIN {tables_join_copy[0]} ON {table_name}.{join['column_name']}={tables_join_copy[0]}.{join['column_name']}")
            else:
                raise Exception("Please Pass 2 Tables to Joins")
        to_execute = f"SELECT {columns} FROM {table_name} {' '.join(conditions)}"
        output = sqlite3_connection.execute(to_execute)
        output_final = []
        for i in output:
            output_final.append(i)
        sqlite3_connection.close()
        if column_names: 
                output_final.insert(0, tuple(self.column_names(table_name)))
        if not formatted:
            if show_column_nums:
                print(len(output_final))
            return output_final
        else:
            for each in output_final:
                print('|'.join([str(i) for i in each]))
            if show_column_nums:
                print(len(output_final))

    def group_by(self, table_name, columns, query="", order_by="", group_by="", limit="", column_names=False, formatted=False, show_column_nums=False):
        sqlite3_connection = self.sqlite3_database.cursor()
        conditions = []
        if isinstance(columns, list):
            columns = ', '.join(columns)
        if query != "":
            conditions.append("WHERE %s" %query)
        if group_by != "":
            conditions.append("GROUP BY %s" %group_by)
        if order_by != "":
            conditions.append("ORDER BY %s" %order_by)
        if limit != "":
            conditions.append("LIMIT "+str(limit))
        to_execute = f"SELECT {columns} FROM {table_name} {' '.join(conditions)}"
        output = sqlite3_connection.execute(to_execute)
        output_final = []
        for i in output:
            output_final.append(i)
        if column_names:
            output_final.insert(0, tuple(self.column_names(table_name)))
        sqlite3_connection.close()
        if not formatted:
            if show_column_nums:
                print(len(output_final))
            return output_final
        else:
            for each in output_final:
                print('|'.join([str(i) for i in each]))

    def minimum(self, table_name, columns, query="", limit="", column_names=False):
        sqlite3_connection = self.sqlite3_database.cursor()
        if isinstance(columns, list):
            columns = ', '.join(columns)
        conditions = []
        if query != "":
            conditions.append("WHERE %s" %query)
        if limit != "":
            conditions.append("LIMIT "+str(limit))
        to_execute = f"SELECT min({columns}) FROM {table_name} {' '.join(conditions)}"
        output = sqlite3_connection.execute(to_execute)
        for i in output:
            output_final = i[0]
        sqlite3_connection.close()
        if column_names:
            output_final.insert(0, tuple(self.column_names(table_name)))
        return output_final

    def maximum(self, table_name, columns, query="", limit="", group_by="", column_names=False):
        sqlite3_connection = self.sqlite3_database.cursor()
        if isinstance(columns, list):
            columns = ', '.join(columns)
        conditions = []
        if query != "":
            conditions.append("WHERE %s" %query)
        if group_by != "":
            conditions.append("GROUP BY %s" %group_by)
        if limit != "":
            conditions.append("LIMIT "+str(limit))
        to_execute = f"SELECT max({columns}) FROM {table_name} {' '.join(conditions)}"
        output = sqlite3_connection.execute(to_execute)
        for i in output:
            output_final = i[0]
        sqlite3_connection.close()
        if column_names:
            output_final.insert(0, tuple(self.column_names(table_name)))
        return output_final

    def update_all(self, table_name, to_change):
        if not isinstance(to_change, dict):
            raise Exception("Please Pass Dict")
        change_final = []
        for key, value in to_change.items():
            change_final.append(f"{key}={value}")
        sqlite3_connection = self.sqlite3_database.cursor()
        columns = [i[0] for i in sqlite3_connection.execute(f"UPDATE {table_name} SET {', '.join(change_final)}")]
        sqlite3_connection.close()

    def update_specific(self, table_name, to_change, query=""):
        if not isinstance(to_change, dict):
            raise Exception("Please Pass Dict")
        change_final = []
        for key, value in to_change.items():
            change_final.append(f"{key}={value}")
        sqlite3_connection = self.sqlite3_database.cursor()
        x = ""
        if query != "":
            x = "WHERE " + query
        sqlite3_connection.execute(f"UPDATE {table_name} SET {', '.join(change_final)} {x}")
        sqlite3_connection.close()

    def delete(self, table_name, query):
        sqlite3_connection = self.sqlite3_database.cursor()
        sqlite3_connection.execute(f"DELETE FROM {table_name} WHERE {query}")
        sqlite3_connection.close()

    def column_names(self, table_name, formatted=False):
        sqlite3_connection = self.sqlite3_database.cursor()
        columns = [i[0] for i in sqlite3_connection.execute("SELECT * FROM %s" % table_name).description]
        sqlite3_connection.close()
        if not formatted:
            return columns
        else:
            for column in columns:
                print(column)

    def get_tables(self, formatted=False):
        sqlite3_connection = self.sqlite3_database.cursor()
        tables = sqlite3_connection.execute("SELECT name FROM sqlite_master WHERE type='table';")
        if not formatted:
            tables_final = []
            for table in tables:
                tables_final.append(table)
            sqlite3_connection.close()
            return tables_final
        else:
            for table in tables:
                print(table[0])
            sqlite3_connection.close()

    def custom_execute_command(self, query, output=True):
        sqlite3_connection = self.sqlite3_database.cursor()
        tables = sqlite3_connection.execute(query)
        if output:
            output_final = []
            for i in tables:
                output_final.append(i)
            sqlite3_connection.close()
            return output_final

    def rollback(self):
        self.sqlite3_database.rollback()

    def commit(self):
        self.sqlite3_database.commit()

    def close(self):
        self.sqlite3_database.close()
        self.closed = True

    def delete_database(self):
        if not self.closed:
            self.commit()
            self.close()
        os.remove(self.db_path)
        self.sqlite3_database = ""
        self.db_path = ""

    def switch_database(self, db_path, changes="commit"):
        if not self.closed:
            if changes == "commit":
                self.commit()
            else:
                self.rollback()
            self.close()
        self.sqlite3_database = sqlite3.connect(db_path)
        self.db_path = db_path

sqlite3_class1 = SQLite3_Class("sqlite3_part.db")
print("Current Tables:")
print(sqlite3_class1.get_tables())
sqlite3_class1.get_tables(formatted=True)

print("\nColumn Names from Student:")
print(sqlite3_class1.column_names("Student"))
sqlite3_class1.column_names("Student", formatted=True)

print("\nAll Values from Student with Column Names")
print(sqlite3_class1.select_all("Student", column_names=True))
sqlite3_class1.select_all("Student", column_names=True, formatted=True, show_column_nums=True)

print("\nAll Values from Student")
print(sqlite3_class1.select_all("Student"))
sqlite3_class1.select_all("Student", formatted=True, show_column_nums=True)

print("\nAll Values where country='India' with Column Names")
print(sqlite3_class1.select_specific("Student", "*", "Country='India'", column_names=True))
sqlite3_class1.select_specific("Student", "*", "Country='India'", column_names=True, formatted=True, show_column_nums=True)

print("\nGPA where country='India'")
print(sqlite3_class1.select_specific("Student", "GPA", "country='India'"))
sqlite3_class1.select_specific("Student", "GPA", "country='India'", formatted=True, show_column_nums=True)

print("\nAll Values from Student SELECT StudentName where GPA < 3.0 order by num1 DESC")
print(sqlite3_class1.select_specific("Student", "StudentName", query="GPA < 3.0", order_by="GPA DESC"))
sqlite3_class1.select_specific("Student", "StudentName", query="GPA < 3.0", order_by="GPA DESC", formatted=True, show_column_nums=True)

print("\nAll Values from Student SELECT GPA where GPA < 3.0 order by GPA ASC limit 3")
print(sqlite3_class1.select_specific("Student", "*", query="GPA < 3.0", order_by="GPA ASC", limit="1"))
sqlite3_class1.select_specific("Student", "*", query="GPA < 3.0", order_by="GPA ASC", limit="3", formatted=True, show_column_nums=True)

print("\nSum from GPA group by GPA")
print(sqlite3_class1.group_by("Student", "GPA, sum(GPA)", group_by="GPA"))
sqlite3_class1.group_by("Student", "GPA, sum(GPA)", group_by="GPA", formatted=True, show_column_nums=True)

print("\nMinimum of GPA from Student")
print(sqlite3_class1.minimum("Student", "GPA"))

print("\nMaximum of GPA from Student")
print(sqlite3_class1.maximum("Student", "GPA"))

print("\nMaximum of GPA from Student group by GPA")
# Look Into Incorrect
print(sqlite3_class1.maximum("Student", "GPA", group_by="GPA"))
# sqlite3_class1.update_specific("Student", {"GPA": 2.94}, "GPA=3.21")

# print("\nSelect all from Student with column names")
# print(sqlite3_class1.select_all("Student", column_names=True))
# sqlite3_class1.select_all("Student", column_names=True, formatted=True, show_column_nums=True)

# sqlite3_class1.delete("Student", "StudentName='Ricky Ma'")

# print("\nSelect all from Student with column names after delete StudentName='Ricky Ma'")
# print(sqlite3_class1.select_all("Student", column_names=True))
# sqlite3_class1.select_all("Student", column_names=True, formatted=True, show_column_nums=True)

print("\nInner join Student and Student2")
print(sqlite3_class1.select_specific("Student", join={"type": "INNER", "tables": ["Student", "Student2"], "column_name": "City"}))
sqlite3_class1.select_specific("Student", join={"type": "INNER", "tables": ["Student", "Student2"], "column_name": "City"}, formatted=True, show_column_nums=True)
print("\nLeft Join Student and Student2")
print(sqlite3_class1.select_specific("Student", join={"type": "LEFT", "tables": ["Student2", "Student"], "column_name": "City"}))
sqlite3_class1.select_specific("Student", join={"type": "LEFT", "tables": ["Student2", "Student"], "column_name": "City"}, formatted=True, show_column_nums=True)

# import subprocess
# import shlex
# print("\nInner Join From Shell")
# innerJoinFromShell = subprocess.Popen(shlex.split(r"sqlite3 'C:\Users\ketha\Documents\Kethan\Youngwonks\Evaluations\Level 3\part1_class_section\sqlite3_part.db' 'SELECT * FROM Student INNER JOIN Student2 on Student.city = Student2.city'"))
# innerJoinFromShell.communicate()
# print("\nLeft Join From Shell")
# leftJoinFromShell = subprocess.Popen(shlex.split(r"sqlite3 'C:\Users\ketha\Documents\Kethan\Youngwonks\Evaluations\Level 3\part1_class_section\sqlite3_part.db' 'SELECT * FROM Student LEFT JOIN Student2 on Student.city = Student2.city'"))
# leftJoinFromShell.communicate()

# sqlite3_class1.create_table("test_table", ["num1 INTEGER", "num2 INTEGER"])
# sqlite3_class1.insert("test_table", (1,2))
# sqlite3_class1.insert("test_table", (9,221))
# sqlite3_class1.insert("test_table", (21,2))
# print("Current Tables:")
# print(sqlite3_class1.get_tables())
# sqlite3_class1.get_tables(formatted=True)
# print("\nColumn Names from test_table:")
# print(sqlite3_class1.column_names("test_table"))
# sqlite3_class1.column_names("test_table", formatted=True)
# print("\nAll Values from test_table with Column Names")
# print(sqlite3_class1.select_all("test_table", column_names=True))
# sqlite3_class1.select_all("test_table", column_names=True, formatted=True)
# print("\nAll Values from test_table")
# sqlite3_class1.select_all("test_table", formatted=True)
# print("\nAll Values from num1 where num2 > 100 with Column Names")
# print(sqlite3_class1.select_specific("test_table", "num1", "num2 > 100", column_names=True))
# sqlite3_class1.select_specific("test_table", "num1", "num2 > 100", column_names=True, formatted=True)
# print("\nAll Values from num1 where num2 > 100")
# print(sqlite3_class1.select_specific("test_table", "num1", "num2 > 100"))
# sqlite3_class1.select_specific("test_table", "num1", "num2 > 100", formatted=True)
# print("\nAll Values from num1 where num2 < 100")
# print(sqlite3_class1.select_specific("test_table", "num1", query="num2 < 100"))
# sqlite3_class1.select_specific("test_table", "num1", query="num2 < 100", formatted=True)
# print("\nAll Values from num1 where num2 < 100 limit 1")
# print(sqlite3_class1.select_specific("test_table", "num1", query="num2 < 100", limit="1"))
# sqlite3_class1.select_specific("test_table", "num1", query="num2 < 100", limit="1", formatted=True)
# print("\nAll Values from num1 where num2 < 100 order by num1 ASC")
# print(sqlite3_class1.select_specific("test_table", "num1", query="num2 < 100", order_by="num1 ASC"))
# sqlite3_class1.select_specific("test_table", "num1", query="num2 < 100", order_by="num1 ASC", formatted=True)
# print("\nAll Values from num1 where num2 < 100 order by num1 DESC")
# print(sqlite3_class1.select_specific("test_table", "num1", query="num2 < 100", order_by="num1 DESC"))
# sqlite3_class1.select_specific("test_table", "num1", query="num2 < 100", order_by="num1 DESC", formatted=True)
# print("\nAll Values from num1 where num2 < 100 order by num1 ASC limit 1")
# print(sqlite3_class1.select_specific("test_table", "num1", query="num2 < 100", order_by="num1 ASC", limit="1"))
# sqlite3_class1.select_specific("test_table", "num1", query="num2 < 100", order_by="num1 ASC", limit="1", formatted=True)
# print("\nSum from num2 group by num2")
# print(sqlite3_class1.group_by("test_table", "num2, sum(num1)", group_by="num2"))
# sqlite3_class1.group_by("test_table", "num2, sum(num1)", group_by="num2", formatted=True)
# print("\nMinimum of num1 from test_table")
# print(sqlite3_class1.minimum("test_table", "num1"))
# print("\nMaximum of num2 from test_table")
# print(sqlite3_class1.maximum("test_table", "num2"))
# print("\nMaximum of num2 from test_table group by num2")
# print(sqlite3_class1.maximum("test_table", "num2", group_by="num2"))
# sqlite3_class1.update_specific("test_table", {"num1": 300}, "num1=1")
# print("\nSelect all from test_table with column names")
# print(sqlite3_class1.select_all("test_table", column_names=True))
# sqlite3_class1.select_all("test_table", column_names=True, formatted=True)
# sqlite3_class1.delete("test_table", "num1=300")
# print("\nSelect all from test_table with column names after delete num1=300")
# print(sqlite3_class1.select_all("test_table", column_names=True))
# sqlite3_class1.select_all("test_table", column_names=True, formatted=True)
# sqlite3_class1.create_table("test_table2", ["num1 INTEGER", "num2 INTEGER"])
# sqlite3_class1.insert("test_table2", (39,17))
# sqlite3_class1.insert("test_table2", (9,2121))
# sqlite3_class1.insert("test_table2", (2123,41))
# sqlite3_class1.insert("test_table", (2123,4))
# print("\nInner join test_table and test_table2")
# print(sqlite3_class1.select_specific("test_table", join={"type": "INNER", "tables": ["test_table", "test_table2"], "column_name": "num1"}))
# sqlite3_class1.select_specific("test_table", join={"type": "INNER", "tables": ["test_table", "test_table2"], "column_name": "num1"}, formatted=True)
# print("\nLeft Join test_table and test_table2")
# print(sqlite3_class1.select_specific("test_table", join={"type": "LEFT", "tables": ["test_table2", "test_table"], "column_name": "num1"}))
# sqlite3_class1.select_specific("test_table", join={"type": "LEFT", "tables": ["test_table2", "test_table"], "column_name": "num1"}, formatted=True)
# sqlite3_class1.delete_table("test_table")
# print("Get all Tables after Deleting test_table")
# print(sqlite3_class1.get_tables())
# sqlite3_class1.get_tables(formatted=True)
sqlite3_class1.commit()
sqlite3_class1.close()
# sqlite3_class1.delete_database()
