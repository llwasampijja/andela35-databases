
from simcard_controller import SimCardController
from human_controller import HumanController
from database_migrations import DatabaseMigration

databaseMigration = DatabaseMigration()

def run_humans():
    humanController = HumanController()
    humanController.add_humans()
    humanController.get_human_by_id()
    humanController.update_human()
    humanController.delete_human()

def run_simcards():
    simcardcontroller = SimCardController()
    simcardcontroller.add_simcards()
    simcardcontroller.get_simcard_by_id()
    simcardcontroller.update_simcard()
    simcardcontroller.delete_simcard()

if __name__ == "__main__":
    databaseMigration.create_db_tables()
    databaseMigration.add_profession_column()
    databaseMigration.add_nationality_column()
    databaseMigration.change_phone_datatype()
    run_humans()
    run_simcards()
