def func(a,b):
    return b if a==0 else func(b % a,a)
#print(func(30,75))

numbers = (4,7,19,2,89,45,72,22)

sorted_numbers= sorted(numbers)
even = lambda a:a%2 ==0
even_numbers = filter(even,sorted_numbers)
#print(type(even_numbers))

set1 = {14,3,55}
set2 = {82,49,62}
set3 = {99,22,17}

#print(len(set1 + set2 + set3))

print(4**3+(7+5)**(1+1))

captains = {
    "Enterprise" : "Picard",
    "Voyager"  : "Janeway",
     "Defiant" : "Sisko"

}

"""for ship, captain in captains.items():
    print(ship,captain)"""

"""for ship in captains:
    print(ship,captains[ship])
"""
"""for ship in captains:
    print(ship,captains)"""


"""captains{"Enterprise" = "Picard"}
captains{"Voyager" = "Janeway"}
captains{"Defiant" = "Sisko"}"""

"""captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"""

"""captains = {
    "Enterprise" : "Picsard",
    "Voyager" : "Janeway",
    "Defiant" :"Sisko"
}
"""
#print(captains)

captains = {
    "Enterprise": "Picard",
    "Voyager" : "Janeway",
    "Defiant": "Sisko",
    "Discovery": "unknown"
}

"""for item in captains.items():
    print(f"The[ship] is captained by [captain]")"""

"""for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}")"""

"""f
or captain,ship in captains.items():
    print(f"The {ship} is captained by {captain}")"""

captains = {
    "Enterprice" : "Piard",
    "Voyager" : "Janeway",
    "Defiant" : "Sisko",
    "Discovery" : "Unkonown"
}


#del captains
#captains.remove()
del captains["Discovery"]
#captains["Discovery"].pop()
print(captains)