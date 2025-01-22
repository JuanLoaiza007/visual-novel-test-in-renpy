# ===> Juego de piedra, papel y tijera <===
label empezar_juego_ppt:
    "El Joker obliga a [mc_name] a jugar piedra, papel y tijera."
    call screen juego_ppt 
    jump pregunta_jugar_de_nuevo 

label pregunta_jugar_de_nuevo:
    joker "¿Quieres jugar de nuevo?"
    menu:
        "Sí":
            jump empezar_juego_ppt 
        "No":
            joker "Hasta la próxima, [mc_name]."
            jump s1_end