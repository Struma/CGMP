#/usr/bin/python3
#tool to make concrete brick molds given a length and thickness of wood.
#Designed for making cement anchors and monolithes
import fire

def square(length, thick):
    l = (length  - (4 * thick))/4
    w = l + (2 * thick)
    ll = 2 * l
    llw = ll + w
    g = f"Cut lines for square mold\n\
         short piece l = {l}, long piece w = {w}\n\
         cut lines: {l}, {ll}, {llw}"
    return print(g)

def rectangle(length, thick):
    l = (length - (4*thick))/3
    w = l/2 + (2*thick)
    ll = 2*l
    llw = ll + w
    g = f"Cut lines for rectangle mold\n\
         long piece l = {l}, short piece w = {w}\n\
         cut lines: {l}, {ll}, {llw}"
    return print(g)

if __name__ == "__main__":
    fire.Fire()
