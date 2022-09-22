
'''
Em C:

typedef struct {
    int dado; // aqui tem que ser tipado; em python não 
    No *proximo; 
}No;

Em Pascal
type
 No = ^MeuNo;
 MeuNo = record
          dado: integer;
          proximo: No
         end;
'''
class No:
    
    def __init__(self,d=None,p=None): 
        # a diferença aqui pra C e Pascal é que existe uma função já "pronta"
        # pra criar o No. Em C e Pascal precisamos fazer isso totalmente na mão.
        self.dado = d
        self.proximo = p
    def __repr__(self):
        return "%s" % (self.dado)

lista = ""
# tamanho_lista = 0

# def inicializar(tamanho):
#     return [None]*tamanho  # O(1) 
 
# def buscar(lista,elemento):
#     pass

# def adicionar(lista,elemento):
#     global tamanho_lista
#     if tamanho_lista < 5:
#         lista[tamanho_lista]  = elemento
#         tamanho_lista += 1
#     else:
#         print("Lista Cheia")

# def remover(lista,elemento):
#     pass

# lista encadeada

def criar_encadeada(dado):
    # return None
    no = No(dado)
    return no
    
# TODO verificar
def adicionar_encadeada_no_comeco(dado):
    global lista
    no = No(dado) 
    no.proximo = lista
    lista = no

def adicionar_encadeada_fim(dado):
    no = No(dado)  # cria o No

    # procura pelo ultimo
    ultimo = lista
    while(ultimo.proximo !=None):
        ultimo = ultimo.proximo

   # o proximo do "ultimo" vai ser o novo no recem criado.
    ultimo.proximo = no

def buscar_encadeada(n):
    pass
def remover_encadeada(dado):
    # procurar na lista
    aux = lista
    anterior = None
    while(aux.dado != dado and aux.proximo !=None):
        anterior = aux
        aux = aux.proximo
    if (aux.proximo == None):
    # chegou no fim
        if(aux.dado == dado):
            # to no ultimo, é o elemento
            anterior.proximo = None
        else:
            print("elemento não encontrado")
    else:
    # nao chegou no fim da lista
        if(lista.dado == aux.dado):
           #comeco da lista 
            aux2 = lista.proximo
            lista = lista.proximo
            aux2.proximo = None
        else:
            # meio da lista
            anterior.proximo = aux.proximo
            aux.proximo = None

lista = criar_encadeada(10)
adicionar_encadeada_fim(5)
adicionar_encadeada_fim(2)
adicionar_encadeada_fim(6)

def imprime_enc():
    aux = lista
    while aux != None:
        print(aux)
        aux = aux.proximo

imprime_enc()

remover_encadeada(10)

print("")
imprime_enc()