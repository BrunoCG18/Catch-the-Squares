from random import randint
import pygame


pygame.init()
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREEN2 = (0, 255, 127)
BLUE = (0, 0, 255)
BLUE2 = (65, 105, 225)
BLACK = (0, 0, 0)
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)

x = 1920
y = 1080
pos_jogador1 = [x / 2, y / 2 - 200]
pos_jogador2 = [x / 2, y / 2 + 200]
tamanho_jogadores = 50
velocidade_jogadores = 10
tamanho_ponto = 25
ponto = pygame.Surface((tamanho_ponto, tamanho_ponto))
ponto.fill(RED)
pontuacao_p1 = 0
pontuacao_p2 = 0

Fonte = pygame.font.SysFont("monospace", 40)
Fonte2 = pygame.font.SysFont("monospace", 150)
Fonte3 = pygame.font.SysFont("monospace", 30)
Fonte4 = pygame.font.SysFont("monospace", 60)

ganhou = 'ganhou!'


class Player1:

    def __init__(self, x, y, color, tamanho):
        self.x = x/2
        self.y = y/2
        self.color = color
        self.tamanho = tamanho

    @staticmethod
    def mexer():

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_a]:
            pos_jogador1[0] -= velocidade_jogadores
        if comandos[pygame.K_d]:
            pos_jogador1[0] += velocidade_jogadores
        if comandos[pygame.K_w]:
            pos_jogador1[1] -= velocidade_jogadores
        if comandos[pygame.K_s]:
            pos_jogador1[1] += velocidade_jogadores


p1 = Player1(x, y, GREEN, tamanho_jogadores)


class Player2:
    def __init__(self, x, y, color, tamanho):
        self.x = x / 2
        self.y = y / 2
        self.color = color
        self.tamanho = tamanho

    @staticmethod
    def mexer():
        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_LEFT]:
            pos_jogador2[0] -= velocidade_jogadores
        if comandos[pygame.K_RIGHT]:
            pos_jogador2[0] += velocidade_jogadores
        if comandos[pygame.K_UP]:
            pos_jogador2[1] -= velocidade_jogadores
        if comandos[pygame.K_DOWN]:
            pos_jogador2[1] += velocidade_jogadores


p2 = Player2(x, y, BLUE, tamanho_jogadores)


def criar_pontos():
    pos_x = randint(0, 1920 - tamanho_ponto)
    pos_y = randint(0, 1080 - tamanho_ponto)
    return pos_x, pos_y


pos_ponto = criar_pontos()


def pontuacao1(pos_jogador1, pos_ponto):
    pos_x1 = pos_jogador1[0]
    pos_y1 = pos_jogador1[1]

    pos_xp = pos_ponto[0]
    pos_yp = pos_ponto[1]

    if (pos_xp >= pos_x1  and pos_xp < (pos_x1 + tamanho_jogadores)) or (pos_x1 >= pos_xp and pos_x1 < (pos_xp + tamanho_ponto)):
        if (pos_yp >= pos_y1 and pos_yp < (pos_y1 + tamanho_jogadores)) or (pos_y1 >= pos_yp and (pos_y1 < (pos_yp + tamanho_ponto))):

            return True


def pontuacao2(pos_jogador2, pos_ponto):
    pos_x2 = pos_jogador2[0]
    pos_y2 = pos_jogador2[1]

    pos_xp = pos_ponto[0]
    pos_yp = pos_ponto[1]

    if (pos_xp >= pos_x2  and pos_xp < (pos_x2 + tamanho_jogadores)) or (pos_x2  >= pos_xp and pos_x2 < (pos_xp + tamanho_ponto)):
        if (pos_yp >= pos_y2 and pos_yp < (pos_y2 + tamanho_jogadores)) or (pos_y2 >= pos_yp and (pos_y2 < (pos_yp + tamanho_ponto))):

            return True


