from controllers.cnnController import cnn

def cnnRoutes(app): 
    app.route('/cnn', methods=['POST'])(cnn)