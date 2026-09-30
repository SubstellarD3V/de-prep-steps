"""
### add_price_to_product ###

Write a function that takes a dictionary (`product`) that looks like this:
`{ 'type': 'Tofu slices' }`,
and a number (`price`). Add a price property to this dictionary and set its
value to the `price`.
Then, return the dictionary.

e.g.

add_price_to_product({ 'type': 'Tofu slices' }, 2.20) # returns
{ 'type': 'Tofu slices', 'price': 2.20 }
"""


#def add_price_to_product(product, price):
#    if product == {}:
#        return product
#    else:
#        product['price'] = price
#        return (product)
    
#add_price_to_product({}, 2.20)

## add_property_to_product ###
"""
Write a function that takes three arguments:

 - a dictionary (`product`) that looks like this: `{'type': 'Terminator 2:
 Judgement Day', 'price': '£6.99', 'quantity': 1 }`
 - a `key` to add
 - a `value` corresponding to the key

It should then update the `product` to include this new attribute and return
the updated `product`.

add_attribute_to_product(
    {'type': 'Terminator 2: Judgement Day', 'price': '£6.99', 'quantity': 1 },
    'length', '2h 36m'
    )
#returns {
    # 'type': 'Terminator 2: Judgement Day',
    # 'price': '£6.99',
    # 'quantity': 1,
    # 'length': '2h 36m'
    # }

NOTE: Only certain types of data are able to be set a dictionary key. Your
function should take this into consideration and only allow the following data
types to be set as a key:
- string
- integer
- float
- boolean

If the given `key` argument is not one of these types then it should be
ignored and the product returned unchanged!
"""

#def add_attribute_to_product(product, key, value):

#    if type(key) == str or type(key) == int or type(key) == float or type(key) == bool:
#        product[key] = value
#        print(product)
#    else: 
#        print(product)

#product = {"type": "Terminator 2: Judgement Day", "price": "£6.99", "quantity": 1}
#add_attribute_to_product(product, [1, 2, 3], "a")

### create_northcoder ###

"""
Write a function that takes a string (name) and a number (year_of_birth) and
returns a dictionary with:

 - a name property set to the value of the name parameter
 - an age property set to whatever the age of the northcoder would be in the
 year 2023
 - a language property set to 'Python'

If the year is after 2023, show 'error' for the age.

create_northcoder('Joe', 2002)

returns
{
  'name': 'Joe',
  'age': 21,
  'language': 'Python'
}
"""

#def create_northcoder(name, year_of_birth):
#    if year_of_birth <= 2023: 
#        newdict = {
#            'name' : name,
#            'age' : 2023 - year_of_birth,
#            'language' : 'Python'
#        }
#    else: 
#        newdict = {
#            'name' : name,
#            'age' : 'error',
#            'language' : 'Python'
#        }
#    print(newdict)
    
#create_northcoder("Zarkon", 2123)

### delete_many_passwords ###
"""
Write a function that takes an array of user dictionaries (`users`), and
deletes the password key value pair on each user and returns the list.
If a dictionary does not already have a password key then it should be
unchanged.

delete_many_passwords([
    {'name': 'Barry', 'password': 'ilovetea', 'department': 'Tea'},
    {
        'name': 'Sandeep',
        'password': 'ilovecoffee',
        'favourite_drink': 'Coffee'
        },
    {'name': 'Kavita', 'password': 'ilovepie', 'weakness': 'Pie'}
])

Returns
[
    { 'name': 'Barry', 'department': 'Tea'},
    { 'name': 'Sandeep', 'favourite_drink': 'Coffee' },
    { 'name': 'Kavita', 'weakness': 'Pie'}
]
"""

#def delete_many_passwords(users):
#    for x in users: 
#        if "password" in x:
#            del x["password"]
#    print(users)
#    return users 
    
#delete_many_passwords(
#        [
#            {"name": "Barry", "password": "ilovetea", "department": "Tea"},
#            {"name": "Sandeep", "password": "ilovecoffee", "favourite_drink": "Coffee"},
#            {"name": "Kavita", "password": "ilovepie", "weakness": "Pie"},
#       ]
#    )

"""
### get_northcoders_names ###

Write a function that takes a list of dictionaries with the format from
create_northcoder (`northcoders`), and returns a new list of the users' names
as strings.
Any northcoders who are missing names should be omitted from the returned list.

northcoders = [
  {
    'name': 'Callum',
    'age': 31,
    'language': 'JavaScript'
  },
  {
    'name': 'Carrie',
    'age': 32,
    'language': 'Python'
  }
]

get_northcoders_names(northcoders) # returns ['Callum', 'Carrie']
"""


#def get_northcoders_names(northcoders):
#    nameslist = []
#    for x in northcoders: 
#        z = x.get("name")
#        if z is not None:
#            nameslist.append(z)
#    print(nameslist)
#    return nameslist
    
#result = get_northcoders_names(
#        [
#            {"name": "Callum", "age": 31, "language": "JavaScript"},
#            {"name": "Carrie", "age": 32, "language": "Python"},
#        ]
#    )

"""
### get_user_pet_age ###

Write a function that takes a `user` dictionary that looks like this:

{
  'name': "Tom",
  'age': 26,
  'pet': {
    'name': "Barney",
    'age': 6,
    'type': "good boy"
  }
}

The dictionary is nested; there are dictionaries paired to keys on the user
dictionary.

The function should access the age property in the nested pet dictionary
and return the value.
If the user doesn't have an age for their pet the function should return None.

user = {
  'name': "Carrie",
  'age': 26,
  'pet': {
    'name': "Pixie",
    'age': 4,
    'type': "gremlin"
  }
}

get_user_pet_age(user) # returns 4
"""


def get_user_pet_age(user):
    if "pet" in user: 
        petage = user.get("pet")   
        age = petage['age']
        print(age)
    else:
        age = None
        print(age)
    return age 

get_user_pet_age({"name": "Carrie", "age": 26})