from flask import render_template, request

def cnn():
    if request.method == 'POST':
        try:
            data = request.get_json()
            print(data)
            return {
                'status': 200,
                'message': "Funcionou"
            }
        except Exception as error: 
            return "Não foi possível enviar a imagem. Erro: {}".format(str(error)), 400
    else: 
        return "Método não aceito", 405