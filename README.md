# Tradutor-pt-en Python

1. **Instalação da Biblioteca:** Primeiro, vamos instalar a biblioteca deep-translator. Abra o terminal do seu editor de código e execute o seguinte comando:

```yaml
pip install deep-translator
```

2. **Importando a Biblioteca:** Agora, importe a biblioteca no seu código Python:

```yaml
from deep_translator import GoogleTranslator
```

3. **Criando o Tradutor:** Vamos criar uma variável chamada tradutor que utiliza a classe GoogleTranslator. Essa classe requer dois parâmetros essenciais: o idioma de origem (source) e o idioma desejado (target). Por exemplo, para traduzir do português para o inglês:

```yaml
tradutor = GoogleTranslator(source="pt", target="en")
```

Você pode informar os idiomas por extenso, como “portuguese” e “english”, ou de forma abreviada. Lembre-se de que os nomes por extenso devem ser escritos em inglês.

4. **Traduzindo Texto:** Agora você pode usar o tradutor para converter palavras ou frases.

```yaml
texto_original = input('Digite uma palavra ou frase em portuguêse e "Enter": ')
texto_traduzido = tradutor.translate(texto_original)
print(f"Texto traduzido: {texto_traduzido}")
```
Isso irá traduzir “Palavra ou frase em portuguêse” para o inglês.

**Com essas poucas linhas de código, você terá um tradutor funcional em Python! Lembre-se de explorar outras opções de tradução disponíveis na biblioteca deep-translator para personalizar ainda mais o seu projeto. 🚀**
