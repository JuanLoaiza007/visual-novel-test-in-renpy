# LOGICA DE JUEGO
init python:
    import random

    icon_rock = "minigames/rock_paper_scissors/piedra.png"
    icon_paper = "minigames/rock_paper_scissors/papel.png"
    icon_scissors = "minigames/rock_paper_scissors/tijeras.png"
    icon_size = (200, 200)

    eleccion_computadora = None
    eleccion_jugador = None
    resultado = None

    def jugar(eleccion):

        global resultado, eleccion_computadora, eleccion_jugador
        opciones = {"piedra": icon_rock, "papel": icon_paper, "tijera": icon_scissors}
        eleccion_jugador = opciones[eleccion]
        eleccion_cpu = random.choice(list(opciones))
        eleccion_computadora = opciones[eleccion_cpu]

        if eleccion == eleccion_cpu:
            resultado = f"Empate! Ambos eligieron {eleccion}."
        elif (eleccion, eleccion_cpu) in [("piedra", "tijera"), ("papel", "piedra"), ("tijera", "papel")]:
            resultado = f"¡Ganaste! {eleccion} vence a {eleccion_cpu}."
        else:
            resultado = f"Perdiste... {eleccion_cpu} vence a {eleccion}."

        renpy.call("mostrar_resultado")

# PANTALLA DE JUEGO
screen juego_ppt():
    vbox:
        align (0.5, 0.1)
        text "Elige tu jugada:" size 40 color "#FFFFFF"

    hbox:
        align (0.5, 0.2)
        spacing 30
        imagebutton idle icon_rock action Function(jugar, "piedra") at Transform(size=icon_size)
        imagebutton idle icon_paper action Function(jugar, "papel") at Transform(size=icon_size)
        imagebutton idle icon_scissors action Function(jugar, "tijera") at Transform(size=icon_size)

# CAPITULO DE RESULTADO
label mostrar_resultado:
    call screen resultado_ppt

# PANTALLA DE RESULTADO
screen resultado_ppt():
    vbox:
        xalign 0.5
        yalign 0.2

        text "Resultado del juego" size 40 color "#FFFFFF" 
        text resultado size 30 color "#FFFFFF"
    hbox:
        xalign 0.5
        yalign 0.6
        spacing 400
        vbox:
            text "Tu elección"
            add eleccion_jugador size icon_size xalign 0.5
        vbox:
            text "Tu oponente"
            add eleccion_computadora size icon_size xalign 0.5

    textbutton "Continuar" action Return() align (0.5, 0.8)
