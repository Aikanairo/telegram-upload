import json
import os

import click

@click.command()
@click.option('--config', default='~/.config', help='Specify the configuration directory')
def main(config):
    config_directory = os.path.expanduser(config)
    config_file = os.path.expanduser(os.path.join(config_directory, 'telegram-upload.json'))
    session_file = os.path.expanduser(os.path.join(config_directory, 'telegram-upload'))

    def prompt_config(config_file):
        os.makedirs(os.path.dirname(config_file), exist_ok=True)
        click.echo('Go to https://my.telegram.org and create an App in API development tools')
        api_id = click.prompt('Please Enter api_id', type=int)
        api_hash = click.prompt('Now enter api_hash')
        with open(config_file, 'w') as f:
            json.dump({'api_id': api_id, 'api_hash': api_hash}, f)
        return config_file

    def default_config():
        if os.path.lexists(config_file):
            return config_file
        return prompt_config(config_file)

    config_file = default_config()
    click.echo(f'Using config directory: {config_directory}')
    click.echo(f'Using config file: {config_file}')
    click.echo(f'Using session file: {session_file}')

if __name__ == '__main__':
    main()
