from flask import Blueprint, render_template, request

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


@user_route.route('/')
def user_list():

    return render_template('user_list.html')

@user_route.route('/', methods=['POST'])
def user_insert():

    print('I got called')

    return render_template('user_list.html')

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
    pass