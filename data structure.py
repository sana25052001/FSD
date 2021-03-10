from enum import Enum
class Country(Enum):
    Africa = 93
    Asia = 355
    America = 213
    Antarctica = 376
    Europe = 244
    Paris = 672
print('\nMember name: {}'.format(Country.Paris.name))
print('Member value: {}'.format(Country.Paris.value))


Output:
Member name: Paris
Member value: 672
