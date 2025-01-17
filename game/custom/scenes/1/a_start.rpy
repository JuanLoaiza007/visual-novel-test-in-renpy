label s1_start:
  scene bg gotham night
  with fade

  pause 1
  
  play music main_theme volume 0.1
  show batman normal at left with dissolve
  batman "Parece una noche tranquila." with dissolve

  show joker shadow at right with dissolve 
  batman "Otra vez tú?."
  batman "..."
  batman "Espera, no eres el joker que conozco.{w=2}.. ¿verdad?"

  play sound "fx-transition.mp3"
  show joker normal at right with dissolve
  joker "Hola Bruce."
  joker "No soy tu joker."
  joker "Bruce, tienes [dinero] dólares."
  joker "Te daré 100 más."

  $ dinero += 100

  joker "Bruce, ahora tienes [dinero] dólares."

  joker "Dime, murciélago… ¿qué es verde, redondo y grita cuando lo tiras por las escaleras?"

  batman "{i}Suspira profundamente{/i}..."

  menu:
    "Un pepinillo filosófico.":
      jump s1_opt_bad
    "Un bloque de gelatina en crisis existencial.":
      jump s1_opt_bad
    "Una lechuga enojada.":
      jump s1_opt_nice
    "Tu sentido común despúes de oir esto.":
      jump s1_opt_bad

  return