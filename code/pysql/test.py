import pyodbc

con_str  = 'driver=MySQL ODBC 8.0 Unicode Driver;server=202.28.94.90;database=oracs;uid=CS2_633020430_2;pwd=p123'
def create_table():
    with pyodbc.connect(con_str) as con:
        sql_cmd = """
            create table person(
                id int PRIMARY KEY AUTO_INCREMENT,
                name string(20)
            )
        """
        con.execute(sql_cmd)
        
if __name__ == '__main__':
    create_table()
        