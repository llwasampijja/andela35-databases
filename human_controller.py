from human import Human

class HumanController:

    def add_humans(self):
        human1 = Human(name="Lamech", address="kasubi", age=99, status="single")
        human2 = Human(name="Edward", address="Bolongatiya", age=35, status="Married")
        human3 = Human(name="Dall", address="Nansana", age=16, status="single")
        human4 = Human(name="Lwasa", address="Makerere", age=45, status="Complicated")
        human5 = Human(name="Army", address="Bolon", age=65, status="Divorced")
        human6 = Human(name="Pjoth", address="Mukono", age=23, status="separated")

        human1.add_human()
        human2.add_human()
        human3.add_human()
        human4.add_human()
        human5.add_human()
        human6.add_human()

    def get_human_by_id(self):
        human = Human(human_id=1)
        human.get_human()

    def update_human(self):
        human = Human(human_id=1, name="Lamech", address="kasubi", age=99, status="single")
        human.update_human()

    def delete_human(self):
        human = Human(human_id=4)
        human.delete_human()