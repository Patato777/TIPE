from scripts.display_results import *

f = open(os.path.dirname(__file__)+'/resources/Liste_pos_Essonne_py.txt')
cities = eval(f.read())
f.close()
main = Main(cities)
for city in cities:
	main.map.plot(city[0],city[1],'foo')
