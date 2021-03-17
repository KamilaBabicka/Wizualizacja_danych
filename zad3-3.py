sklep = {"jabłka": "kg",
        "chleb": "sztuki",
        "gruszki": "kg",
        "mleko": "sztuki",
        "pomidory": "kg"}

kg = [key for key, value in sklep.items() if value == "kg"]
print(kg)