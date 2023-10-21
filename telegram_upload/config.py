import json
import os

import click


#CONFIG_DIRECTORY = os.environ.get('TELEGRAM_UPLOAD_CONFIG_DIRECTORY', '~/.config')
#CONFIG_FILE = os.path.expanduser('{}/telegram-upload.json'.format(CONFIG_DIRECTORY))

# Ottieni il percorso assoluto dello script corrente
current_script_directory = os.path.abspath(os.path.dirname(__file__))

# Utilizza il percorso della cartella dello script come valore predefinito per CONFIG_DIRECTORY
CONFIG_DIRECTORY = os.environ.get('TELEGRAM_UPLOAD_CONFIG_DIRECTORY', current_script_directory)
SESSION_FILE = os.path.expanduser('{}/telegram-upload'.format(CONFIG_DIRECTORY))


def prompt_config(config_file):
    os.makedirs(os.path.dirname(config_file), exist_ok=True)
    click.echo('Go to https://my.telegram.org and create a App in API development tools')
    api_id = click.prompt('Please Enter api_id', type=int)
    api_hash = click.prompt('Now enter api_hash')
    with open(config_file, 'w') as f:
        json.dump({'api_id': api_id, 'api_hash': api_hash}, f)
    return config_file


def default_config():
    if os.path.lexists(CONFIG_FILE):
        return CONFIG_FILE
    return prompt_config(CONFIG_FILE)
