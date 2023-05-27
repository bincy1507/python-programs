is_magician = False
is_expert = True

if not(is_magician) and is_expert:
    print("You are a master magician")
elif not(is_magician) and not(is_expert):
    print("Atleast you are getting there")
elif is_magician and is_expert:
    print("You need magical powers")
else:
    print("Invalid condition")