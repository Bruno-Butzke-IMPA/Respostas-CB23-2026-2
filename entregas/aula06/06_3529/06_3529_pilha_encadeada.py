class _No:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo

class PilhaEncadeada:

    def __init__(self):
        self._topo = None
        self.quantidade = 0

    def push(self, item):
        """
        Adiciona um elemento no topo da pilha.
        Complexidade: O(1).
        """
        novo_no = _No(item, self._topo)
        self._topo = novo_no
        self.quantidade += 1

    def pop(self):
        """
        Remove e retorna o elemento que está no topo da pilha.
        Complexidade: O(1).
        """
        if self.esta_vazia(): raise IndexError("A pilha está vazia")

        item = self._topo.valor
        self._topo = self._topo.proximo
        self.quantidade -= 1

        return item
    

    def topo(self):
        """
        Retorna o elemento que está no topo sem removê-lo.
        Complexidade: O(1).
        """
        if self.esta_vazia(): raise IndexError("A pilha está vazia")

        return self._topo.valor
    
    def esta_vazia(self):
        """
        Verifica se a pilha está vazia.
        Complexidade: O(1).
        """
        return self.quantidade == 0
    
    def __len__(self):    
        """
        Retorna a quantidade de elementos da pilha.
        Complexidade: O(1).
        """
        return self.quantidade


    def __repr__(self):
        """
        Retorna uma representação da pilha do topo para o fim.
        Complexidade: O(N), pois percorre todos os nós.
        """
        resultado = "PilhaEncadeada("
        atual = self._topo

        while atual is not None:
            resultado += str(atual.valor)

            if atual.proximo is not None:
                resultado += " -> "

            atual = atual.proximo
        resultado += ")"

        return resultado
