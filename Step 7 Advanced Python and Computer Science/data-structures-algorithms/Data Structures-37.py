## 3. Exercise: Dynamic Arrays ##

# Retrieving an item in an array by index
retrieval_by_index = "constant"

# Searching for a value in an unordered array
search = "linear"

# Deleting an item from an array, and filling the gap
#     by shifting all later items back by one
deletion = "linear"

# Inserting an item into the array, and shifting forward
#     every item that comes after it
insertion = "linear"

## 4. Exercise: Practice Inserting Into an Array ##

players = ["Reggie Jackson"]
print(players)
players.insert(1, "C.J. Watson")
print(players)
players.insert(0, "Jeff Adrien")
print(players)
players.remove("Reggie Jackson")
print(players)
players.insert(0,"Quincy Acy")
players.insert(2,"Evan Turner")

## 6. 2D Array Implementation ##

red_pieces = 0
black_pieces = 0

# Find how many red and black pieces there are
for i in checker_board:
    for j in i:
        if j=="black":
            black_pieces+=1
        elif j=="red":
            red_pieces+=1

## 9. Dictionary Access ##

# Population of Rio de Janeiro
rio_population = city_populations["Rio de Janeiro"]
boston_population=city_populations["Boston"]
paris_population=city_populations["Paris"]
city_populations["Beijing"] += 1
city_populations["Boston"] -= 1

## 12. Exercise: Choosing a Data Structure ##

# Scenario A: You need to keep track of people sitting in an auditorium for a play. You'll have to identify which seats are empty, and sell tickets until the auditorium is completely full. How will you store the names of who's sitting where?
scenario_A_data_structure = "2d array"

# Scenario B: You're in charge of maintaining a guest list for a wedding. You're only concerned with a list of who's coming to the party. You have to add someone's name whenever they RSVP that they'll be attending the wedding.
scenario_B_data_structure = "dynamic array"

# Scenario C: Now every person who RSVPs for the wedding indicates which meal they want. You have to keep track of both the person and the meal order. You need to be able to find out what meal a particular person ordered quickly, so the waiters don't delay too long when it comes time to eat.
scenario_C_data_structure = "hash table"