usa=1
china=0.1
print(type(china))
year=0
while china<usa:
    year=year+1
    china=china*1.048
    usa=usa*1.03
    print('china',china)
    print('usa',usa)
    print('year',year)
