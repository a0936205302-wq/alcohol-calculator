drink_list=[{"name":"beer","volume":500,"abv":5,"count":2},
            {"name":"wine","volume":150,"abv":12,"count":1},
            {"name":"whisky","volume":30,"abv":40,"count":2},]

def calculate_alcohol(volume,abv,count):
    alcohol=volume*(abv/100)*0.789*count
    return alcohol

for drink in drink_list:
    alcohol=calculate_alcohol(drink["volume"],drink["abv"],drink["count"])
    print(f'{drink["name"]} alcohol = {alcohol:.1f} g')