import pygame as pg

SIZE = WIDTH, HEIGHT = (880, 500)
pg.init()
screen = pg.display.set_mode(SIZE)

# игрок
pl_size = 50
player = pg.Surface((pl_size, pl_size))
player.fill('#ab0995')  # Цвет
pl_x, pl_y = WIDTH // 2, HEIGHT // 2  # координаты игрока
pl_step = 50  # шаг

# 1 противник
en_size = 50
enemy = pg.Surface((en_size, en_size))
enemy.fill('#5e755d')
en_x, en_y = 0, 0
en_step = 10

# 2 противник
en2_size = 50
enemy2 = pg.Surface((en2_size, en2_size))
enemy2.fill('#593030')
en2_x, en2_y = 670, 150


# Создание выхода
win_size = 50
win = pg.Surface((win_size, win_size))
win.fill('#7442c8')
win_x, win_y = 800, 0


# функция движения игрока
def move_player(x, y):
    pressed = pg.key.get_pressed()
    if pressed[pg.K_LEFT] or pressed[pg.K_a]:
        x -= pl_step
    if pressed[pg.K_RIGHT] or pressed[pg.K_d]:
        x += pl_step
    if pressed[pg.K_UP] or pressed[pg.K_w]:
        y -= pl_step
    if pressed[pg.K_DOWN] or pressed[pg.K_s]:
        y += pl_step
    return x, y


# функция движения противников
def move_enemy(x, y):
    if x < pl_x - en_step:
        x += en_step
    if x > pl_x + en_step:
        x -= en_step
    if y < pl_y - en_step:
        y += en_step
    if y > pl_y + en_step:
        y -= en_step
    return x, y


# Проверка, догнал ли противника игрок
def enemy_got_player():
    return (abs(pl_x - en_x) < 25 and abs(pl_y - en_y) < 25) or abs(pl_x - en2_x) < 25 and abs(pl_y - en2_y) < 25

# Проверка, дошел ли игрок до выхода
def player_got_win():
    return abs(pl_x - win_x) < 25 and abs(pl_y - win_y) < 25


game_running = True
while game_running:
    pg.time.delay(100)
    for e in pg.event.get():
        if e.type == pg.QUIT:  # Если был нажат крестик
            game_running = False
        elif e.type == pg.KEYDOWN:  # Если нажата клавиша
            pl_x, pl_y = move_player(pl_x, pl_y)  # Двигаем игрока

    en_x, en_y = move_enemy(en_x, en_y) # Двигаем противников
    en2_x, en2_y = move_enemy(en2_x, en2_y)
    if enemy_got_player():
        print('You lose :)')
        game_running = False

    if player_got_win():
        print('You win!!')
        game_running = False

    screen.fill('#cda4de')
    screen.blit(player, (pl_x, pl_y))  # Отрисовка игрока и противников
    screen.blit(enemy, (en_x, en_y))
    screen.blit(enemy2, (en2_x, en2_y))
    screen.blit(win, (win_x, win_y))

    pg.display.update()
# привет Тарас!!!
# whats up??
# \(^.^)/