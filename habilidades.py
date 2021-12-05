from flask_restful import Resource


lista_habilidades = ['Python', 'Flask', 'django', 'SQL', 'html', 'CSS', 'javaScript', 'PHP', 'RUBY', 'React']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades
