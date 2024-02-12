# importe a biblioteca no seu código Python

from deep_translator import GoogleTranslator

# Vamos criar uma variável chamada tradutor 
# que utiliza a classe GoogleTranslator. 
# Essa classe requer dois parâmetros essenciais: 
# o idioma de origem (source) e o idioma desejado (target). 
# Por exemplo, para traduzir do português para o inglês

tradutor = GoogleTranslator(source="pt", target="en")

# Você pode informar os idiomas por extenso, 
# como “portuguese” e “english”, ou de forma abreviada. 
# Lembre-se de que os nomes por extenso devem ser escritos em inglês.

texto_original = input('Digite uma palavra ou frase em portuguêse e "Enter": ')
texto_traduzido = tradutor.translate(texto_original)
print(f"Texto traduzido: {texto_traduzido}")

