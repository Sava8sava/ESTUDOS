#include <iostream>
#include <string>
#include <stdexcept>

using namespace std;
#define endl '\n'

const int lim = 10;

typedef struct Pess{
string nome;
int idade;
int priority;

}Pessoa;

// Sobrecarga do operador << para imprimir Pessoa
ostream& operator<<(ostream& os, const Pessoa& p) {
    os << "Nome: " << p.nome << ", Idade: " << p.idade;
    return os;
}
//nao estava conseguindo imprimir  head entao o gpt propos a ideia acima;

class Queuearray
{
private:
    int  head,tail,size;
    int capacity = lim;
    
    Pessoa *fila;

public:
  Queuearray(){
     head = 0;
     tail = -1;
     fila = new Pessoa[capacity];
     size = 0;
  }

  ~Queuearray(){ 
     delete[] fila;
  }

  bool isEmpty(){
   return size == 0;
  }

  bool isFull(){
        return size == capacity;
  }

  void enqueue(string name,int idade){
    if(isFull()){
            cout<<" a Fila esta cheia"<<endl;
            return;
    }
    
    Pessoa newPerson = {name,idade,returnPriority(idade)};

    //esquema para montar a fila com base na prioridade
    int i = (tail + capacity) % capacity;

    while (size > 0 && fila[i].idade < newPerson.idade) {
         fila[(i + 1) % capacity] = fila[i];
         i = (i - 1 + capacity) % capacity;  // Para evitar índices negativos
    }

   //adiciona no lugar certo
    fila[(i + 1) % capacity] = newPerson;
    tail = (tail + 1) % capacity;
    size++;
  }

  void dequeue(){
    if(isEmpty()){
            cout<<"a Fila esta vazia"<<endl;
            return;
    }
    cout << fila[head].nome << " desenfileirado, idade: " << fila[head].idade <<"prioridade: "<<fila[head].priority<<"." << endl;
    head = (head+1) % capacity;
    size--;
 }

 Pessoa peek(){
    if(!isEmpty()){
            return fila[head];
    }
    throw out_of_range("Fila vazia!");
 }

 int returnPriority(int age){

      if(age>=60 && age<70){return 1;
      }
      else if(age>=70 && age<80){return 2;
      }
      else if(age>=80 && age<90){return 3;
      }
      else if(age>=90 && age<100){return 4;
      }
      else if(age>=100){return 5;
      }
      else{ return 0;
      }  

 }

};

int main(){
Queuearray fila ;

    fila.enqueue("jorge", 10);
    fila.enqueue("mario", 60);
    fila.enqueue("domingos", 103);
    fila.enqueue("julio", 80);
    fila.enqueue("julia",60);

    cout << fila.peek() << endl;

    fila.dequeue();
    
    
    fila.enqueue("mumia",200);
   cout << fila.peek() << endl;

   

    cout << fila.peek() << endl;
}
