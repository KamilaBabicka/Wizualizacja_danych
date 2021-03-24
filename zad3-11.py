import dni_tygodnia

x = int(input("Podaj numer dnia tygodnia, by otrzymać jego pełną nazwę.\n"))
print(dni_tygodnia.dni_numer(x))

y = input("Podaj nazwę dnia tygodnia, by otrzymać jego nazwę w języku angielskim.\n")
print(dni_tygodnia.dni_eng(y), "\n")
