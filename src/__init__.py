import connexion
import json


# set up the connexion app
connexionApp = connexion.App(__name__, specification_dir='../swagger')
app = connexionApp.app # initialize the flask app from the connexion app
app.json_encoder = json.JSONEncoder
connexionApp.add_api('swagger.yaml') # load the yaml file
