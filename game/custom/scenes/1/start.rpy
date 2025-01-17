default s1_opt1 = False
default s1_opt2 = False
default s1_opt3 = False

label s1_start:
  play music main_theme
  scene bg gotham night
  with fade

  pause 1

  show batman normal at left with dissolve
  batman "Parece una noche tranquila." with dissolve

  show joker shadow at right with dissolve 
  batman "Otra vez tú?."
  batman "..."
  batman "Espera, no eres el joker que conozco.{w=2}.. ¿verdad?"

  play sound "fx-transition.mp3" volume 2
  show joker normal at right with dissolve
  joker "Hola [mc_name]."
  joker "No soy tu joker."
  joker "[mc_name], tienes [dinero] dólares."
  joker "Te daré 300 más."

  $ dinero += 300

  joker "[mc_name], ahora tienes [dinero] dólares."

  stop music fadeout 1.0
  play music stress_theme fadein 1.0

  pause 1

  joker "¿Que tal un acertijo?"
  batman "* Suspira profundamente *"

  jump jokers_questionary

  return

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

    return

label s1_opt_nice:
    joker "BJAAJAWWJAJWAJJA."
    joker "... {w=1}Lo siento."
    jump s1_end

label s1_opt_bad:
    joker "BEW! {w=1} Error{w=1}, se ha retirado 100 de su cartera [mc_name]"
    $ dinero -= 100 
    jump jokers_questionary