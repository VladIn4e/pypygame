import pygame
import random


def main():

    pygame.init()

    win = pygame.display.set_mode((500, 500))

    pygame.display.set_caption("Snake")

    font = pygame.font.SysFont('arial', 30)
    follow = font.render("Game Over", 1, (0, 100, 0))
    followb1 = font.render("Restart(press(f))", 1, (0, 200, 0))
    followb2 = font.render("Quit(press(g))", 1, (0, 200, 0))

    snake_speed = 10
    enemy_speed = 5

    x1 = 10
    y1 = 50
    width1 = 200
    height1 = 70

    x2 = 230
    y2 = 50

    colors = {
        "snake_head": (0, 155, 0),
        "snake_tail": (0, 200, 0),
        "apple": (255, 0, 0),
        "sensor": (255, 0, 0),
        "enemy": (0, 0, 255),
        "enemy_tails": (0, 0, 200)
    }

    snake_pos = {
        "x": 500/2,
        "y": 500/2,
        "x_change": 0,
        "y_change": 0
    }

    snake_size = (10, 10)

    snake_tails = []

    food_pos = {
        "x": round(random.randrange(0, 500 - snake_size[0]) / 10) * 10,
        "y": round(random.randrange(0, 500 - snake_size[0]) / 10) * 10,
    }

    enemy_size = (10, 10)

    enemy_pos = {
        "x": round(random.randrange(0, 500 - enemy_size[0]) / 10) * 10,
        "y": round(random.randrange(0, 500 - enemy_size[0]) / 10) * 10,
        "x_change": 0,
        "y_change": 0
    }

    enemy_pos2 = {
        "x": round(random.randrange(0, 500 - enemy_size[0]) / 10) * 10,
        "y": round(random.randrange(0, 500 - enemy_size[0]) / 10) * 10,
        "x_change": 0,
        "y_change": 0
    }


    enemy_tails = []
    enemy_tails2 = []
    enemy_tails.append([enemy_pos["x"]+10, enemy_pos["y"]])
    enemy_tails.append([enemy_pos["x"]+20, enemy_pos["y"]])
    enemy_tails.append([enemy_pos["x"]+30, enemy_pos["y"]])

    enemy_tails2.append([enemy_pos2["x"]+10, enemy_pos2["y"]])
    enemy_tails2.append([enemy_pos2["x"]+20, enemy_pos2["y"]])
    enemy_tails2.append([enemy_pos2["x"]+30, enemy_pos2["y"]])

    food_size = (10, 10)
    food_eaten = 0

    def game_over():
        run2 = True
        game_over_win = pygame.display.set_mode((500, 300))
        game_over_win.blit(follow, (220, 0))
        button_quit = pygame.draw.rect(game_over_win, (0, 60, 0), (x1, y1, width1, height1))
        button_restart = pygame.draw.rect(game_over_win, (0, 60, 0), (x2, y2, width1, height1))
        game_over_win.blit(followb1, (x1, y1))
        game_over_win.blit(followb2, (x2, y2))
        pygame.display.update()

        while run2:
            pygame.time.delay(90)


            for event in pygame.event.get():

                keys = pygame.key.get_pressed()

                if event.type == pygame.QUIT:
                    run2 = False
                    quit()

                elif keys[pygame.K_g]:
                    quit()
                    run2 = False

                elif keys[pygame.K_f]:
                    main()
                    run2 = False

    run = True
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.K_ESCAPE:
                run = False
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT and snake_pos["x_change"] == 0:
                    snake_pos["x_change"] = -snake_speed
                    snake_pos["y_change"] = 0

                elif event.key == pygame.K_RIGHT and snake_pos["x_change"] == 0:
                    snake_pos["x_change"] = snake_speed
                    snake_pos["y_change"] = 0

                elif event.key == pygame.K_UP and snake_pos["y_change"] == 0:
                    snake_pos["x_change"] = 0
                    snake_pos["y_change"] = -snake_speed

                elif event.key == pygame.K_DOWN and snake_pos["y_change"] == 0:
                    snake_pos["x_change"] = 0
                    snake_pos["y_change"] = snake_speed


        win.fill((0, 0, 0))

        ltx = snake_pos["x"]
        lty = snake_pos["y"]

        for i, v in enumerate(snake_tails):
            _ltx = snake_tails[i][0]
            _lty = snake_tails[i][1]

            snake_tails[i][0] = ltx
            snake_tails[i][1] = lty

            ltx = _ltx
            lty = _lty

        ltx1 = enemy_pos["x"]
        lty1 = enemy_pos["y"]

        for i, v in enumerate(enemy_tails):
            _ltx1 = enemy_tails[i][0]
            _lty1 = enemy_tails[i][1]

            enemy_tails[i][0] = ltx1
            enemy_tails[i][1] = lty1

            ltx1 = _ltx1
            lty1 = _lty1


        ltx2 = enemy_pos2["x"]
        lty2 = enemy_pos2["y"]
        for i, v in enumerate(enemy_tails2):
            _ltx2 = enemy_tails2[i][0]
            _lty2 = enemy_tails2[i][1]

            enemy_tails2[i][0] = ltx2
            enemy_tails2[i][1] = lty2

            ltx2 = _ltx2
            lty2 = _lty2

        for t in snake_tails:
            pygame.draw.rect(win, colors["snake_tail"], [
                t[0],
                t[1],
                snake_size[0],
                snake_size[1]])

        for i in enemy_tails:
            pygame.draw.rect(win, colors["enemy_tails"], [
                i[0],
                i[1],
                enemy_size[0],
                enemy_size[1]])

        for i in enemy_tails2:
            pygame.draw.rect(win, colors["enemy_tails"], [
                i[0],
                i[1],
                enemy_size[0],
                enemy_size[1]])

        if(snake_pos["x"] < -snake_size[0] + 10):
            game_over()
            run = False
        elif(snake_pos["x"] > 490):
            game_over()
            run = False
        elif(snake_pos["y"] < -snake_size[1] + 10):
            game_over()
            run = False
        elif(snake_pos["y"] > 490):
            game_over()
            run = False

        snake_pos["x"] += snake_pos["x_change"]
        snake_pos["y"] += snake_pos["y_change"]

        enemy_pos["x"] += enemy_pos["x_change"]
        enemy_pos["y"] += enemy_pos["y_change"]

        enemy_pos2["x"] += enemy_pos2["x_change"]
        enemy_pos2["y"] += enemy_pos2["y_change"]

        pygame.draw.rect(win, colors["snake_head"], [
            snake_pos["x"],
            snake_pos["y"],
            snake_size[0],
            snake_size[1]])

        pygame.draw.rect(win, colors["enemy"], [
            enemy_pos["x"],
            enemy_pos["y"],
            enemy_size[0],
            enemy_size[1]])

        pygame.draw.rect(win, colors["enemy"], [
            enemy_pos2["x"],
            enemy_pos2["y"],
            enemy_size[0],
            enemy_size[1]])

        pygame.draw.rect(win, colors["apple"], [
            food_pos["x"],
            food_pos["y"],
            food_size[0],
            food_size[1]])

        if (snake_pos["x"] > enemy_pos["x"] and enemy_pos["x"] + 10 != enemy_pos2["x"]):
            enemy_pos["x_change"] = enemy_speed
            enemy_pos["y_change"] = 0
        if (snake_pos["x"] < enemy_pos["x"] and enemy_pos["x"] - 10 != enemy_pos2["x"]):
            enemy_pos["x_change"] = -enemy_speed
            enemy_pos["y_change"] = 0
        if (snake_pos["y"] > enemy_pos["y"] and enemy_pos["y"] + 10 != enemy_pos2["y"]):
            enemy_pos["x_change"] = 0
            enemy_pos["y_change"] = enemy_speed
        if (snake_pos["y"] < enemy_pos["y"] and enemy_pos["y"] - 10 != enemy_pos2["y"]):
            enemy_pos["x_change"] = 0
            enemy_pos["y_change"] = -enemy_speed

        if (snake_pos["x"] > enemy_pos2["x"] and enemy_pos["x"] + 10 != enemy_pos2["x"]):
            enemy_pos2["x_change"] = enemy_speed
            enemy_pos2["y_change"] = 0
        if (snake_pos["x"] < enemy_pos2["x"] and enemy_pos["x"] - 10 != enemy_pos2["x"]):
            enemy_pos2["x_change"] = -enemy_speed
            enemy_pos2["y_change"] = 0
        if (snake_pos["y"] > enemy_pos2["y"] and enemy_pos["y"] + 10 != enemy_pos2["y"]):
            enemy_pos2["x_change"] = 0
            enemy_pos2["y_change"] = enemy_speed
        if (snake_pos["y"] < enemy_pos2["y"] and enemy_pos["y"] - 10 != enemy_pos2["y"]):
            enemy_pos2["x_change"] = 0
            enemy_pos2["y_change"] = -enemy_speed


        if(snake_pos["x"] == enemy_pos["x"]
            and snake_pos["y"] == enemy_pos["y"]):
            game_over()

        if(snake_pos["x"] == enemy_pos2["x"]
            and snake_pos["y"] == enemy_pos2["y"]):
            game_over()

        if(snake_pos["x"] == food_pos["x"]
            and snake_pos["y"] == food_pos["y"]):
            food_eaten += 1
            snake_tails.append([food_pos["x"], food_pos["y"]])

            food_pos = {
                "x": round(random.randrange(0, 500 - snake_size[0]) / 10) * 10,
                "y": round(random.randrange(0, 500 - snake_size[0]) / 10) * 10,
            }

        for i, v in enumerate(snake_tails):
            if(enemy_pos["x"] + enemy_pos["x_change"] == snake_tails[i][0]
                and enemy_pos["y"] + enemy_pos["y_change"] == snake_tails[i][1]):
                    enemy_pos = {
                        "x": round(random.randrange(0, 500 - enemy_size[0]) / 10) * 10,
                        "y": round(random.randrange(0, 500 - enemy_size[0]) / 10) * 10,
                        "x_change": 0,
                        "y_change": 0
                    }

        for i, v in enumerate(snake_tails):
            if (enemy_pos2["x"] + enemy_pos2["x_change"] == snake_tails[i][0]
                and enemy_pos2["y"] + enemy_pos2["y_change"] == snake_tails[i][1]):
                    enemy_pos2 = {
                        "x": round(random.randrange(0, 500 - enemy_size[0]) / 10) * 10,
                        "y": round(random.randrange(0, 500 - enemy_size[0]) / 10) * 10,
                        "x_change": 0,
                        "y_change": 0
                    }

        for i, v in enumerate(snake_tails):
            if(snake_pos["x"] + snake_pos["x_change"] == snake_tails[i][0]
                and snake_pos["y"] + snake_pos["y_change"] == snake_tails[i][1]):
                    pygame.time.delay(500)
                    game_over()

        for i, v in enumerate(enemy_tails):
            if(snake_pos["x"] + snake_pos["x_change"] == enemy_tails[i][0]
                and snake_pos["y"] + snake_pos["y_change"] == enemy_tails[i][1]):
                    pygame.time.delay(500)
                    game_over()

        for i, v in enumerate(enemy_tails2):
            if(snake_pos["x"] + snake_pos["x_change"] == enemy_tails2[i][0]
                and snake_pos["y"] + snake_pos["y_change"] == enemy_tails2[i][1]):
                    pygame.time.delay(500)
                    game_over()
        pygame.display.update()

main()