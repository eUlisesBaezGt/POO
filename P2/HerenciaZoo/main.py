from Class.Felidae import *

lion = Lion("Simba", "Savannah", "Mufasa", "Nala", 8, 500, 1.5, "Africa", 50)
lion.show()
print()
print()

tiger = Tiger("Richard Parker", "Jungle", "Diego", "Tigress", 7, 300, 1.2, "Asia", 40)
tiger.show()
print()
print()

panther = Panther("Bagheera", "Swamp", "Lucifer", "Felicia", 15, 400, 1.4, "America", 30)
panther.show()
print()
print()

cheetah = Cheetah("Azaad", "Sub-saharan africa", "Rocky", "Cybil", 10, 200, 1.1, "Africa", 80)
cheetah.show()
print()
print()

cougar = Cougar("P-22", "Scrub", "Zeus", "Stella", 13, 350, 1.25, "America", 60)
cougar.show()
print()
print()

# You can use:
lion.m_feed()
lion.m_transfer()
lion.m_check()
lion.m_sterilize()
lion.m_sleep()

lion.show()
