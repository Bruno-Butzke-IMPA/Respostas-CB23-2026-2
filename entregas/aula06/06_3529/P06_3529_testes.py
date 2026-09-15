import unittest
from importlib import import_module

PilhaEncadeada = import_module(
    "06_3529_pilha_encadeada"
).PilhaEncadeada
FilaEncadeada = import_module(
    "06_3529_fila_encadeada"
).FilaEncadeada

class TestPilhaEncadeada(unittest.TestCase):

    def test_push_pop_lifo(self):
        pilha = PilhaEncadeada()

        pilha.push(1)
        pilha.push(2)
        pilha.push(3)

        self.assertEqual(pilha.pop(), 3)
        self.assertEqual(pilha.pop(), 2)
        self.assertEqual(pilha.pop(), 1)

    def test_pop_pilha_vazia(self):
        pilha = PilhaEncadeada()

        with self.assertRaises(IndexError):
            pilha.pop()

    def test_topo_pilha_vazia(self):
        pilha = PilhaEncadeada()

        with self.assertRaises(IndexError):
            pilha.topo()

    def test_len(self):
        pilha = PilhaEncadeada()

        self.assertEqual(len(pilha), 0)

        pilha.push("a")
        self.assertEqual(len(pilha), 1)

        pilha.push("b")
        self.assertEqual(len(pilha), 2)

        pilha.pop()
        self.assertEqual(len(pilha), 1)

        pilha.pop()
        self.assertEqual(len(pilha), 0)

    def test_alternancia_de_operacoes(self):
        pilha = PilhaEncadeada()

        pilha.push(10)
        self.assertEqual(pilha.topo(), 10)

        pilha.push(20)
        self.assertEqual(pilha.pop(), 20)

        pilha.push(30)
        self.assertEqual(pilha.topo(), 30)

        self.assertEqual(pilha.pop(), 30)
        self.assertEqual(pilha.pop(), 10)

    def test_diferentes_tipos_valores_repetidos_e_none(self):
        pilha = PilhaEncadeada()

        pilha.push(None)
        pilha.push(10)
        pilha.push("10")
        pilha.push(10)

        self.assertEqual(pilha.pop(), 10)
        self.assertEqual(pilha.pop(), "10")
        self.assertEqual(pilha.pop(), 10)
        self.assertIsNone(pilha.pop())


class TestFilaEncadeada(unittest.TestCase):

    def test_enfileirar_desenfileirar_fifo(self):
        fila = FilaEncadeada()

        fila.enfileirar(1)
        fila.enfileirar(2)
        fila.enfileirar(3)

        self.assertEqual(fila.desenfileirar(), 1)
        self.assertEqual(fila.desenfileirar(), 2)
        self.assertEqual(fila.desenfileirar(), 3)

    def test_intercalacao_enfileirar_desenfileirar(self):
        fila = FilaEncadeada()

        fila.enfileirar("A")
        fila.enfileirar("B")

        self.assertEqual(fila.desenfileirar(), "A")

        fila.enfileirar("C")

        self.assertEqual(fila.desenfileirar(), "B")
        self.assertEqual(fila.desenfileirar(), "C")

    def test_esvaziar_e_reutilizar(self):
        fila = FilaEncadeada()

        fila.enfileirar(1)
        fila.enfileirar(2)

        self.assertEqual(fila.desenfileirar(), 1)
        self.assertEqual(fila.desenfileirar(), 2)

        self.assertTrue(fila.esta_vazia())

        fila.enfileirar(3)
        fila.enfileirar(4)

        self.assertEqual(fila.desenfileirar(), 3)
        self.assertEqual(fila.desenfileirar(), 4)

    def test_desenfileirar_fila_vazia(self):
        fila = FilaEncadeada()

        with self.assertRaises(IndexError):
            fila.desenfileirar()

    def test_frente_fila_vazia(self):
        fila = FilaEncadeada()

        with self.assertRaises(IndexError):
            fila.frente()

    def test_frente_sem_remover(self):
        fila = FilaEncadeada()

        fila.enfileirar(10)
        fila.enfileirar(20)

        self.assertEqual(fila.frente(), 10)
        self.assertEqual(len(fila), 2)

        self.assertEqual(fila.desenfileirar(), 10)

    def test_len(self):
        fila = FilaEncadeada()

        self.assertEqual(len(fila), 0)

        fila.enfileirar("a")
        self.assertEqual(len(fila), 1)

        fila.enfileirar("b")
        self.assertEqual(len(fila), 2)

        fila.desenfileirar()
        self.assertEqual(len(fila), 1)

        fila.desenfileirar()
        self.assertEqual(len(fila), 0)


if __name__ == "__main__":
    unittest.main()
