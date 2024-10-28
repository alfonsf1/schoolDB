import click
import requests

API_URL= 'http://127.0.0.1:5000'

@click.group()
def cli():
    pass

@cli.command()
def get_students():
    response = requests.get(f'{API_URL}/students')
    print(response.json())

@cli.command()
@click.argument('identifier')
def get_students(identifier):
    response = requests.get(f'{API_URL}/students/{identifier}')
    print(response.json())

@cli.command()
@click.argument('identifier')
def get_students_by_name(identifier):
    response = requests.get(f'{API_URL}/students_by_name/{identifier}')
    print(response.json())

@cli.command()
def get_professors_classes():
    response = requests.get(f'{API_URL}/professors_classes')
    print(response.json())

if __name__ == '__main__':
    cli()
