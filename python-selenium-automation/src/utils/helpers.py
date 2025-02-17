def load_env():
    """Carrega variáveis de ambiente do arquivo .env."""
    from dotenv import load_dotenv
    import os

    load_dotenv()

def get_env_variable(var_name):
    """Retorna o valor da variável de ambiente especificada."""
    import os
    return os.getenv(var_name)

def print_message(message):
    """Imprime uma mensagem no console."""
    print(message)