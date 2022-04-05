'''
Készíts egy programot, amely képes tárolni:
- a diákok nevét és osztályát,
- a tanárok nevét és szakját / szakjait,
és ezeket meg is tudja jeleníteni a képernyőn egy összefüggő mondat formájában.

Például:
Szia, a nevem Kiss Péter, és a(z) 10.A osztályba járok.
Szia, a nevem Horváth Zita, biológia-kémia szakos tanár vagyok.
Szia, a nevem Schmidt Emil, matematika szakos tanár vagyok.

Használj objektumorientált megoldást!
- Először gondold végig, milyen osztályokra lesz szükség?
- Van-e lehetőség öröklődés alkalmazása révén optimálisabb kódot írni?
'''

class Suli:
    def __init__(self, vnev, knev, dort, osztaly, szak):
        self.vnev = vnev
        self.knev = knev
        self.dort = dort
        self.osztaly = osztaly
        self.szak = szak
        self.tnev = knev +' '+ vnev
        
alany = Suli(input('add meg a vezetékneved: '), input('Add meg a keresztneved: '), input('tanár vagy diák vagy? (t/d) : '), input('Hanyadik osztalyba jársz? (hagyd uresen ha tanár vagy.): '), input('milyen szakon végeztél? (hagyd uresen ha diak vagy): '))

if alany.dort == 'diák' or alany.dort == 'diak' or alany.dort == 'd':
    print(f'Szia, a nevem {alany.tnev}, és a {alany.osztaly} osztályba járok.')
elif alany.dort == 'tanár'or alany.dort == 'tanar' or alany.dort == 't':
    print(f'Szia, a nevem {alany.tnev}, és {alany.szak} szakos tanár vagyok.')