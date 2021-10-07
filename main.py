vocales="aeiouáéíóú"
espacio=" "
palabra=""
palabra_final=""
contador_caracteres=0
texto = input("introduzca el texto: ").lower()
print("Frase original: ",texto)
texto=texto+espacio
for letras in texto:
  if letras == espacio:
    if contador_caracteres<6:
      for letras2 in palabra:
        palabra_final=palabra_final+letras2
    else:
      for letras2 in palabra:
        if letras2 not in vocales:
          palabra_final=palabra_final+letras2
    palabra_final=palabra_final+espacio
    palabra=""
    contador_caracteres=0
  else:
    palabra=palabra+letras
    if letras != ".":
      contador_caracteres=contador_caracteres+1

print("Frase resultante: ",palabra_final)






  