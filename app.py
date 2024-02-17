from flask import Flask, request, jsonify, render_template
from flask_humanize import Humanize

from lib.requestHelper import requestHelper

app = Flask(__name__, template_folder="templates")
humanize = Humanize(app)


@humanize.localeselector
def get_locale():
    return 'id_ID'


@app.route("/")
def index():
    request_helper = requestHelper()
    data = request_helper.get_count()
    return render_template(
        "index.html",
        data_paslon=data["data_paslon"],
        data_chart=data["chart"],
        data_table=data["data"],
        data_last_updated=data["last_updated"],
        data_progres=data["progres"],
    )


@app.route("/api")
def api():
    return jsonify({
        "message": "Welcome to API endpoint",
        "endpoints": [
            "/api/data-paslon",
            "/api/data-wilayah",
            "/api/data-table",
        ]
    })


@app.route("/api/data-paslon")
def data_paslon():
    request_helper = requestHelper()
    data = request_helper.get_paslon()
    return jsonify(data)


@app.route("/api/data-wilayah")
def data_wilayah():
    request_helper = requestHelper()
    data = request_helper.get_wilayah()
    return jsonify(data)


@app.route("/api/data-table")
def data_table():
    request_helper = requestHelper()
    data = request_helper.get_table()
    return jsonify(data)
