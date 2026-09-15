import random

def generate_maze(m, n, room=0, wall=1, cheese='.'):
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    stack = [(0, 0)]
    maze[1][1] = room

    while stack:
        x, y = stack[-1]

        random.shuffle(directions)
        encontrou = False

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall ):
                maze[2 * x + 1 + dx][2 * y + 1 + dy] = room
                maze[2 * nx + 1][2 * ny + 1] = room
                stack.append((nx, ny))
                encontrou = True
                break
        if not encontrou:
            stack.pop()

    while True:
        i = int(random.uniform(0, 2 * m))
        j = int(random.uniform(0, 2 * m))
        if maze[i][j] == room:
            maze[i][j] = cheese
            break

    return maze

def encontrar_queijo(maze, cheese='*'):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == cheese:
                return (i, j)

    return None

def buscar_caminho_dfs(maze, inicio=(1, 1), cheese='*', wall='■'):

    linhas = len(maze)
    colunas = len(maze[0])

    destino = encontrar_queijo(maze, cheese)

    if destino is None:
        return None

    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visitados = set()
    caminho = []

    def dfs(posicao):
        i, j = posicao

        if not (0 <= i < linhas and 0 <= j < colunas):
            return False

        if maze[i][j] == wall:
            return False

        if posicao in visitados:
            return False

        visitados.add(posicao)
        caminho.append(posicao)

        if posicao == destino:
            return True

        for di, dj in movimentos:
            nova_posicao = (i + di, j + dj)

            if dfs(nova_posicao):
                return True

        caminho.pop()
        return False

    if dfs(inicio):
        return caminho

    return None

def exibir_labirinto_com_caminho(maze, caminho, cheese='*'):
    labirinto = [linha[:] for linha in maze]

    for i, j in caminho:
        if labirinto[i][j] != cheese:
            labirinto[i][j] = 'x'

    for linha in labirinto:
        print(" ".join(map(str, linha)))

def print_maze(maze):
    for row in maze:
        print(" ".join(map(str, row)))

if __name__ == '__main__':
    m, n = 10, 14

    random.seed()

    room = ' '
    wall = '■'
    cheese = '*'

    maze = generate_maze(m, n, room, wall, cheese)

    print("\nLabirinto original:\n")
    for linha in maze:
        print(" ".join(map(str, linha)))

    caminho = buscar_caminho_dfs(maze, inicio=(1, 1), cheese=cheese, wall=wall)

    if caminho is not None:
        print("\nLabirinto com caminho encontrado:\n")
        exibir_labirinto_com_caminho(maze, caminho, cheese=cheese)

    else:
        print("\nNão foi possível encontrar um caminho.")