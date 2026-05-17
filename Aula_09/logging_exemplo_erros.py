from loguru import logger

logger.debug("Iniciando o programa") #"Um aviso para o desenvolvedor (ou eu mesmo) no futuro"
logger.info("Realizando uma operação de divisão") # Informacao importante do processo
logger.warning("Cuidado! A divisão por zero pode ocorrer.") # Um aviso que algo vai parar de funcionar no futuro
logger.error("Erro! A divisão por zero ocorreu.") # Um erro que ocorreu, mas o programa continua rodando
logger.critical("Erro crítico! O programa não pode continuar.") # Um erro que ocorreu e o programa não pode continuar