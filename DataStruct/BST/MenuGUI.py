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

        self.BTshowmax = tk.Button(self.left_frame,text='Max Nodo',command= self.get_max_value)
        self.BTshowmax.pack(pady = (0,10),padx=10,anchor='nw')

        #nodo de menor valor
        self.inputMin = tk.Entry(self.left_frame,width= 20,state='readonly')
        self.inputMin.pack(pady = (10,5),padx = 10,anchor= 'nw')

        self.BTshowmin = tk.Button(self.left_frame,text='Min Nodo',command= self.get_min_value)
        self.BTshowmin.pack(pady = (0,10),padx=10,anchor='nw')

        #altura da arvore
        self.inputH = tk.Entry(self.left_frame,width= 20,state='readonly')
        self.inputH.pack(pady = (10,5),padx = 10,anchor= 'nw')

        self.BTshowH = tk.Button(self.left_frame,text='Altura da arvore',command= self.get_height_value)
        self.BTshowH.pack(pady = (0,10),padx=10,anchor='nw')

        #profundidade do no
        self.inputnodedp = tk.Entry(self.left_frame,width= 20,fg='gray')
        self.inputnodedp.pack(pady=(10,5),padx=10,anchor='nw')
        self.inputnodedp.insert(0,'Digite o No')
        self.inputnodedp.bind('<FocusIn>',self.clear_placeholder)
        self.inputnodedp.bind('<FocusOut>',self.add_placeholder)    
        
        self.inputDepth = tk.Entry(self.left_frame, width=20, state='readonly')
        self.inputDepth.pack(pady=(10, 5), padx=10, anchor='nw')

        self.BTshowDepth = tk.Button(self.left_frame, text='Profundidade', command=self.get_node_depth)
        self.BTshowDepth.pack(pady=(0, 10), padx=10, anchor='nw')

        #checar balaceamento
        self.inputbal = tk.Entry(self.left_frame,width= 20,state='readonly')
        self.inputbal.pack(pady = (10,5),padx = 10,anchor= 'nw')

        self.BTshowmin = tk.Button(self.left_frame,text='Checar Balanceamento',command= self.get_balavl)
        self.BTshowmin.pack(pady = (0,10),padx=10,anchor='nw')

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

    def get_balavl(self):
        pass
    def draw_tree(self):
        self.Rcanvas.delete('all')
        if self.tree.root:
            self._draw_node(self.tree.root,400,50,100)


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



  
