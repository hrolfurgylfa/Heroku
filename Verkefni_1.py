from sys import argv
from bottle import *

@route("/")
def index():
    return """
    <h2>Verkefni 1</h2>
    <a href="/um">Um mig</a>
    <a href="/aefisaga">Aefisaga min</a>
    <a href="/myndir">Myndir af mer</a>
"""

@route("/um")
def um():
    return "Herna eru upplysingar um mig"

@route("/aefisaga")
def aefisaga():
    return "Herna er aefisagan min"

@route("/myndir")
def myndir():
    return "Herna eru myndir af mer"

bottle.run(host='0.0.0.0', port=argv[1])