def resetar_posicao_jogar(pos_jogador1, pos_jogador2):
    if pos_jogador1[1] <= 0:
        pos_jogador1[1] = 0

    if pos_jogador1[1] >= 1080 - tamanho_jogadores:
        pos_jogador1[1] = y - tamanho_jogadores

    if pos_jogador1[0] <= 0:
        pos_jogador1[0] = 0

    if pos_jogador1[0] >= 1920 - tamanho_jogadores:
        pos_jogador1[0] = 1920 - tamanho_jogadores

    if pos_jogador2[1] <= 0:
        pos_jogador2[1] = 0

    if pos_jogador2[1] >= 1080 - tamanho_jogadores:
        pos_jogador2[1] = y - tamanho_jogadores

    if pos_jogador2[0] <= 0:
        pos_jogador2[0] = 0

    if pos_jogador2[0] >= 1920 - tamanho_jogadores:
        pos_jogador2[0] = 1920 - tamanho_jogadores


running = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_ESCAPE]:
            running = False

    clock.tick(60)
    pygame.time.delay(10)

    win.fill(BLACK)
    pygame.draw.rect(win, RED, (pos_ponto[0], pos_ponto[1], tamanho_ponto, tamanho_ponto))

    p1.mexer()
    p2.mexer()
    resetar_posicao_jogar(pos_jogador1, pos_jogador2)

    if pontuacao1(pos_jogador1, pos_ponto):
        pos_ponto = criar_pontos()
        pygame.draw.rect(win, RED, (pos_ponto[0], pos_ponto[1], tamanho_ponto, tamanho_ponto))
        pontuacao_p1 += 1

    if pontuacao2(pos_jogador2, pos_ponto):
        pos_ponto = criar_pontos()
        pygame.draw.rect(win, RED, (pos_ponto[0], pos_ponto[1], tamanho_ponto, tamanho_ponto))
        pontuacao_p2 += 1

    text1 = 'Pontuação:' + str(pontuacao_p1)
    label1 = Fonte.render(text1, 1, GREEN2)
    win.blit(label1, (0 + 10, 0 + 10))

    text2 = 'Pontuação:' + str(pontuacao_p2)
    label2 = Fonte.render(text2, 1, BLUE2)
    win.blit(label2, (x - 340, y - 50))

    if pontuacao_p1 >= 10 or pontuacao_p2 >= 10:
        game_over = 'Game Over'
        game_over_label = Fonte2.render(game_over, 1, AMARELO)
        win.blit(game_over_label, (x / 2 - 400, y / 2 - 200))

        r_to_restart = 'Aperte "R" para recomeçar'
        r_to_restart_label = Fonte3.render(r_to_restart, 1, AMARELO)
        win.blit(r_to_restart_label, (x / 2 - 225, y - 100))

        if pontuacao_p1 >= 10:
            verde = 'Verde'
            pontu_label = Fonte4.render(verde, 1, GREEN2)
            pontu_label2 = Fonte4.render(ganhou, 1, BRANCO)
            win.blit(pontu_label, (x / 2 - 200, y / 2))
            win.blit(pontu_label2, (x / 2, y / 2))

        elif pontuacao_p2 >= 10:
            azul = 'Azul'
            pontu_label = Fonte4.render(azul, 1, BLUE2)
            pontu_label2 = Fonte4.render(ganhou, 1, BRANCO)
            win.blit(pontu_label, (x / 2 - 180, y / 2))
            win.blit(pontu_label2, (x / 2, y / 2))

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_r]:
            pos_jogador1 = [x / 2, y / 2 - 200]
            pos_jogador2 = [x / 2, y / 2 + 200]
            pontuacao_p1 = 0
            pontuacao_p2 = 0
            pos_ponto = criar_pontos()
            pygame.draw.rect(win, RED, (pos_ponto[0], pos_ponto[1], tamanho_ponto, tamanho_ponto))

    pygame.draw.rect(win, GREEN, (pos_jogador1[0], pos_jogador1[1], tamanho_jogadores, tamanho_jogadores))
    pygame.draw.rect(win, BLUE, (pos_jogador2[0], pos_jogador2[1], tamanho_jogadores, tamanho_jogadores))

    pygame.display.update()
