names = ['Laura', 'William', 'Weiwen', 'Justin', 'Ivan', 'Brandon']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[-1])
message = "Hey " + names[0].title() + ", just wanted to check in on you."
print(message)

message2 = "Hey " + names[2].title() + ", just wanted to check in on you."
print(message2)

message3 = "Hey " + names[3].title() + ", just wanted to check in on you."
print(message3)


transport = ['MRT', 'subway', 'bus', 'car']
message4  = "I love taking the " + transport[0].upper() + " everytime I'm commuting to work"
print(message4)

bts = ['suga', 'rm', 'v','jimin', 'jin', 'j-hope', 'jungkook']
print(bts[0].title())

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# pop function basically to remove the last data off the list, but to keep it on a nother list you've made
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first mototcycle I owned was a ' + first_owned.title() + '.')

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
too_expensive = 'honda'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me")

# 3.4 guest list
dinner_date = ['harry potter','suga','thomas newman', 'monet']
print(dinner_date)
print("Hey " + dinner_date[0].title() + " wanna come out and have dinner?")
print("Hey " + dinner_date[1].title() + " I would love to go on a date with you!")
print("Hey " + dinner_date[-1].title() + " let's go and have breakfast together!")
print("Hey " + dinner_date[2].title() + " can we have pasta for dinner tonight?")


# 3.5 changing guest list
dinner_date = ['harry potter','suga','thomas newman', 'monet']
print(dinner_date)
flaked_invite = dinner_date.pop(-1)
print(flaked_invite)
dinner_date.append('elon musk')
print(dinner_date)
print("Hey " + dinner_date[0].title() + " you're still coming for dinner right?")
print("Hey " + dinner_date[1].title() + " I can't wait for you to come!")
print("Hey " + dinner_date[2].title() + " bring your oboe to my dinner!")
print("Hey " + dinner_date[-1].title() + " tell me everything about Tesla later!")

# 3.6 more guests
dinner_date = ['harry potter','suga','thomas newman', 'monet']
print(dinner_date)
flaked_invite = dinner_date.pop(-1)
print(flaked_invite)
dinner_date.append('elon musk')
print(dinner_date)
print("\tHi everyone, unfortunately because " + flaked_invite + " can't make it tonight we will have a bigger dinner table! Oh and " + dinner_date[-1].title() + " will be coming as well!")
dinner_date.insert(0, 'bill clinton')
dinner_date.insert(3, 'aang')
dinner_date.append('da vinci')
print(dinner_date)
print("Hey " + dinner_date[0].title() + " I can't wait for you to come!")
print("Hey " + dinner_date[1].title() + " I can't wait for you to come!")
print("Hey " + dinner_date[2].title() + " I can't wait for you to come!")
print("Hey " + dinner_date[3].title() + " I can't wait for you to come!")
print("Hey " + dinner_date[4].title() + " I can't wait for you to come!")
print("Hey " + dinner_date[5].title() + " I can't wait for you to come!")
print("Hey " + dinner_date[-1].title() + " I can't wait for you to come!")


# 3.8 seeing the world
print('\n3.8 Seeing the world - This is a new exercise')
travel = ['sydney', 'stockholm','paris', 'auckland','doha']
print(travel)
print(sorted(travel))
print(travel)
travel.reverse()
print(travel)
travel.reverse()
print(travel)

