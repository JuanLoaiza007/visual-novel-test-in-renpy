# ===> Juego de adivinanzas <===
default s1_opt1 = False
default s1_opt2 = False
default s1_opt3 = False

label start_s1_questionary:
  joker "[mc_name], tienes [dinero] dólares."
  
  show screen dinero_display

  joker "Te daré 300 más."

  $ dinero += 300
  show screen dinero_display

  joker "[mc_name], ahora tienes [dinero] dólares."

  stop music fadeout 1.0
  play music stress_theme fadein 1.0
  show bg joker gray with vpunch 

  pause 1

  joker "¿Que tal un acertijo?"
  batman "* Suspira profundamente *"
  jump jokers_questionary

screen dinero_display():
    text "Dinero: [dinero]" xpos 0.5 ypos 0.1 color "#FFFFFF" size 50 font "fonts/BatmanForever.ttf"

label jokers_questionary:
    joker "Dime [mc_name]… ¿qué es verde, redondo y grita cuando lo tiras por las escaleras?"

    menu:
        "Un pepinillo filosófico." if not s1_opt1:
            $ s1_opt1 = True
            jump s1_opt_bad
        "Un bloque de gelatina en crisis existencial." if not s1_opt2:
            $ s1_opt2 = True
            jump s1_opt_bad
        "Una lechuga enojada.":
            jump s1_opt_nice
        "Tu sentido común después de oír esto." if not s1_opt3:
            $ s1_opt3 = True
            jump s1_opt_bad

label s1_opt_bad:
    joker "BEW! {w=1} Error{w=1}, se ha retirado 100 de su cartera [mc_name]"
    $ dinero -= 100 
    show screen dinero_display
    jump jokers_questionary

label s1_opt_nice:
    joker "BJAAJAWWJAJWAJJA."
    joker "... {w=1}Lo siento."
    jump empezar_juego_ppt