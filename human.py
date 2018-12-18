
from database_migrations import DatabaseMigration
class Human:
    databaseMigration = DatabaseMigration()
    def __init__(self, **kwargs):
        self.human_id = kwargs.get("human_id")
        self.name = kwargs.get("name")
        self.address = kwargs.get("address")
        self.age = kwargs.get("age")
        self.status  = kwargs.get("status")

    def add_human(self):
        return self.databaseMigration.create_human(self.name, self.address, self.age, self.status)


    def get_human(self):
        return self.databaseMigration.get_human(self.human_id)

    def update_human(self):
        return self.databaseMigration.update_human(self.human_id, self.name, self.address, self.age, self.status)

    def delete_human(self):
        return self.databaseMigration.delete_human(self.human_id)