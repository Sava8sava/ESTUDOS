from HashtableALFABETO import Hashtable
from HashTable import _Hashtable

def getnames(path):
    names = []
    with open(path,'r') as file:
        names = [ line.strip() for line in file]
    return names    


if __name__ == "__main__":
    path = r"segunda parte /alunosED_2024.txt"
    names = getnames(path)

    #para mudar o valor de M so mudar o valor 
    #HSA = Hashtable(26)
    HS = _Hashtable(47)

    '''
    for name in names:
        HSA.put(name,1)
'''
    for name in names:
        HS.put(name,1)

    #print(HSA.show_quant_names())
    print(HS.show_quant_names())        



