from loguru import logger

logger.add("meu_log.log", level="CRITICAL")

def soma(x, y):
    try:
        soma = x + y
        logger.info(f"A soma de {x} e {y} é {soma}")
        return soma
    except:
        logger.critical("Você tem que digitar valores corretos")


soma(3, 5)
soma(2, 5)
soma(3, "5")