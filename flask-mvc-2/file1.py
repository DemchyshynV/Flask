class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} - {self.surname}'


dicts = {'name': 'vasia', 'surname': 'popov', 'age': 3}
dicts.pop('age')

user = User(**dicts)

print(user)
