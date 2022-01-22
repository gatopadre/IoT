import psycopg2


class PostgreSQL():
    host = 'localhost'
    database = 'arduino'
    user = 'postgres'
    password = 'Sebastian'
    connection = None
    cursor = None

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()
        except BaseException as exception:
            print('Has ocurred an exception connecting to PostgreSql: {}'.format(exception))

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def run_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def run_insert(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.rowcount


if __name__ == '__main__':
    database = PostgreSQL()
    database.run_query('select * from temperature')
    print('seba')

