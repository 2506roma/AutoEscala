### Projeto: Sistema de Escala de Funcionários - Técnicos em Enfermagem e Enfermeiros

Este projeto visa criar um sistema automatizado para organizar escalas de plantão de funcionários técnicos em enfermagem e enfermeiros, com base no modelo 12x36. O sistema será capaz de receber dados dos funcionários, como nome, COREN e horários de trabalho, para gerar uma escala que abranja um período específico, do dia 16 ao dia 15 do mês seguinte.

### Funcionalidades
- **Período de Trabalho:** A escala será gerada com base nos dias de trabalho do dia 16 de um mês até o dia 15 do mês seguinte.
- **Modelo 12x36:** A escala seguirá o modelo de plantão 12x36, onde os turnos podem variar entre dias pares ou ímpares, dependendo do mês.
  
### Requisitos Funcionais
- **Quantidade de Funcionários Variável:** O sistema deve lidar com um número indefinido de funcionários, acomodando novas contratações e desligamentos.
- **Direito a Folga:** Cada funcionário terá direito a uma folga, que será equilibrada entre os plantões.
- **Reequilíbrio de Folgas:** Se houver plantões desbalanceados com relação às folgas (por exemplo, 3 funcionários em um plantão e apenas 1 no outro), o sistema deve permitir que os funcionários redistribuam suas folgas ou escolher automaticamente por meio de sorteio.
- **Identificação de Status de Indisponibilidade:** O sistema deve identificar automaticamente funcionários em férias, licença nojo, licença maternidade, afastamento, treinamento, gestação, folga de categoria ou afastamento do INSS, para não escalá-los.

### Requisitos Não Funcionais
- **Tempo de Resposta:** O sistema deve ser rápido e eficiente.
- **Eficiência de Memória:** O sistema deverá consumir pouca memória.
- **Usabilidade:** O sistema será simples e fácil de usar.
- **Documentação:** O resultado será gerado em formato Excel, de fácil leitura e exportação.
- **Capacidade de Escalar:** O sistema deve lidar com o crescimento do número de funcionários sem perda de desempenho.
- **Compatibilidade com Plataformas:** O sistema será compatível com diferentes sistemas operacionais (Windows, macOS, Linux) e diferentes versões do Python.
- **Disponibilidade:** O sistema deverá estar sempre disponível quando o documento for importado ao sistema.

### Ferramentas e Tecnologias
- **IDE:** PyCharm
- **Bibliotecas:** Pandas (para manipulação de planilhas Excel) e outras bibliotecas a serem definidas conforme necessário.

### Objetivo
O objetivo deste projeto é criar uma solução que automatize completamente a geração de escalas de plantão, considerando ausências, direitos a folga, e promovendo uma organização eficiente. O sistema proporcionará praticidade e clareza, gerando uma escala justa para todos os funcionários.
