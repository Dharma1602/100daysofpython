programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

## Adding new items to a dictionary 

programming_dictionary["Loop"] = "The action of doing something over and over again"

## 
# create an empty dictionary

empty_dictionary = {}

##
# Wipe a existing dictionary 

dictionary = {
    "abc": "first three letters"
}

###To empty the above dictionary 

dictionary = {}

## Loop through a dictionary

for key in programming_dictionary:
    print(key)

## Edit an item in dictionary

programming_dictionary["Bug"] = "A Moth in your computer"

## Nested Dictionary

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}


travel_log = {
    "India": ["Delhi", "Vizag", "Hyderabad"],  # Nesting a List in Dictionary
    "Canada": ["Toronto", "Brampton", "Mississuaga"],
}

travel_log = {
    "India": {"cities_visited": ["Delhi", "Vizag", "Hyderabad"], "no_of_visits": 12},         # Nesting a Dicitonary in DIctionary
    "Canada": {"cities_visited": ["Toronto", "Brampton", "Mississuaga"], "no_of_visits": 2},
}


# Nesting a DIctionary in a List

travel_log = [
    {
        "country": "India",
        "cities_visited": ["Delhi", "Vizag", "Hyderabad"],                   
        "no_of_visits": 12
    },         
    {
        "country": "Canada",
        "cities_visited": ["Toronto", "Brampton", "Mississuaga"],
        "no_of_visits": 2
    },
]

