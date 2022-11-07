#the author is Cadyn Reger

cpsc_names = {"Brown":"Cody","Bub":"Julia","Doherty":"Catherine","Dunn":"Nargaret","Greene":"Haley","Guthrie Beckstrom":"Isabela","Hongell":"Danielle","Hurley":"Camryn","Kevin":"Ellen","Kieft":"Brenna","Miloserny":"Amanda","Nyhuis":"Kaylen","Reger":"Cadyn","Rusch":"Emily","Salazar":"Britney","Schutz":"Julia", "Shadid":"Christina","Skrip":"Holly","Sullivan":"Anna","Verstraete":"Adrianne","Wardlow":"Sarah"}

def first_letter(d, letter):
    total = 0
    for key in d:
        if key[0] == letter:
            total += 1
    return total

first_letter(cpsc_names, "S")
first_letter(cpsc_names, "D")
