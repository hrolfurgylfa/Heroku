#TIL KENNARA!!!
#       |
#       |
#       V
#Til þess að finna Verkefni 1 þarf að fara á https://hrolfurgylfa.herokuapp.com/Verkefni_1 og til þess að finna verkefni tvö þarf að fara á https://hrolfurgylfa.herokuapp.com/Verkefni_2

from sys import argv
import bottle
from bottle import *


#Verkefni 1----------Verkefni 1----------Verkefni 1----------Verkefni 1----------Verkefni 1
@route("/Verkefni_1")
def Verkefni_1():
    return """
    <h2>Verkefni 1</h2>
    <a href="/um">Um mig</a>
    <a href="/aefisaga">Aefisaga min</a>
    <a href="/myndir">Myndir af mer</a>
"""

#Um
@route("/Verkefni_1/um")
def um():
    return "Herna eru upplysingar um mig"

#Æfisaga
@route("/Verkefni_1/aefisaga")
def aefisaga():
    return "Herna er aefisagan min"

#Myndir
@route("/Verkefni_1/myndir")
def myndir():
    return "Herna eru myndir af mer"

#Verkefni 2----------Verkefni 2----------Verkefni 2----------Verkefni 2----------Verkefni 2
@route("/Verkefni_2")
def Verkefni_2():
    return """
    <h1>Verkefni 2</h1>
    <a href="/Verkefni_2/lidur_A">Liður A</a> - 
    <a href="/Verkefni_2/lidur_B">Lidur B</a>
    """
#Liður A
@route("/Verkefni_2/lidur_A")
def lidur_a():
    return """
    <h1>Verkefni 2 - Liður A</h1>
    <a href="/Verkefni_2/sida/1">Síða 1</a>
    <a href="/Verkefni_2/sida/2">Síða 2</a>
    <a href="/Verkefni_2/sida/3">Síða 3</a>
    """
#Liður B
@route("/Verkefni_2/lidur_B")
def lidur_b():
    return """
    <h2>Verkefni 2 - Liður A</h2>
    <h3>Veldu uppáhalds staf</h3>
    <img src="/Myndir/A.jpg">
    <img src="Myndir/B.jpg">
    <img src="Myndir/C.jpg">
    <img src="Myndir/D.jpg">
    """
#Liður A
@route("/Verkefni_2/sida/<id:int>")
def page(id):
    if id == 1:
        return "Þetta er síða 1<br><a href='/Verkefni_2/lidur_A'>Til baka</a>"

    elif id == 2:
        return "Þetta er síða 2<br><a href='/Verkefni_2/lidur_A'>Til baka</a>"

    elif id == 3:
        return "Þetta er síða 3<br><a href='/Verkefni_2/lidur_A'>Til baka</a>"

    else:
        return '<h2 style="color:red;text-align: center;">Þessi síða finnst ekki</h2>'

@route("/Verkefni_3")
def index_V3():
    gogn = {"title": "Modular template", "content": "<h3>Halló Modular templates!</h3>", "footer": "Höfundur &copy; 2018 Hrólfur Gylfason"}
    
    return template("Aðaltemplates/base.tpl", gogn)

# 1
@route("/Verkefni_3/page1")
def index1():
    return template("Verkefni_3/page-1.tpl")

# 2
@route("/Verkefni_3/page2")
def index2():
    return template("Verkefni_3/page-2.tpl")

# 3
@route("/Verkefni_3/page3")
def index3():
    return template("Verkefni_3/page-3.tpl", nafn="Hrólfur")

# 4
@route("/Verkefni_3/page4")
def index4():
    dict1 = {"number": 123, "street": "MyStreet", "city": "MyCity"}

    return template("Verkefni_3/page-4.tpl", dict1)

# 5
@route("/Verkefni_3/page5")
def index5():
    dict1 = {"title": "Vocaloids", "names": ["Miku", "Luka", "Len", "Rin"]}

    return template("Verkefni_3/page-5.tpl", dict1)

#Til þess að setja inn myndir
@route('/Myndir/<skra:path>')
def server_static(skra):
    return static_file(skra, root='Myndir')

#404 ERROR síða----------404 ERROR síða----------404 ERROR síða----------404 ERROR síða----------404 ERROR síða
@error (404)
def notFound(error):
    return '<h2 style="color:red;text-align: center;">Þessi síða finnst ekki</h2>'


#bottle.run(host="localhost", port=8080, reloader=True, debug=True)
bottle.run(host='0.0.0.0', port=argv[1])
