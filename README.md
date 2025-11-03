# Esse projeto está em desenvolvimento:
Esse projeto foi desenvolvido pelo Grupo 6 para a disciplina de Programação 2 (CB23) do IMPA Tech

Feito por:
<ul>
    <li>Arthur Barbosa Pinheiro</li>
    <li>Daniel Rodrigues Serqueira</li>
    <li>Gabriel Colatusso Castro Da Cruz</li>
    <li>Manuela Abati Bordeaux Ronconi</li>
    <li>Marcelo Miguel Alves Da Silva</li>
    <li>Mateus Almeida Oliveira</li>
    <li>Ryan Kevin Da Costa Felinto</li>
    <li>Sérgio Teixeira Rosa</li>
    <li>Thierry Ventura Marcolino Da Silva</li>
    <li>Vinícius Flesch Kern</li>
</ul>

<br/>

# Versão do projeto: v0.0.4
Added linear interpolation

# Documentação

A biblioteca CB2325NumericaG6 é uma biblioteca de cálculo numérico para python que trabalha com funções de interpolação, aproximação, integração, busca de raízes, polinômios, etc.

## Instalação:
```shell
pip install CB2325NumericaG6
```

# Módulos:

- aproximacao
- erros
- integracao
- interpolacao
- polinomios
- raizes

# Aproximação (.aproximacao)

Esse módulo é direcionado a funções de aproximação numérica.

## Funções:

`ajuste_linear(x, y)`:

[❌] Status: Não implementado

```python
ajuste_linear(x: list[float], y: list[float]) -> Polinomio
```
**Entrada:**

A função recebe duas listas de variáveis, uma de coordenadas X e outra de coordenadas Y correspondentes.

As listas devem ter tamanhos iguais, pois cada ponto Y corresponde ao respectivo ponto X.

**Retorno:**
A função retorna o ajuste linear $y = ax + b$ da série de pontos por meio de um `Polinomio` [a,b]

# Erros (.erros)

Esse módulo é destinado ao cálculo de erros numéricos.

## Funções

`erro_absoluto(valor_real, valor_aproximado)`:

[❌] Status: Não implementado

`erro_relativo(valor_real, valor_aproximado)`:

[❌] Status: Não implementado

# Integração (.integracao)

Módulo que compõe as funções de integração.

## Funções

`integral(f, start, end, divisions)`

[✅] Status: Concluído

```python
integral(f:Callable, start: float, end: float, divisions: int) -> float
```

**Entrada:**
- f (Callable): Função a ser integrada
- start (float): Ponto inicial do intervalo
- end (float): Ponto final do intervalo
- divisions (int): Número de subdivisões do intervalo: números maiores implicam uma aproximação mais precisa, mas também consome mais CPU.

**Retorno:**
- float: Valor da integral.

# Interpolação (.interpolacao)

Módulo que compõe as funções de interpolação.

`Interpolator` é um `callable` que recebe `float` e retorna `float`

## Funções

`linear_interp(x, y)`, `poly_interp(x, y)`

[⚠️] Status: Necessária tradução do docstrings

```python
linear_interp(x: Sequence, y: Sequence) -> Interpolator
poly_interp(x: Sequence[float], y: Sequence[float]) -> Interpolator
```

**Entrada:**

- x (Sequence): Lista de coordenadas do eixo X (estritamente crescente)
- y (Sequence): Lista de coordenadas do eixo Y

**Retorno:**
- Interpolator: Uma função que retorna o valor interpolado linearmente baseado nos valores X, Y.

`hermite_interp(x, y, dy)`

[⚠️] Status: Necessária tradução do docstrings

```python
hermite_interp(x: Sequence[float], y: Sequence[float], dy: Sequence[float]) -> Interpolator
```

**Entrada:**

- x (Sequence): Lista de coordenadas do eixo X (estritamente crescente)
- y (Sequence): Lista de coordenadas do eixo Y
- dy (Sequence): Derivada dos valores para cada Y.

**Retorno:**
- Interpolator: Uma função que retorna o valor em um ponto pela interpolação de hermite baseado nos valores X, Y, dy.

# Interpolação (.interpolacao)

Módulo para definição e cálculo de polinomios.

## Classes:

`Polinomio`

[⚠️] Status: TO-DO pendente.

> TO-DO: Implementar um método melhor de definição de tolerância a partir do módelo de erros, ou por épsilon de máquina

### Métodos mágicos:
- **\_\_init\_\_(values: List[float])**
- **\_\_repr\_\_**
- **\_\_len\_\_**
- **\_\_getitem\_\_**
- **\_\_setitem\_\_**
- **\_\_mul\_\_, \_\_rmul\_\_**
- **\_\_neg\_\_**
- **\_\_add\_\_**
- **\_\_sub\_\_**
- **\_\_eq\_\_**

### Propriedades:
- **degree**: (int) Retorna o grau do polinômio
- **isZero**: (bool) Retorna True se o polinômio é nulo `[0.0]` ou False caso contrário.

### Métodos:
- **evaluate(x: float) -> float**: Calcula o valor do polinômio em um determinado ponto.
- **divideBy(divisor: Polinomio) -> Tuple[Polinomio, Polinomio]**: Realiza a divisão do polinomio por outro polinomio e retorna uma tupla da forma (Polinomio dividido, resto).
- **getRealRootBounds() -> tuple[float, float]**: Calcula os limites inferior e superior no quais estão todas as raízes reais positivas do polinômio;

## Funções

`diffPol(pol)`

[✅] Status: Concluído

```python
diffPol(pol: Polinomio) -> Polinomio
```

**Entrada:**

- pol (Polinomio): Polinomio a ser derivado.

**Retorno:**

- Polinomio: Polinomio derivado

`lambdify(P)`

[✅] Status: Concluído

```python
lambdify(P: 'Polinomio') -> Callable[[float], float]:
```

**Entrada:**

- P (Polinomio): O objeto Polinomio a ser convertido.

**Retorno:**

- Callable[[float], float]: Uma função lambda que recebe x (float) e retorna P(x) (float). *É apenas um wrapper do método evaluate que pode ser passadas para funções como `integral`*

# Raízes (.raizes)

Módulo com funções de busca de raíz e cálculo de número de raízes.


## Funções

`secante(f, a, b, tol)`, `bissecao(f, a, b, tol)`

[✅] Status: Concluído

```python
secante(f: Callable, a: float, b: float, tol: float) -> float
bissecao(f: Callable, a: float, b: float, tol: float) -> float
```

**Entrada:**
- f: Função a ser analizada
- a: Intervalo inicial da função f
- b: Intervalo final da função f
- tol: Tolerancia para o erro da aproximação final

**Retorno:**
- float: Aproximação da raiz da função no intervalo [a, b]

`newton_raphson(f, df, a, tol)`

[✅] Status: Concluído

```python
newton_raphson(f: Callable, df: Callable, a:float, tol: float)
```

**Entrada:**
- f: Função a ser analizada
- df: Derivada de f
- a: Ponto inicial da função f
- tol: Tolerancia para o erro da aproximação final

**Retorno:**
- float: Aproximação da raiz da função encontrada.

