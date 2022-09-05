from .. import app

from flask import jsonify

@app.route("/ping")
def  ping():
    return jsonify(success=True ,option= {"name":"zy"})



@app.route("/test")
def test():
    return jsonify({"hi":1})