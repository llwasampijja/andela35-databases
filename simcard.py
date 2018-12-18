from human import Human
from database_migrations import DatabaseMigration
class SimCard (Human):
    databaseMigration = DatabaseMigration()
    def __init__(self, **kwargs):
        super(SimCard, self).__init__(**kwargs)
        self.simcard_id = kwargs.get("simcard_id")
        self.phone_number = kwargs.get("phone_number")
        self.serial = kwargs.get("serial")
        self.service_provider = kwargs.get("service_provider")
        self.is_active = kwargs.get("is_active")

    def add_simcard(self):
        return self.databaseMigration.create_simcard(self.name, self.phone_number, self.serial,\
             self.service_provider, self.is_active, self.human_id)

    def get_simcard(self):
        return self.databaseMigration.get_simcard(self.simcard_id)

    def update_simcard(self):
        return self.databaseMigration.update_simcard(self.simcard_id, self.name, self.phone_number, \
               self.serial, self.service_provider, self.is_active, self.human_id)

    def delete_simcard(self):
        return self.databaseMigration.delete_simcard(self.simcard_id) 
