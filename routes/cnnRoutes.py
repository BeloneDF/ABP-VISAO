from controllers.cnnController import cnn


def cnnRoutes(app):
    app.route('/cnn', methods=['POST'])(cnn)
    app.route('/', methods=['GET'])(cnn)