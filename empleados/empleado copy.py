import sqlite3
from sqlite3 import Error

class Empleado:
    def __init__(self):
        self.con = self.sql_connection()

    def sql_connection(self):
        """ Create a connection with SQLite database specified
            by the mytest.db file
        :param con: the connection object
        :return: connection object or Error"""
        try:
            db = sqlite3.connect('empleados/mytest.db')
            return db
        except Error:
            print(Error)

    def create_table(self):
        """ Create the table with given columns
        """
        try:
            cur = self.con.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT,
            department TEXT,
            position TEXT,
            salary REAL,
            date TEXT);''')
            self.con.commit()
            print('The table is created successfully')
        except Error:
            print(Error)

    def insert_data(self, entities):
        """  Insert records into the table
        """
        query = """INSERT INTO employees (id, name, surname, department, position,
                salary, date) VALUES(?,?,?,?,?,?,?)"""

        try:
            cur = self.con.cursor()
            cur.execute(query, entities)
            self.con.commit()
            print("The record added successfully")
        except Error:
            print(Error)

    def add_data(self):
        """ The second method to add records into the table"""
        try:
            cur = self.con.cursor()
            cur.execute("INSERT INTO employees VALUES(2, 'David', 'Anderson', 'IT', 'Dev', 3000, '2020-06-01')")
            cur.execute("INSERT INTO employees VALUES(3, 'Tom', 'Roger', 'IT', 'Manager', 3000, '2018-03-02')")
            cur.execute("INSERT INTO employees VALUES(4, 'Alan', 'Meyer', 'IT', 'Dev', 5000, '2019-04-15')")
            self.con.commit()
            print("The records added successfully")
        except Error:
            print(Error)

    def select_all(self):
        """Selects all rows from the table to display
        """
        try:
            cur = self.con.cursor()
            cur.execute('SELECT * FROM employees')
            rows = cur.fetchall()
            for row in rows:
                print(row)
        except Error:
            print(Error)

    def update_data(self, salary, id):
        """ Update the table with given new values"""
        try:
            cur = self.con.cursor()
            cur.execute("UPDATE employees SET salary = ?  WHERE id = ?", (salary, id))
            self.con.commit()
            print("The record updated successfully")
        except Error:
            print(Error)

    def delete_record(self, surname):
        """ Delete the given record
        """
        query = "DELETE FROM employees WHERE surname = ?;"
        try:
            cur = self.con.cursor()
            cur.execute(query, (surname,))
            self.con.commit()
            print("The record deleted successfully")
        except Error:
            print(Error)
    
    def close_connection(self):
        """ Close the connection """
        self.con.close()

def main():
    
    empleado = Empleado()
    con = empleado.sql_connection()
    print 
    empleado.create_table()
    while True:
        print("\nMenu:")
        print("1. Insertar registro")
        print("2. Añadir datos")
        print("3. Mostrar todos los registros")
        print("4. Actualizar registro")
        print("5. Eliminar registro")
        print("6. Salir")
        
        choice = input("Ingrese el número correspondiente a la acción que desea realizar: ")

        if choice == '1':
            id = int(input("Ingrese el ID: "))
            name = input("Ingrese el nombre: ")
            surname = input("Ingrese el apellido: ")
            department = input("Ingrese el departamento: ")
            position = input("Ingrese el cargo: ")
            salary = float(input("Ingrese el salario: "))
            date = input("Ingrese la fecha (YYYY-MM-DD): ")
            entities = (id, name, surname, department, position, salary, date)
            empleado.insert_data(entities)
        elif choice == '2':
            empleado.add_data()
        elif choice == '3':
            empleado.select_all()
        elif choice == '4':
            id = int(input("Ingrese el ID del registro que desea actualizar: "))
            salary = float(input("Ingrese el nuevo salario: "))
            empleado.update_data(salary, id)
        elif choice == '5':
            surname = input("Ingrese el apellido del registro que desea eliminar: ")
            empleado.delete_record(surname)
        elif choice == '6':
            empleado.close_connection()
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 6.")


main ()