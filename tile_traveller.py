# Þetta forrit virkar eins og maður sé fastur í völundarhúsi og hefur bara viss marga 
# möguleika til að hreyfa sig. 

# Völundarhúsið er 3x3 reitir og hreyfingin er einn af 4 möguleikum
# S.s. n/N fyrir norður(upp), e/E fyrir austur(hægri), s/S fyrir suður(niður) og w/W fyrir vestur(vinstri)
# á ýmsum reitum eru veggir sem leifa þér ekki að fara í einhverja átt
# t.d. í reit 2,2 er bara hægt að fara til vinstri.
# Forritið mun láta notaandan vita hvaða leið er hægt að fara.
# t.d. ef forritið er í reiti 1,2 þá mun forritð segja að hægt sé að fara n/N, s/S og e/E
# Ef notandi skildi slá inn v/V þá mun koma in "Not a valid direction!"

# Forritið mun klárast þegar það er komið í reit 3,1
# Þá mun það prenta ú "Victory!"
def movement_side(x):
    if x == "e" or "E":
        x += 1
    elif x == "v" or "V":
        x -= 1
    return x
def movement_upp_down(y):
    if y == "n" or "N":
        y += 1
    elif y == "s" or "S":
        x -= 1
    return y

directions = input("Direction: ")

start = (1,1)
print(start)
n, N = 1
e, E = 1
v, V = -1
s, S = -1