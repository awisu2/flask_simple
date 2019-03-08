from flask import Blueprint, current_app as app, render_template

BP_URL_PREFIX='/index2'
BP_NAME=BP_URL_PREFIX
bp = Blueprint(BP_NAME, __name__, url_prefix=BP_URL_PREFIX)

@bp.route('/', methods=['GET'])
@bp.route('/<name>', methods=['GET'])
def index(name=''):
  return render_template('index.html')
