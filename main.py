
class BaseContact:
  def __init__(self, first_name,last_name, phone_number, email):
     self.first_name  = first_name
     self.last_name = last_name
     self.phone_number = phone_number
     self.email = email
  def __str__(self):
      return f'{self.first_name} {self.last_name} {self.phone_number} {self.email}'
  def __repr__(self):
       return f'Card(first_name="{self.first_name}", last_name="{self.last_name}", phone_number="{self.phone_number}",email="{self.email}")'
  def contact(self):
       return f'Wybieram numer +48 {self.phone_number}i dzwonię do {self.first_name} {self.last_name}'
  @property
  def label_length(self):
      add = len(self.first_name) + len(self.last_name)
      return f'Dlugosc znakow: {add}'

class BusinessContact(BaseContact):
  def __init__(self, job, company, phone_number_business, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.job = job
         self.company = company
         self.phone_number_business = phone_number_business
  def __str__(self):
         return f'{self.first_name} {self.last_name} {self.phone_number} {self.email} {self.job} {self.company} {self.phone_number_b}'
  def __repr__(self):
   return f'Card(first_name="{self.first_name}", last_name="{self.last_name}", phone_number="{self.phone_number}",email="{self.email}, job="{self.job}", company="{self.company}", phone_number_business="{self.phone_number_business})'
  def contact(self):
          return f'Wybieram numer +48 {self.phone_number_business} i dzwonię do {self.first_name} {self.last_name}'
  @property
  def label_length(self):
    add = len(self.first_name) + len(self.last_name)
    return f'Dlugosc znakow: {add}'

my_list = []
def create_contacts(type, amount):
  from faker import Faker
  fake = Faker()
  for _ in range(amount):
      if type == 'N':
        card = BaseContact(first_name=fake.first_name(),last_name=fake.last_name(),phone_number=fake.phone_number(),email=fake.email())
      elif type == 'B': 
        card = BusinessContact(first_name=fake.first_name(),last_name=fake.last_name(),phone_number=fake.phone_number(),email=fake.email(), job=fake.job(),company=fake.company(),phone_number_business=fake.phone_number())
      my_list.append(card)

  print(f'Losowe wizytowki: {my_list}')
  print(card.contact())
  print(card.label_length)

type_of_contact  = (input('Podaj rodzaj wizytowki: (N/B)'))
amount = int(input('Podaj ilosc wizytowek:'))
create_contacts(type_of_contact , amount)



