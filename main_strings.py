# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

kicker_1 = "Ruud Gullit"
goal_0 = 32
kicker_2 = "Marco van Basten"
goal_1 = 54

scorers = kicker_1 + " " + str(goal_0) + ", " + kicker_2 + " " + str(goal_1)

report = f"{kicker_1} scored in the {goal_0}nd minute\n" + kicker_2 + " scored in the " + str(goal_1) + "th minute"

player = kicker_1
first_name = kicker_1[:kicker_1.find(" ")]
last_name_len = len(kicker_1[kicker_1.find(" ")+1:])
name_short = kicker_1[0] + ". " + kicker_1[kicker_1.find(" ")+1:]
chant = ((first_name + "! ")* len(first_name))[:-1]
good_chant = chant[-1] != " "