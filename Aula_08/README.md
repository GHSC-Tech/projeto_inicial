# Aula 08: Funções em Python - ETL com Pandas, JSON e Parquet

## Visão Geral
Nesta aula aprendi a realizar um processo **ETL (Extract, Transform, Load)** utilizando Python e a biblioteca **Pandas**.  
No início parecia complexo, mas conforme fui praticando, percebi que cada etapa tem sua lógica e que juntas formam um fluxo poderoso para manipulação de dados.

---

## Passos do ETL

- **Extract**: Ler dados de um arquivo JSON.  
- **Transform**: Concatenar os dados em um único DataFrame e aplicar transformações.  
- **Load**: Salvar o resultado em um arquivo CSV ou PARQUET.  

Essa sequência me mostrou como é possível organizar dados de forma prática e reutilizável.

---

## Logging com Loguru

Durante a aula também aprendi sobre **logging** e como usar a biblioteca **Loguru**.  
Antes eu achava que logging era algo distante, mas percebi que é essencial para entender o que o programa está fazendo e diagnosticar erros.

### O que é Logging?
Logging é o processo de registrar mensagens sobre eventos que acontecem durante a execução do software.  
Essas mensagens podem indicar progresso, avisos ou erros, e são fundamentais para depuração e manutenção.

### Instalação
poetry add loguru

### Exemplos de Uso
### Decoradores com Loguru

Aprendi também a criar um decorador para adicionar logs automaticamente às funções. Isso facilita muito, pois não preciso modificar o corpo da função para registrar informações.

from loguru import logger

def log_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando '{func.__name__}' com {args} e {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"'{func.__name__}' retornou {result}")
            return result
        except Exception as e:
            logger.exception(f"'{func.__name__}' lançou uma exceção: {e}")
            raise
    return wrapper

### Aplicando o Decorador

@log_decorator
def soma(a, b):
    return a + b

@log_decorator
def falha():
    raise ValueError("Erro intencional")

soma(5, 3)
try:
    falha()
except ValueError:
    pass

### Benefícios que Percebi
- Código mais limpo e organizado.

- Facilidade para depuração e monitoramento.

- Reutilização de lógica de logging em várias funções.

- Melhor entendimento do fluxo de execução do programa.

### Conclusão
Essa aula me mostrou como unir ETL com Pandas e logging com Loguru para criar programas mais robustos e fáceis de manter. Agora consigo enxergar a importância de registrar informações e como isso pode facilitar tanto no aprendizado quanto em projetos reais.


