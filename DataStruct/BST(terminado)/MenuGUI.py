import tkinter as tk 
from tkinter import messagebox
from BinaryTree import BinaryTree

class MenuGui:
    def __init__(self):
        self.tree = BinaryTree()
        self.root = tk.Tk()
        self.root.title("BST")
        self.root.geometry('800x600')

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        ###################lado esquerdo################
        self.left_frame = tk.Frame(self.root,bg='#1c1018',width=400,height=600)
        self.left_frame.pack(side='left',fill='both')
        
        #inserir
        self.input = tk.Entry(self.left_frame,width= 20)
        self.input.pack(pady = (10,5),padx = 10,anchor= 'nw')

        self.BTins = tk.Button(self.left_frame,text='inserir',command= self.insert_tree)
        self.BTins.pack(pady=(0,10),padx= 10,anchor='nw')
        
        #nodo de maior valor
        self.inputMax = tk.Entry(self.left_frame,width= 20,state='readonly')
        self.inputMax.pack(pady = (10,5),padx = 10,anchor= 'nw')

        self.BTshowmax = tk.Label(self.left_frame,text='Max Nodo')
        self.BTshowmax.pack(pady = (0,10),padx=10,anchor='nw')

        #nodo de menor valor
        self.inputMin = tk.Entry(self.left_frame,width= 20,state='readonly')
        self.inputMin.pack(pady = (10,5),padx = 10,anchor= 'nw')

        self.BTshowmin = tk.Label(self.left_frame,text='Min Nodo')
        self.BTshowmin.pack(pady = (0,10),padx=10,anchor='nw')

        #altura da arvore
        self.inputH = tk.Entry(self.left_frame,width= 20,state='readonly')
        self.inputH.pack(pady = (10,5),padx = 10,anchor= 'nw')

        self.BTshowH = tk.Label(self.left_frame,text='Altura da arvore')
        self.BTshowH.pack(pady = (0,10),padx=10,anchor='nw')

        #profundidade do no
        self.inputnodedp = tk.Entry(self.left_frame,width= 20,fg='gray')
        self.inputnodedp.pack(pady=(10,0),padx=10,anchor='nw')
        self.inputnodedp.insert(0,'Digite o No')
        self.inputnodedp.bind('<FocusIn>',self.clear_placeholder)
        self.inputnodedp.bind('<FocusOut>',self.add_placeholder)    
        
        self.inputDepth = tk.Entry(self.left_frame, width=20, state='readonly')
        self.inputDepth.pack(pady=(0, 5), padx=10, anchor='nw')

        self.BTshowDepth = tk.Button(self.left_frame, text='Profundidade', command=self.get_node_depth)
        self.BTshowDepth.pack(pady=(0, 10), padx=10, anchor='nw')

        #checar largura interna
        self.inputL = tk.Entry(self.left_frame,width= 20,state='readonly')
        self.inputL.pack(pady = (10,5),padx = 10,anchor= 'nw')

        self.BTshowL = tk.Label(self.left_frame,text='largura interna da BST')
        self.BTshowL.pack(pady = (0,10),padx=10,anchor='nw')

        #checar balaceamento
        self.inputbal = tk.Entry(self.left_frame,width= 20,state='readonly')
        self.inputbal.pack(pady = (10,5),padx = 10,anchor= 'nw')

        self.BTshowbal = tk.Button(self.left_frame,text='Checar Balanceamento',command= self.get_balavl)
        self.BTshowbal.pack(pady = (0,10),padx=10,anchor='nw')

        #mostrar arvore por tipos de ordenção
        self.BTorder = tk.Button(self.left_frame,text='Mostrar arvores ordenadas',command=self.show_orders)
        self.BTorder.pack(pady=(10,5),padx=10,anchor= 'nw')

        ###################lado direito#################
        self.right_frame = tk.Frame(self.root,bg='white',width=400,height=600)
        self.right_frame.pack(side='right',fill='both',expand=True)

        #scroll vertical
        self.v_scrl = tk.Scrollbar(self.right_frame,orient='vertical')
        self.v_scrl.pack(side='right',fill='y')

        #scroll horizontal
        self.h_scrl = tk.Scrollbar(self.right_frame,orient='horizontal')
        self.h_scrl.pack(side='bottom',fill='x')

        self.Rcanvas = tk.Canvas(self.right_frame,bg='#95e06c',yscrollcommand=self.v_scrl.set,xscrollcommand=self.h_scrl.set)
        self.Rcanvas.pack(fill='both',expand=True)

        self.v_scrl.config(command=self.Rcanvas.yview)
        self.h_scrl.config(command=self.Rcanvas.xview)

        self.root.mainloop()

    def insert_tree(self):
        name = self.input.get()
        aux = self.tree.insert(name)

        if aux:
            print('Inserido')
            self.draw_tree()
            self.get_max_value()
            self.get_min_value()
            self.get_height_value()
            self.get_internal_width()
        else:
            print("erro")

    def get_max_value(self):
        MAX_val = self.tree.Max_value()

        self.inputMax.config(state='normal')
        self.inputMax.delete(0,tk.END)
        self.inputMax.insert(0,str(MAX_val))
        self.inputMax.config(state='readonly')

    def get_min_value(self):
        MIN_val = self.tree.Min_value()

        self.inputMin.config(state='normal')
        self.inputMin.delete(0,tk.END)
        self.inputMin.insert(0,str(MIN_val))
        self.inputMin.config(state='readonly') 

    def get_height_value(self):
        height = self.tree.getheight()

        self.inputH.config(state='normal')
        self.inputH.delete(0,tk.END)
        self.inputH.insert(0,str(height))
        self.inputH.config(state='readonly')    

    def get_node_depth(self):
        aux = self.inputnodedp.get()
        val = self.tree.getdepth(aux)

        self.inputDepth.config(state='normal')
        self.inputDepth.delete(0,tk.END)
        self.inputDepth.insert(0,str(val))
        self.inputDepth.config(state='readonly') 

    def get_internal_width(self):
        val = self.tree.internal_path_lenght()

        self.inputL.config(state='normal')
        self.inputL.delete(0,tk.END)
        self.inputL.insert(0,str(val))
        self.inputL.config(state='readonly') 

    def get_balavl(self):
        bool_aux = self.tree.is_balanced()

        self.inputbal.config(state='normal')
        self.inputbal.delete(0,tk.END)
        self.inputbal.insert(0,str(bool_aux))
        self.inputbal.config(state='readonly') 

    def draw_tree(self):
        self.Rcanvas.delete('all')
        if self.tree.root:
            self._draw_node(self.tree.root,400,50,100)

    def show_orders(self):
        try:
            pre = self.tree.show_pre_order()
            ino = self.tree.show_in_order()
            pos = self.tree.show_pos_order()
            niv = self.tree.show_in_level()

            pre_str = ' → '.join(map(str, pre))
            ino_str = ' → '.join(map(str, ino))
            pos_str = ' → '.join(map(str, pos))
            niv_str = ' → '.join(map(str, niv))

            messagebox.showinfo(
            "Ordenação da Árvore",
            f" ORDENAÇÃO POR:\n\n"
            f" PRÉ-ORDEM: {pre_str}\n"
            f" EM-ORDEM: {ino_str}\n"
            f" PÓS-ORDEM: {pos_str}\n"
            f" EM-NÍVEL: {niv_str}"
        )
            
        except Exception as e:
            messagebox.showerror("Erro Inesperado", f"Ocorreu um erro: {e}")

    def _draw_node(self,node,x,y,offset):
        #desenha o nó atual
        self.Rcanvas.create_oval(x-20,y-20,x+20,y+20,fill='#c3f73a')
        self.Rcanvas.create_text(x, y, text=str(node.data), font=("Arial", 12, "bold"))

        #caso exista desenha o nó da esquerda 
        if node.left:
            self.Rcanvas.create_line(x, y+20, x-offset, y+100, arrow=tk.LAST)
            self._draw_node(node.left, x-offset, y+100, offset//1.5)

        #analogamente o nó da direita 
        if node.right:
            self.Rcanvas.create_line(x, y+20, x+offset, y+100, arrow=tk.LAST)
            self._draw_node(node.right, x+offset, y+100, offset//1.5)

        
    #funçoes placeholder
    def clear_placeholder(self, event):
        if self.inputnodedp.get() == "Digite o No":
            self.inputnodedp.delete(0, tk.END)
            self.inputnodedp.config(fg='black')

    def add_placeholder(self, event):
        if not self.inputnodedp.get():
            self.inputnodedp.insert(0, "Digite o No")
            self.inputnodedp.config(fg='gray')
    


MenuGui()



  
