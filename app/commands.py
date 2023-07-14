import click
from app.models import db
from app.models.book import Book
from app.models.log import Log
from app.models.role import Role
from app.models.user_role import UserRole
from app.models.user import User

from flask import Blueprint


bp = Blueprint('commands', __name__, cli_group='setup')


def __create_tables():
    # create tables
    click.echo('Creating tables')
    db.create_all()
    click.echo('Done')


def __insert_demo_data():
    # insert some seed data for demo purposes
    click.echo('Inserting demo data')
    # add 2 roles: admin, and user
    click.echo('Inserting 2 roles: admin and user')
    role_1 = Role(name="admin")
    role_2 = Role(name="user")
    db.session.add_all([role_1, role_2])
    db.session.commit()

    # add two users
    click.echo('Inserting 2 users: an admin and a regular user')
    user_1 = User(first_name="Admin", last_name="User")
    user_2 = User(first_name="Regular", last_name="User")
    db.session.add_all([user_1, user_2])
    db.session.commit()

    # assign roles to users
    click.echo('Inserting user-role relationship')
    db.session.add_all(
        [
            UserRole(user_id=user_1.id, role_id=role_1.id),
            UserRole(user_id=user_2.id, role_id=role_2.id),
        ]
    )
    db.session.commit()

    # add a few books
    click.echo('Inserting 3 books')
    book_1 = Book(
        title="The Little Prince",
        author="Antoine de Saint-Exupéry",
        isbn="978-0152023980"
    )
    book_2 = Book(
        title="Learning Python",
        author="Mark Lutz",
        isbn="978-1449355739"
    )
    book_3 = Book(
        title="Unwinding Anxiety",
        author="Judson Brewer",
        isbn="978-0593421406"
    )
    db.session.add_all([book_1, book_2, book_3])
    db.session.commit()

    click.echo('Done')


@bp.cli.command('create-tables')
def create_tables():
    __create_tables()


@bp.cli.command('insert-demo-data')
def insert_demo_data():
    __insert_demo_data()


@bp.cli.command('all')
def all():
    # do it all
    __create_tables()
    __insert_demo_data()
