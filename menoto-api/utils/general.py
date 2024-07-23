import os

def get_env(key):
    # Check if environment is loca, dev, production
    if os.environ['ENV'] == 'local':
        return os.environ[key]
    else:
        # Secrets manager
        return "NO"
