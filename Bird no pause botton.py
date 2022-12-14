#Desarrollado por WinstXD320
import pygame
import random
import time
pygame.init()
pantalla = pygame.display.set_mode((270, 600))
pygame.display.set_caption("bird no pause button")
run = True
bandera_menu = True
tubo1 = pygame.image.load("pipe.png").convert_alpha()
tubo_1 = tubo1.get_rect()
tuboUP_1 = pygame.image.load("pipe_2.png").convert_alpha()
tubo_2 = tuboUP_1.get_rect()
animacion_pajaro = [pygame.image.load("bird1.png").convert_alpha(), pygame.image.load("bird2.png").convert_alpha(), pygame.image.load("bird3.png").convert_alpha()]
fondo = pygame.image.load("bg.png").convert_alpha()
imagen_menu = pygame.image.load("birdmenu.png").convert_alpha()
reloj = pygame.time.Clock()
fuente_tiempo = pygame.font.SysFont("System", 30, True)
fuente_puntos = pygame.font.SysFont("System", 30, True)
fuente_finjuego = pygame.font.SysFont("System", 20, True)
fuente_menu = pygame.font.SysFont("System", 25, True)
fuente_menu_c = pygame.font.SysFont("System", 25, True)
fuente_elaborado = pygame.font.SysFont("System",20,  True)
#********************************************************************************
fuente_dialogo = pygame.font.SysFont("system", 20, True)
fuente_creditos = pygame.font.SysFont("Console", 17 ,True)
dialogo = [
"       Ufffff!. Que viaje tan largo.", 
"  Voy a recoger todas las monedas",
"que pueda para comprar una paleta",
"",
"            'P' para continuar"
]
creditos = [
"        >Creditos<",
"",
"Sonído de fondo: KyB0za.",
"Codígo fuente del juego:",
"GitHub de WinstXD320.",
"",
"    Hecho con ♥ para la",
"    comunidad de python.",
"",
" Pulsa'B' para ir al menú",
"",
" Click en la pantalla para  ",
"     comenzar a jugar"
]
def icono(ruta_icono):
     pygame.display.set_icon(ruta_icono)
#--------------------------------------------------------------------------------
def menu():
    bandera_menu = True
    bandera_creditos = False
    while bandera_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                a = False
                bandera_menu = False
                pygame.display.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    print("Press c")
                    bandera_creditos = True
                if event.key == pygame.K_b:
                    bandera_creditos = False
                    print("Press b")
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("Press click izquierdo")
                    sonido_intro = pygame.mixer.Sound("sonido_intro.mp3")
                    sm = sonido_intro.play()
                    pygame.time.delay(2000)
                    bandera_menu = False
                    bandera_intro = True
        pantalla.fill((255,255, 255))
        pantalla.blit(fondo, (0, 0))
        boton = pantalla.blit(imagen_menu, (40, 200))
        texto = fuente_menu.render(">> Click en la pantalla <<", True, (255, 255, 255))
        texto_B = fuente_menu_c.render(">> Pulsa 'C' creditos <<", True, (255, 255, 255))
        texto_elaborado = fuente_elaborado.render("Made by WinstXD320", True, (101, 28, 30))
        pantalla.blit(texto, (20, 400))
        pantalla.blit(texto_B,(30, 430))
        pantalla.blit(texto_elaborado, (116, 580))
        e = 160
        if bandera_creditos == True:
            pantalla.fill((0,0,0))
            for texto in creditos:
                fuente = fuente_creditos.render(texto, True, (255, 0, 0))
                pantalla.blit(fuente, (1, e))
                e = e + 20
        pygame.display.update()
def animacion_intro():
    bandera_intro = True
    x, y = -40, 300
    bandera = True
    while bandera_intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                a = False
                bandera_intro = False
                pygame.display.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    print("Press p")
                    bandera = False
        pantalla.fill((255,255, 255))
        pantalla.blit(fondo, (0, 0))
        x = x + 1
        frame = int((time.time()) * 10) % len(animacion_pajaro)
        pantalla.blit(animacion_pajaro[frame], (x, y))
        e = 350
        if bandera == True:
            if x > 115:
                x = 115
                for i in dialogo:
                    texto_dialogo = fuente_dialogo.render(i, True, (101, 28, 30))
                    pantalla.blit(texto_dialogo, (7, e))
                    e = e + 15
        else:
            x = x + 1
        if x > 270:
            a = True
            bandera_intro =False
            pygame.mixer.music.load("musica_juego.mp3")
            pygame.mixer.music.play(-1)
        pygame.display.update()
        reloj.tick(60)
