x=0
while x<=5:
    print(x)
    x=x+1


counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

check =dir(int)
print(check)