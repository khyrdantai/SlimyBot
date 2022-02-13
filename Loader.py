from Person import Person


class Loader:

    # we will need these text files
    birthdays_append = None
    birthdays_read = None
    birthdays_write = None
    # these are read-only
    channel_text = None
    token_text = None
    # turning some text files into usable objects
    channel_id = None
    token = None
    # the object-form list of people
    list_of_people = []

    def __init__(self):
        self.init = "Initializer"
        self.load_texts()
        self.operations()
        self.generate_list()

    def load_texts(self):
        self.birthdays_append = open("birthdays.txt", "a")
        self.birthdays_read = open("birthdays.txt", "r")
        self.birthdays_write = open("birthdays.txt", "w+")
        self.channel_text = open("channel.txt", "r")
        self.token_text = open("token.txt", "r")

    def operations(self):
        self.channel_id = self.channel_text.readline()
        self.token = self.token_text.readline()

    def generate_list(self):
        # reset the list to avoid memory leaks
        self.list_of_people = None
        self.list_of_people = []
        for lines in self.birthdays_read:
            info = lines.split(".")
            self.list_of_people.append(Person(info[0], info[1]))
