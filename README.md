# Ganho de Capital
Programa de linha de comando (CLI) que calcula o imposto a ser pago sobre lucros ou prejuízos de operações no mercado financeiro de ações.


# Decisões técnicas e arquiteturais
Usado recursos nativos do Python para manter a simplicidade e facilitar a manutenção.
Aplicado conceitos de clean code para manter a elegância:
- Separação das responsabilidades e uma estrutura de código organizada.
- Type hints: usado para adicionar tipos a variáveis, parâmetros, argumentos de função, bem como seus valores de retorno, atributos de classe e métodos.
- Docstring: usado para adicionar strings literais que aparecem na definição de uma função, método, classe ou módulo.


# Compilar e executar o projeto
A melhor maneira de instalar (e desinstalar) seu aplicativo Python CLI é usar pip3. 

**Instalar o CLI**

No diretório raiz do código-fonte CLI, execute:
> Instalará este aplicativo usando setup.py como “instruções”.

```bash
    pip3 install -e .
```

**Desistalar o CLI**

Da mesma forma, execute:
> Removerá o aplicativo.

```bash
    pip3 uninstall pycli
```

**Executar o programa**

```bash
    cd pycli
```
```bash
    pycli
```

**Exemplo de entrada**

```bash
    [{"operation":"buy", "unit-cost":10.00, "quantity": 10000},{"operation":"sell", "unit-cost":20.00, "quantity": 5000}]
```

**Exemplo de saída**

```bash
    [{"tax":0.00}, {"tax":10000.00}]
```


# Executar os testes
...