icono(animacion_pajaro[0])
def main(a):
    move_tubo1DOWN_1 = [300, 350, 340, 300]
    move_tuboUP_12 = [-350, -350, -360, -350]
    pos_texto_finjuego = -100
    pos_texto_tiempo = 10
    pos_texto_puntos = 30
    move_tubo1 = 300
    tubo_abajo = random.choice([move_tubo1DOWN_1[0], move_tubo1DOWN_1[1], move_tubo1DOWN_1[2], move_tubo1DOWN_1[3]])
    move_tuboUP_1 = 300
    tubo_arriba = random.choice([move_tuboUP_12[0],  move_tuboUP_12[1], move_tuboUP_12[2], move_tuboUP_12[3]])
    posicion_moneda = random.randint(200, 400)
    move_moneda  = 600
    v_y = 300
    v_x = 0
    velocidad = 0
    puntos = 0
    contador_tiempo = 0
    tiempo = 30
    a = True
    menu()
    animacion_intro()
    while a:
        contador_tiempo = contador_tiempo + 1
        if contador_tiempo == 30:
            contador_tiempo = 0
            tiempo = tiempo - 1
        if tiempo == 0:
            pantalla.blit(texto_finjuego, (100, 300))
            v_y = 10000
            print("tiempo se acabo")
            pos_texto_tiempo = - 30
            pos_texto_puntos = - 30
            pos_texto_finjuego = 300
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                a = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    velocidad = - 8
                    sonido = pygame.mixer.Sound("sonido_salto.mp3")
                    s = sonido.play()
                if event.key == pygame.K_p:
                    print("Return")
                    pos_texto_tiempo = 10
                    pos_texto_puntos = 30
                    pos_texto_finjuego = -100
                    v_y = 300
                    v_x = 0
                    velocidad = 0
                    move_tuboUP_1 = 300
                    move_tubo1 = 300
                    posicion_moneda = 300
                    move_moneda = 600
                    tiempo = 30
                    puntos = 0
                    contador_tiempo = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:    
                    velocidad = 2
        pantalla.fill((255, 255, 255))
        pantalla.blit(fondo, (0, 0))
        if move_tubo1 < move_tubo1 + 70:
            move_tubo1 -= 2
        if move_tubo1 < - 70:
            move_tubo1 = 300
            tubo_abajo = random.choice([move_tubo1DOWN_1[0], move_tubo1DOWN_1[1], move_tubo1DOWN_1[2], move_tubo1DOWN_1[3]])
        if move_tuboUP_1 < move_tuboUP_1 + 70:
            move_tuboUP_1 -= 2
        if move_tuboUP_1 < -70:
            move_tuboUP_1 = 300
            tubo_arriba = random.choice([move_tuboUP_12[0],  move_tuboUP_12[1], move_tuboUP_12[2], move_tuboUP_12[3]])
        obj1 = pantalla.blit(tubo1, (move_tubo1, tubo_abajo))
        obj2 = pantalla.blit(tuboUP_1, (move_tuboUP_1,  tubo_arriba))
        v_y = v_y + velocidad
        frame = int((time.time()) * 10) % len(animacion_pajaro)
        player = pantalla.blit(animacion_pajaro[frame], (v_x, v_y))
        if obj1.colliderect(player):
            v_y = 10000
            print("fin del juego" )
            pos_texto_tiempo = - 30
            pos_texto_puntos = - 30
            pos_texto_finjuego = 300
        if obj2.colliderect(player):
            v_y = 10000
            print("fin del juego")
            pos_texto_tiempo = -30
            pos_texto_puntos = -30
            pos_texto_finjuego = 300
        move_moneda -= 2
        obj3 = pygame.draw.circle(pantalla, (250, 213, 1), (move_moneda, posicion_moneda), 20, width=15)
        if move_moneda < - 30:
            move_moneda = 600
            posicion_moneda = random.randint(200, 400)
        if obj3.colliderect(player):
            sonido_moneda = pygame.mixer.Sound("sonido_moneda.wav")
            sm = sonido_moneda.play()
            move_moneda = - 29
            puntos += 1
            tiempo = tiempo + 10
            print("puntos: ", puntos)
        if obj1.colliderect(obj3):
            move_moneda = 600
        if obj2.colliderect(obj3):
            move_moneda = 600
        if puntos > 2:
            move_tuboUP_1 = move_tuboUP_1 - 0.4
            move_tubo1 = move_tubo1 - 0.4
            move_moneda = move_moneda - 0.4
        if puntos > 4:
            move_tuboUP_1 = move_tuboUP_1 - 0.4
            move_tubo1 = move_tubo1 - 0.4
            move_moneda = move_moneda - 0.4
        if puntos > 6:
            move_tuboUP_1 = move_tuboUP_1 - 0.4
            move_tubo1 = move_tubo1 - 0.4
            move_moneda = move_moneda - 0.4
        if puntos > 8:
            move_tuboUP_1 = move_tuboUP_1 - 0.4
            move_tubo1 = move_tubo1 - 0.4
            move_moneda = move_moneda - 0.4
        if puntos > 10:
            move_tuboUP_1 = move_tuboUP_1 - 0.4
            move_tubo1 = move_tubo1 - 0.4
            move_moneda = move_moneda - 0.4
        if puntos > 12:
            move_tuboUP_1 = move_tuboUP_1 - 0.4
            move_tubo1 = move_tubo1 - 0.4
            move_moneda = move_moneda - 0.4
        texto_tiempo = fuente_tiempo.render("Tiempo: " + str(tiempo), True, (255, 255, 255))
        texto_puntos = fuente_tiempo.render("Puntos: " + str(puntos), True, (255, 255, 255))
        texto_finjuego = fuente_finjuego.render("Fin del juego. 'P' para volver a jugar", True, (255, 0, 0))
        pantalla.blit(texto_tiempo, (140, pos_texto_tiempo))
        pantalla.blit(texto_puntos, (140, pos_texto_puntos))
        pantalla.blit(texto_finjuego, (5, pos_texto_finjuego))
        pygame.display.update()
        reloj.tick(60)
    pygame.display.quit()
main(run)