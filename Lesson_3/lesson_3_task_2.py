from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Samsung", "Galaxy S24", "+7 900 123 45 67"))
catalog.append(Smartphone("Apple", "iPhone 14", "+7 923 456 78 90"))
catalog.append(Smartphone("Google", "Pixel 8", "+7 934 567 89 01"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+7 945 678 90 12"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+7 956 789 01 23"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
