from Person import Person


class Loader:

    # used for turning some text files into usable objects
    channel_id = None
    token = None
    # the object-form list of people
    list_of_people = []

    def __init__(self):
        self.init = 'Initializer'
        self.operations()
        self.generate_list()

    def operations(self):
        # open channel text and read the line
        id_text = open('channel.txt', 'r')
        self.channel_id = id_text.readline()
        id_text.close()
        # open token text and read the line
        token_text = open('token.txt', 'r')
        self.token = token_text.readline()
        token_text.close()

    def generate_list(self):

        birthdays_text = open('birthdays.txt', 'r')

        self.list_of_people = []
        for lines in birthdays_text:
            info = lines.split(".")
            info[1].replace("\n", "")
            self.list_of_people.append(Person(info[0], info[1]))

        birthdays_text.close()

    def add_birthday(self, birth_date, user_id):
        # add to object list of people
        self.list_of_people.append(Person(birth_date, user_id))
        # open file, write, and close to save new input
        birthdays_text = open('birthdays.txt', 'a')
        birthdays_text.write(birth_date + '.' + user_id + '\n')
        birthdays_text.close()


#   def remove_birthday(self):
#   yet to implement
