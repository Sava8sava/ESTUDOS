from BinaryTree import BinaryTree

if __name__ == "__main__":
    teste = BinaryTree()
    teste.get(10)
    teste.insert('H')
    teste.insert('H')
    teste.insert('A')
    teste.insert('G')
    teste.insert('Z')
    teste.insert('V')
    teste.insert('X')
    teste.insert('Y')
    teste.get('Z')
    teste.get('H')
    teste.get('B')
    teste.size()
    teste.getdepth('A')
    teste.getheight()
    print(teste.Max_value())
    print(teste.Min_value())
    print(teste.internal_path_lenght())
    print(teste.is_balanced())
    aux = teste.show_pre_order()
   
   
    
    print(aux)