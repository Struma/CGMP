#/usr/bin/python3
import fire

def printer():
    return print(dang)

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
