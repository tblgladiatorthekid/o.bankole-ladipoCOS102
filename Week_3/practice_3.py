print("WELCOME TO COUPE DE ESCRIVA 2023: FOOTBALL PICKS \n")

captain = {"Madiba":"Chubby Obiora-Okafor", "Blue Jays":"Christopher Uweh",
           "Cirok": "Alexander", "TSG Walkers": "Ikechukwu"}

goalkeepers = {"Madiba":"Chubby Obiora-Okafor",
               "Blue Jays":"Oladimeji Abaniwondea/ Jeffery Awagu","Cirok":"Timileyin Pearse/ Izuako Jeremy",
               "TSG Walkers": "Ayomide Ojituke"}
for pick in captain:
    print(pick, captain[pick])

print("\n")

for pick in goalkeepers:
    print(pick, goalkeepers[pick])
