from importlib import import_module

PilhaEncadeada = import_module(
    "06_3529_pilha_encadeada"
).PilhaEncadeada


class FilaEncadeada:

    def __init__(self):
        self.entrada = PilhaEncadeada()
        self.saida = PilhaEncadeada()
        self.quantidade = 0
        
    def enfileirar(self, item):
        """
        Insere um item no fim da fila. 
        Complexidade: O(1).
        """
        self.entrada.push(item)
        self.quantidade += 1


    def desenfileirar(self):
        """
        Remove e retorna o item da frente da fila.
        Complexidade: O(1) amortizada.
        """
        if self.esta_vazia():
            raise IndexError("A fila está vazia")

        if self.saida.esta_vazia():
            while not self.entrada.esta_vazia():
                self.saida.push(self.entrada.pop())

        self.quantidade -= 1
        return self.saida.pop()


    def frente(self):
        """
        Retorna o item da frente sem removê-lo.
        Complexidade: O(1) amortizada.
        """
        if self.esta_vazia():
            raise IndexError("A fila está vazia")

        if self.saida.esta_vazia():
            while not self.entrada.esta_vazia():
                self.saida.push(self.entrada.pop())

        return self.saida.topo()
    

    def __len__(self):
        """
        Retorna a quantidade de elementos da fila. 
        Complexidade: O(1).
        """
        return self.quantidade
    

    def esta_vazia(self):
        """
        Retorna True se a fila estiver vazia. 
        Complexidade: O(1).
        """
        return self.quantidade == 0


    def __repr__(self):
        """
        Retorna uma representação da fila da frente para o fim.
        Complexidade: O(N).
        """
        resultado = "FilaEncadeada("
        primeiro = True

        temporaria = PilhaEncadeada()


        while not self.saida.esta_vazia():
            item = self.saida.pop()
            temporaria.push(item)

            if not primeiro:
                resultado += " -> "

            resultado += str(item)
            primeiro = False

        while not temporaria.esta_vazia():
            self.saida.push(temporaria.pop())

        temporaria = PilhaEncadeada()


        while not self.entrada.esta_vazia():
            temporaria.push(self.entrada.pop())


        while not temporaria.esta_vazia():
            item = temporaria.pop()

            if not primeiro:
                resultado += " -> "

            resultado += str(item)
            primeiro = False

            self.entrada.push(item)

        resultado += ")"

        return resultado