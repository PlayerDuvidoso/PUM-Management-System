from flask import Blueprint, render_template, request
from database import users

user_route = Blueprint('user', __name__)

"""
Users Route

    - /users/ (GET) - Listar os users
    - /users/ (POST) - Inserir o cliente no servidor
    - /users/new (GET) - renderizar o formulario para criar um cliente
    - /users/<id> (GET) - obter os dados de um cliente
    - /users/<id>/edit (GET) - renderizar o formulario para edição do cliente
    - /users/<id>/update (PUT) - atualizar informações do cliente
    - /users/<id>/delete (DELETE) - remove o cliente do banco de dados


"""


@user_route.route('/', methods=['GET', 'POST'])
def user_list():

    if request.method == 'GET':

        return render_template('user_list.html', status='', users=users.users)
    
    elif request.method == 'POST':

        if 'username' in request.form.keys() and request.form.get('username').strip() != '':
            username = request.form.get('username').strip()
            
            if 'email' in request.form.keys() and request.form.get('email').strip() != '':
                email = request.form.get('email').strip().lower()

                status = users.create_user(username, email)

                return render_template('user_list.html', status=status, users=users.users)

@user_route.route('/new')
def user_new(): #Renderizar o formulario para criar um client
    return render_template('user_form.html')

@user_route.route('/<int:id>')
def user_id(id): #Obter os dados de um cliente
    pass

@user_route.route('/<int:id>/edit')
def user_edit(id): #Renderizar o formulario para edição do cliente
    pass

@user_route.route('/<int:id>/update', methods=['PUT'])
def user_update(id): #Atualizar informações do cliente
    pass

@user_route.route('/<int:id>/delete', methods=['DELETE'])
def user_delete(id): #Remove o cliente do banco de dados
    
    users.delete_user(id)

    return render_template('user_list.html', status='', users=users.users)