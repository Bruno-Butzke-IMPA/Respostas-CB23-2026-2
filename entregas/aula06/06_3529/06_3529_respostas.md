# Aula 6 — Pilha e Fila Encadeadas
## Complexidade amortizada

Uma chamada isolada de `desenfileirar()` pode custar O(N).

Isso acontece quando a pilha de saída está vazia e existem N elementos na pilha de entrada. Nesse caso, todos os N elementos precisam ser retirados da pilha de entrada e colocados na pilha de saída. Porém, essa transferência não acontece a cada remoção. Depois que os elementos foram transferidos para a pilha de saída, várias operações de `desenfileirar()` podem ser realizadas com custo O(1), até que a pilha de saída fique vazia novamente. Assim, considerando uma sequência de N operações, o custo total das transferências é proporcional a N. Portanto, o custo médio por operação é O(1), caracterizando uma complexidade O(1) amortizada.

A mesma ideia se aplica ao método `frente()`: caso seja necessário realizar uma transferência, uma chamada isolada pode custar O(N), mas as transferências são distribuídas ao longo das operações. Por isso, seu custo amortizado é O(1).
