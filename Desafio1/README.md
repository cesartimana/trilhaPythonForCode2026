# Calculadora da Viagem

## Explicação do funcionamento do programa

Calculadora escrita em Python para indicar a viabilidade de uma viagem programada. O programa solicita informações de entrada ao usuário e, com elas, realiza cálculos para finalmente indicar se a viagem é viável ou não.

Os dados de entrada solicitados são:
- Orçamento disponível
- Destino
- Custo da passagem
- Custo diário da hospedagem
- Dias de viagem

O programa emite as seguintes informações:
- Se o orçamento é suficiente para viajar.
- Se a viagem é viável (o que exige, além do orçamento, que a quantidade de dias seja maior que zero).

## Instruções de uso

Insira os dados de entrada de acordo com o indicado:
- **Destino:** em formato de texto (nome).
- **Orçamento e custos:** em números reais positivos. Use **ponto decimal** e não utilize **separador de milhares**.
- **Dias de viagem:** em número inteiro positivo. Se forem inseridos decimais, estes serão ignorados.

## Respostas às perguntas teóricas

*Qual a diferença entre o comando* `git add .` *e* `git commit -m "mensagem"`*?*

O comando `git add .` atualiza a lista de mudanças dos arquivos do repositorio, mas não salva nada. O comando `git commit -m "mensagem"` salva permanentemente essas mudanças no histórico do repositório local. O `-m`  permite adicionar uma mensagem informativa.

*Por que é necessário realizar o casting (conversão de tipo) ao usar a função* `input()` *em Python para cálculos matemáticos?*

Porque a função `input()` sempre retorna os dados como uma string (texto). Para realizar operações matemáticas, precisamos que o Python reconheça eles como números. Por isso é preciso converter esse texto em um tipo numérico (`int` ou `float`).

*O que acontece se tentarmos somar uma variável do tipo* `str` *com uma do
tipo* `float` *?*

Ocorrerá um erro. O computador não consegue somar tipos diferentes porque as operações são distintas: somar duas `str` resulta em concatenação de textos, enquanto somar dois `float` é uma soma aritmética. A mistura desses dois tipos não está programada para funcionar.
