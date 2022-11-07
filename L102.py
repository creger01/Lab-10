#the author is Cadyn Reger

cpsc = ["Cody", "Julia", "Catherine", "Margaret", "Haley", "Isabela", "Danielle", "Camryn", "Ellen", "Brenna", "Amanda", "Kaylen", "Cadyn", "Emily", "Britney", "Julia", "Christina", "Holly", "Anna", "Adrianne", "Sarah"]

def frequency(cpsc):
    d = dict()
    for char in cpsc:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d

frequency(cpsc)
