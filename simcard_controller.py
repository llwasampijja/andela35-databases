from simcard import SimCard
class SimCardController:
    def add_simcards(self):
        simcard1 = SimCard(name=2, phone_number=775961853, serial=7483738, service_provider="mtn", is_active=True, human_id=2)
        simcard2 = SimCard(name=3, phone_number=715961853, serial=42455232, service_provider="mtn", is_active=True, human_id=3)
        simcard3 = SimCard(name=1, phone_number=794961853, serial=6745646, service_provider="orange", is_active=False, human_id=1)
        simcard4 = SimCard(name=2, phone_number=744961853, serial=56456456, service_provider="mtn", is_active=True, human_id=2)
        simcard5 = SimCard(name=3, phone_number=755961853, serial=7565756, service_provider="mtn", is_active=True, human_id=3)
        simcard6 = SimCard(name=5, phone_number=751787037, serial=8453266, service_provider="mtn", is_active=True, human_id=5)

        simcard1.add_simcard()
        simcard2.add_simcard()
        simcard3.add_simcard()
        simcard4.add_simcard()
        simcard5.add_simcard()
        simcard6.add_simcard()

    def get_simcard_by_id(self):
        simcard = SimCard(simcard_id=1)
        simcard.get_simcard()

    def update_simcard(self):
        simcard = SimCard(name=1, phone_number=796961853, serial=957575, service_provider="africell", is_active=False, human_id=1)
        simcard.update_simcard()

    def delete_simcard(self):
        simcard = SimCard(simcard_id=4)
        simcard.delete_simcard()