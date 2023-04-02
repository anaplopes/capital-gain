# Ganho de Capital

Programa de linha de comando (CLI) que calcula o imposto a ser pago sobre lucros ou prejuízos de operações no mercado financeiro de ações.

## Decisões técnicas e arquiteturais

Escolhido o Python como linguagem de programação, pela simplicidade de desenvolvimento, fácil entendimento e a diversidade de recursos nativos, evitando o uso de muitas dependências externas.
Na estrutura do projeto aplicado Clean Architecture com o objetivo de padronizar e organizar o código tornando reutilizável.
O desenvolvimento do código foi mantido o conceitos de clean code para facilitar a manutenção:
    - Separação das responsabilidades.
    - Type hints: usado para adicionar tipos a variáveis, parâmetros, argumentos de função, bem como seus valores de retorno, atributos de classe e métodos.
    - Docstring: usado para adicionar strings literais que aparecem na definição de uma função, método, classe ou módulo.

## Executar o aplicativo

- Instalar o CLI

    No diretório raiz do código-fonte, execute:
    > Instalará este aplicativo usando setup.py como “instruções”.

    ```bash
        pip3 install -e .
    ```

- Desistalar o CLI

    Da mesma forma, execute:
    > Removerá o aplicativo.

    ```bash
        pip3 uninstall pytax
    ```

- Executar o programa

    ```bash
        pytax
    ```

- Exemplo de entrada

    ```bash
        [{"operation": "buy", "unit_cost": 10.00, "quantity": 10000},{"operation": "sell", "unit_cost": 20.00, "quantity": 5000}]
    ```

- Exemplo de saída

    ```bash
        [{"tax": 0.00}, {"tax": 10000.00}]
    ```

## Executar os testes

- Unitário

    ```bash
        python3 -m unittest discover -s tests/unit -v
    ```
