# import whatever modules/functions/classes that we need for our code to work as intended

from flask import render_template
from flask.blueprints import Blueprint


# each webpage is defined/controlled by a flask rout -> which is a python function 

site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    return render_template('index.html')