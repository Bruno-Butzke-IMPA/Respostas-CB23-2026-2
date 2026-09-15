<!-- utilizado IA somente para formatação em markdown. -->

# Respostas

## 1. Relações de herança entre as classes

As classes podem ser organizadas da seguinte forma:

### Classes-base

* **Pessoa**
* **Restaurante**
* **Iguaria**

### Subclasses

* **Funcionário**

  * Herda os atributos e métodos de **Pessoa**.
* **Chef de Cozinha**

  * Herda os atributos e métodos de **Funcionário**.
* **Garçom**

  * Herda os atributos e métodos de **Funcionário**.
* **Gerente**

  * Herda os atributos e métodos de **Funcionário**.
* **Pizza**

  * Herda os atributos e métodos de **Iguaria**.
* **Bolo**

  * Herda os atributos e métodos de **Iguaria**.
* **Pizzaria**

  * Herda os atributos e métodos de **Restaurante**.

A hierarquia de herança pode ser representada da seguinte maneira:

```text
Pessoa
└── Funcionário
    ├── Chef de Cozinha
    ├── Garçom
    └── Gerente

Restaurante
└── Pizzaria

Iguaria
├── Pizza
└── Bolo
```

Dessa forma, cada subclasse reutiliza os atributos e métodos de sua classe-pai, podendo também possuir características específicas.

---

## 2. Relação entre `Restaurante` e `Iguaria`

Eu não modelaria essa relação como uma **herança**, pois um restaurante não é uma iguaria e uma iguaria não é um restaurante.

Nesse caso, trata-se de uma relação de **associação/composição**, na qual um restaurante possui várias iguarias disponíveis.

Uma possibilidade seria criar uma classe intermediária chamada **Estoque**, responsável por representar e administrar as iguarias pertencentes a um restaurante.

Essa abordagem permite que a relação entre `Restaurante` e `Iguaria` seja tratada separadamente, sem a necessidade de modificar diretamente as duas classes.

A estrutura poderia ser:

```text
Iguaria N ─── 1 Estoque 1 ─── 1 Restaurante
```

Ou seja:

* Um **Estoque** pode estar associado a várias **Iguarias**.
* Um **Estoque** pertence a um **Restaurante**.
* O **Restaurante** utiliza o **Estoque** para controlar suas iguarias.

A classe `Estoque` também poderia possuir atributos e métodos próprios, como quantidade disponível, adicionar iguaria, remover iguaria, consultar estoque etc.

---

## 3. Tipos dos argumentos

### `argumento1` — `pedido`

Seria uma **instância de uma classe `Pedido`**.

```java
Pedido pedido
```

A criação de uma classe própria para representar o pedido permite armazenar diferentes informações relacionadas a ele, como:

* Cliente;
* Iguarias solicitadas;
* Quantidade;
* Valor total;
* Status do pedido.

Dessa forma, evita-se utilizar diversos argumentos separados para representar as informações de um pedido.

---

### `argumento2` — `comida`

Seria interessante utilizar um **`enum`**, contendo as opções de comidas disponíveis.

Por exemplo:

```java
enum Comida {
    PIZZA,
    BOLO
}
```

Assim, o argumento poderia ser:

```java
Comida comida
```

O uso de `enum` limita os valores possíveis do argumento às opções previamente definidas, evitando valores inválidos.

---

### `argumento3` — `funcionario_id`

Seria um tipo **inteiro**, utilizado para representar o identificador único de um funcionário.

```java
int funcionario_id
```

O uso de um ID é mais adequado do que utilizar o nome do funcionário como identificador, pois podem existir duas ou mais pessoas com nomes iguais ou semelhantes.

Assim, o ID permite identificar cada funcionário de forma única e reduz a possibilidade de associações incorretas.

---

## 4. Diagrama de classes UML

O diagrama de classes deve representar:

* A hierarquia de herança entre `Pessoa`, `Funcionário`, `Chef de Cozinha`, `Garçom` e `Gerente`;
* A hierarquia entre `Iguaria`, `Pizza` e `Bolo`;
* A hierarquia entre `Restaurante` e `Pizzaria`;
* A associação entre `Restaurante`, `Estoque` e `Iguaria`;
* Os atributos e métodos relevantes de cada classe;
* As multiplicidades das associações.

O diagrama pode ser desenvolvido utilizando uma das seguintes ferramentas online:

* **Paradigm Online**
* **draw.io (diagrams.net)**
