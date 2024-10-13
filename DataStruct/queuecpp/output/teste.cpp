#include <iostream>
#include <string>
#include <stdexcept>
using namespace std;

#define endl '\n'
const int lim = 10;

typedef struct Pess {
    string nome;
    int idade;
    int priority;
} Pessoa;

// Sobrecarga do operador << para imprimir Pessoa
ostream& operator<<(ostream& os, const Pessoa& p) {
    os << "Nome: " << p.nome << ", Idade: " << p.idade << ", Prioridade: " << p.priority;
    return os;
}

class Queuearray {
private:
    int size;
    int capacity = lim;
    Pessoa *fila;

public:
    Queuearray() {
        fila = new Pessoa[capacity];
        size = 0;
    }

    ~Queuearray() {
        delete[] fila;
    }

    bool isEmpty() {
        return size == 0;
    }

    bool isFull() {
        return size == capacity;
    }

    void enqueue(string name, int idade) {
        if (isFull()) {
            cout << "A Fila esta cheia" << endl;
            return;
        }

        Pessoa newPerson = {name, idade, returnPriority(idade)};
        
        // Inserir a pessoa na posição correta, movendo outros para frente
        int i;
        for (i = size - 1; i >= 0 && fila[i].priority < newPerson.priority; i--) {
            fila[i + 1] = fila[i];  // Movendo para frente
        }

        // Inserir a nova pessoa na posição correta
        fila[i + 1] = newPerson;
        size++;
    }

    void dequeue() {
        if (isEmpty()) {
            cout << "A Fila esta vazia" << endl;
            return;
        }

        // Remover a pessoa do início da fila (com maior prioridade)
        cout << fila[0].nome << " desenfileirado, idade: " << fila[0].idade 
             << ", prioridade: " << fila[0].priority << "." << endl;

        // Mover os outros elementos para trás
        for (int i = 1; i < size; i++) {
            fila[i - 1] = fila[i];
        }
        size--;
    }

    Pessoa peek() {
        if (!isEmpty()) {
            return fila[0];
        }
        throw out_of_range("Fila vazia!");
    }

    int returnPriority(int age) {
        if (age >= 60 && age < 70) { return 1; }
        else if (age >= 70 && age < 80) { return 2; }
        else if (age >= 80 && age < 90) { return 3; }
        else if (age >= 90 && age < 100) { return 4; }
        else if (age >= 100) { return 5; }
        else { return 0; }
    }
};

int main() {
    Queuearray fila;

    fila.enqueue("jorge", 10);
    fila.enqueue("mario", 60);
    fila.enqueue("domingos", 103);
    fila.enqueue("julio", 80);
    fila.enqueue("1", 72);
    fila.enqueue("2", 97);
    fila.enqueue("3", 20);
    fila.enqueue("4", 30);
    fila.enqueue("5", 71);
    fila.enqueue("mumia", 200);

  for(size_t i = 0;i<lim;++i){

    fila.dequeue();
  }
   fila.enqueue("mario",35);
   fila.enqueue("69",69);
   fila.enqueue("ggggg",5);
   
   fila.dequeue();

    
    cout << fila.peek() << endl;  

    return 0;
}
