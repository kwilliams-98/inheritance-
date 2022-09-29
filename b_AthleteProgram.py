import b_AthleteClass as ac

generic_athlete = ac.Athlete(6,220,0.2)

quarterback = ac.Football_Player(6.2,250,0.15,'quarterback','offense')


print("The height for the generic athlete is:",generic_athlete.get_ht()) #superclass method (superclass)

#print("The team of the generic athlete is:",generic_athlete.get_team()) #subclass method (superclass) = error

print("The weight for the football player is:",quarterback.get_wt()) #superclass method (subclass)

print("The position of the football player is:",quarterback.get_position()) #subclass method (subclass)
