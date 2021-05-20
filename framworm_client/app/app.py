#Imports
from flask             import Flask, url_for, redirect ,render_template, request
from secrets           import token_bytes
from json              import loads
from os.path           import exists
from base64            import b64decode
from pygrok            import Grok

#Fonctions
def parse(log):
    grok      = Grok("<%{WORD:type}:%{WORD:severity}>%{TIMESTAMP_ISO8601:timestamp}%{SPACE}%{IP:ip}:%{IPORHOST:host}%{SPACE}%{GREEDYDATA:data}")
    l         = grok.match(log)
    l["data"] = b64decode(bytes.fromhex(l["data"])).decode()
    return l
    
def get_logs():
    """
    :return: Liste de dicts {type, severity, timestamp, host, data}
    """
    if not exists("logs.json"): open("logs.json", "a+")
    with open("logs.json", "r+") as f:
        return [parse(x.strip()) for x in f.readlines()]

def push_logs(logs):
    """
    :param logs: Liste de logs
    """
    with open("logs.json", "a+") as f:
        for log in logs:
            f.write(log + "\n")

#Applications
app            = Flask(__name__)
app.secret_key = token_bytes(24)

@app.route("/")
def root():
    return redirect(url_for("index"))

@app.route("/index.html")
def index():
    return render_template("index.html.j2", logs=get_logs(), site_root="http://192.168.200.1:8000")

@app.route("/get", methods=["POST"])
def get():
    if request.method == "POST":
        data = loads(b64decode(request.get_data()).decode())
        push_logs(data)
        return ""

@app.route("/get_all_logs")
def get_all_logs():
    l = get_logs()
    data = ""
    for element in l:
        data += f"""
    <tr>
            <td>{ element["type"] }</td>
            <td>{ element["severity"] }</td>
            <td>{ element["timestamp"] }</td>
            <td>{ element["ip"] }</td>
            <td>{ element["host"] }</td>
            <td>{ element["data"] }</td>
        </tr>"""
    html = f"""    <div class="table-wrapper">
<table class="fl-table">
        <thead>
        <tr>
            <th>Type</th>
            <th>Sévérité</th>
            <th>Timestamp</th>
            <th>IP</th>
            <th>Hôte</th>
            <th>Contenu</th>
        </tr>
        </thead>
        <tbody>

        {data}
        <tbody>
    </table></div>
"""
    return html