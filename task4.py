class List:

    def __init__(self):
        self.all_contacts = []

    def search_by_name(self, *name):
        for i in name:
            self.all_contacts.append(i.title())
        name = [i for i in self.all_contacts if self.all_contacts.count(i) > 1]
        names = set(name)
        print("Repeated word: ")
        for a in names:
            print("\t" , a)
class ContactList(List):

    def __init__(self):
        super().__init__()
my_contacts = ContactList()
my_contacts.search_by_name("Aisuluu" , "Beka" , "Ais" , "Ainazik" , "Beka")