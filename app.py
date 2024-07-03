from flask import Flask
from controllers.pessoa_controller import pessoa_controller

app = Flask(__name__)
app.debug = True
app.register_blueprint(pessoa_controller)

# configuracao de debugger;
# if __name__ == "__main__":
#     app.run(debug=True)