#include <iostream>

using namespace std;

typedef struct node{
    int value;
    node *next;
};

int main(){
    node *head;

    node variable_node = node();

    node *current = new node();
    current->value = 1000;
    current->next = NULL;

    variable_node = *(current);

    head = current;
    for(int i = 0 ; i <= 50 ; i++){
        //*dar 20 vueltas en el for
        node *aux = new node();
        aux->value = i;
        //*se creo un nodo y se le dio el valor de i
        current->next = aux;
        current = current->next;
    }
    current = head;
    while (current != NULL)
    {
       if ((current->value % 10) == 0){
           current->value = -1;
       }
        current = current->next;
    }
    current = head;
    current->next->next->next->next->next->next->value = -10;
    while (current != NULL)
    {
        cout << "Valor: " << current->value << endl;
        current = current->next;
    }
    return 0;
}