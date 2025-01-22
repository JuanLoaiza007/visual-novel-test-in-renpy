# ===> Inicio del capítulo <===
label s1_start:
  play music main_theme
  scene bg gotham night
  with fade

  pause 1

  show batman normal at left with dissolve
  batman "Hoy me gustaría cambiar mi nombre de superheroe."
  $ mc_name = renpy.input("¿Cómo te llamas?", default="Batman")
  batman "¡[mc_name]!{w=1}... {w=2}Bueno, luego podré cambiarlo."
  
  batman "Parece una noche tranquila." with dissolve

  show joker shadow at right with dissolve 
  batman "Otra vez tú?."
  batman "..."
  batman "Espera, no eres el joker que conozco.{w=2}.. ¿verdad?"

  play sound "fx-transition.mp3" volume 2
  show joker normal at right with dissolve
  joker "Hola [mc_name]."
  joker "No soy tu joker."
  
  jump start_s1_questionary
