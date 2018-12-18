import psycopg2


class DatabaseMigration:

    def __init__(self):
        self.db_name = "andela35"
        self.db_connect = psycopg2.connect(f"dbname={self.db_name} user='andela' \
            host='localhost' password='bootcamp'")
        self.db_connect.autocommit = True
        self.cursor_db = self.db_connect.cursor()

    def create_db_tables(self):
        humans_table_query = """
        CREATE TABLE IF NOT EXISTS humans (\
        human_id serial PRIMARY KEY UNIQUE NOT NULL, \
        name varchar NOT NULL, \
        address varchar NOT NULL, \
        age int NOT NULL, \
        status varchar NOT NULL)
        """

        simcards_table_querry = """
        CREATE TABLE IF NOT EXISTS simcards (\
        simcard_id serial PRIMARY KEY UNIQUE, \
        name int REFERENCES humans(human_id) ON DELETE RESTRICT NOT NULL,\
        phone_number int UNIQUE NOT NULL, \
        serial int UNIQUE NOT NULL, \
        service_provider varchar NOT NULL, \
        is_active BOOL NOT NULL, \
        human_id int references humans(human_id) ON DELETE RESTRICT NOT NULL)
        """

        self.cursor_db.execute(humans_table_query)
        self.cursor_db.execute(simcards_table_querry)

    def add_profession_column(self):
        sql_query = """ALTER TABLE humans ADD COLUMN IF NOT EXISTS profession varchar;"""
        self.cursor_db.execute(sql_query)

    def add_nationality_column(self):
        sql_query = """ALTER TABLE humans ADD COLUMN IF NOT EXISTS nationality varchar;"""
        self.cursor_db.execute(sql_query)

    def change_phone_datatype(self):
        sql_query = """ALTER TABLE simcards ALTER COLUMN phone_number TYPE bigint;"""
        self.cursor_db.execute(sql_query)

    def create_human(self, name, address, age, status):
        sql_query = f""" INSERT INTO humans (name, address, age, status) \
            VALUES ('{name}', '{address}', '{age}', '{status}')
            """
        self.cursor_db.execute(sql_query)
        return {"message": "Success"}

    def get_human(self, human_id):
        sql_query = f""" SELECT * FROM humans WHERE human_id = {human_id}"""
        self.cursor_db.execute(sql_query)
        result = self.cursor_db.fetchall()
        return result


    def update_human(self, human_id, name, address, age, status):
        sql_query = f"""UPDATE humans SET name = '{name}', address = '{address}', \
        age = '{age}', status = '{status}' WHERE human_id = '{human_id}'"""
        self.cursor_db.execute(sql_query)
        return {"message": "Success"}

    def delete_human(self, human_id):
        sql_query = f"""DELETE FROM humans WHERE human_id = '{human_id}'"""
        self.cursor_db.execute(sql_query)
        return {"message": "Success"}

    def create_simcard(self, name, phone_number, serial, service_provider, is_active, human_id):
        sql_query = f""" INSERT INTO simcards (name, phone_number, serial, service_provider, is_active, human_id) \
            VALUES ('{name}','{phone_number}', '{serial}', '{service_provider}', '{is_active}', '{human_id}')
            """
        self.cursor_db.execute(sql_query)
        return {"message": "Success"}

    def get_simcard(self, simcard_id):
        sql_query = f""" SELECT * FROM simcards WHERE simcard_id = {simcard_id}"""
        self.cursor_db.execute(sql_query)
        result = self.cursor_db.fetchall()
        return result

    def update_simcard(self, simcard_id, name, phone_number, serial, service_provider, is_active, human_id):
        sql_query = f"""UPDATE simcards SET name = '{name}', phone_number = '{phone_number}', \
        serial = '{serial}', service_provider = '{service_provider}', is_active = '{is_active}', human_id = '{human_id}'  WHERE simcard_id = '{simcard_id}'"""
        self.cursor_db.execute(sql_query)
        return {"message": "Success"}

    def delete_simcard(self, simcard_id):
        sql_query = f"""DELETE FROM simcards WHERE simcard_id = '{simcard_id}''"""
        self.cursor_db.execute(sql_query)
        return {"message": "Success"}
