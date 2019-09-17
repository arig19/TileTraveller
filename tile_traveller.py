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
def movement(x, y):
# Færa forritð til hliðar s.s. hægri eða vinstri
    if directions == "e" and "E":
        x += 1
    elif directions == "v" and "V":
        x -= 1
# færa forritð upp eða niður
    if directions == "n" and "N":
        y += 1
    elif directions == "s" and "S":
        y -= 1
    return x, y
N = "(N)orth"
E = "(E)ast"
S = "(S)outh"
W = "(W)est"
start = (1,1)
print("You can travel:", N)
if start == (1,1):
    print("You can travel:", N)
elif start == (1,2):
    print("You can travel:", N, "or", E, "or", S)
elif start == (1,3):
    print("You can travel:", E, "or", S)
elif start == (2,1):
    print("You can travel:", N)
elif start == (2,2):
    print("You can travel:", W, "or", S)
elif start == (2,3):
    print("You can travel:", E, "or", W)
elif start == (3,3):
    print("You can travel:", W, "or", S)
elif start == (3,2):
    print("You can travel:", N, "or", S)
elif start == (3,1):
    print("Victory!")


directions = input("Directions: ")


while start != (3,1):
    directions = movement(start, start)
    print(start)