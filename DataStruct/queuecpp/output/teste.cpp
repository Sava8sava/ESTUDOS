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
    int prio_pess = 0;
    int notprio_pers = 0;
    int nprioperswait = 0;
    int prioperswait = 0;

public:
    Queuearray() {
        fila = new Pessoa[capacity];
        size = 0;
        Menu();

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

         if(newPerson.priority<1){
            ++nprioperswait;
        }else{
            ++prioperswait;
        }

        size++;
    }

    void dequeue() {
        if (isEmpty()) {
            cout << "A Fila esta vazia" << endl;
            return;
        }

         if(fila[0].priority<1){
            ++notprio_pers;
            --nprioperswait;
        }else{
            ++prio_pess;
            --prioperswait;
        }

        // Remover a pessoa do início da fila (com maior prioridade)
        cout << fila[0].nome << " atendendido, idade: " << fila[0].idade 
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

    void strqueue(){
         if (isEmpty()) {
        cout << "A Fila esta vazia" << endl;
        return;
    }
    
    cout << "Fila atual:" << endl;
    for (int i = 0; i < size; i++) {
        cout << fila[i] << endl; // Usando a sobrecarga do operador << para imprimir Pessoa
    }

    }

    void getinfo(){
        cout<<"o numero de pessoas atendidas:\natendimento normal: "<<notprio_pers<<endl<<"atendimento prioritario: "<<prio_pess<<endl<<"tamanho atual da fila de atendimento:"<<size<<endl<<"numero de pessoas a ser atendidas:"<<endl<<"atendimento normal: "<<nprioperswait<<endl<<"atendimento prioritario:"<<prioperswait<<endl;


    }

    void Menu(){
        int opt = 0;
        bool active_loop = true;
        while(active_loop){
        cout<<"###############"<<endl<<"1.adicionar cliente. "<<endl<<"2.atender cliente. "<<endl<<"3.mostrar ordem da fila. "<<endl<<"4.gerar dados de consulta. "<<endl<<"5.sair\n"<<endl<<"escolha uma opcao.\n"<<"###############"<<endl;
        //acentos dao erros graficos corrigir depois,tabela ascii talves? 

        cin>>opt;
        cin.ignore();

        switch (opt){
        case 1: { 
          string nameaux;
          int idadeaux;
          cout<<"adicionando cliente"<<endl;
          cout<<"informe o nome"<<endl;
          getline(cin,nameaux);
          cout<<"informe a idade"<<endl;
          cin>>idadeaux;
          cin.ignore();
          enqueue(nameaux,idadeaux);
          break;
        }

        case 2:
         cout<<"atendendo o primeiro da fila"<<endl;
         dequeue();
         break;
        
        case 3:
         strqueue();
         break;

        case 4:
         getinfo();
         break;

        case 5:
         if(!isEmpty()){
         cout<<"a fila ainda nao esta vazia."<<endl;
         break;
         }
         active_loop = false;
         break;

        default:
            cout<<"erro"<<endl;
            break;
      }
    }
  } 
 
};

int main() {
    Queuearray fila;

    return 0;
}
