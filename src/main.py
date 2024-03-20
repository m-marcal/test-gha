import os
import requests
import sys


NON_PROD_URL = 'https://www.google.com'
PROD_URL     = 'https://www.google.com'

PORTS_BY_ENV = {
    'DEV1':  [1234, 4567, 8910],
    'DEV2':  [1234, 4567, 8910],
    'TEST':  [1234, 4567, 8910],
    'INT':   [1234, 4567, 8910],
    'PrePROD': [1234, 4567, 8910],
    'PROD':  [1234, 4567, 8910]
}

def clear_dispatcher_cache(env: str):
    
    if env not in PORTS_BY_ENV:
        print(f"Environment {env} is not supported!")
        raise Exception
    
    # Use non-prod endpoint
    for port in PORTS_BY_ENV.get(env):
        resp = None
        if env != 'PROD':
            resp = requests.get(f"{NON_PROD_URL}")
        else: 
            resp = requests.get(f"{NON_PROD_URL}")
        print(resp)

if __name__ == '__main__':
    env = sys.argv[1]
    clear_dispatcher_cache(env)