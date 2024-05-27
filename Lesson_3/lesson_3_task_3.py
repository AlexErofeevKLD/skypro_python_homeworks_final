from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Ленина", "10", "5")
from_address = Address("654321", "Санкт-Петербург", "Невский пр.", "15", "10")
mail = Mailing(to_address, from_address, 1000, "Заказное письмо")

print(f"Отправление {mail.track} из {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house}-{from_address.apartment} "
      f"в {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house}-{to_address.apartment}. "
      f"Стоимость {mail.cost} рублей.")
