
import requests
import random

FOAAS_URL = "https://foaas.com"
ENDPOINTS = [
    "/absolutely/:company/:from",
    "/anyway/:company/:from",
    "/asshole/:from",
    "/awesome/:from",
    "/back/:name/:from",
    "/bag/:from",
    "/ballmer/:name/:company/:from",
    "/bday/:name/:from",
    "/because/:from",
    "/blackadder/:name/:from",
    "/bm/:name/:from",
    "/bucket/:from",
    "/bus/:name/:from",
    "/bye/:from",
    "/chainsaw/:name/:from",
    "/cocksplat/:name/:from",
    "/cool/:from",
    "/cup/:from",
    "/dalton/:name/:from",
    "/dense/:from",
    "/deraadt/:name/:from",
    "/diabetes/:from",
    "/donut/:name/:from",
    "/dumbledore/:from",
    "/equity/:name/:from",
    "/even/:from",
    "/everyone/:from",
    "/everything/:from",
    "/family/:from",
    "/fascinating/:from",
    "/fewer/:name/:from",
    "/flying/:from",
    "/ftfy/:from",
    "/fts/:name/:from",
    "/fyyff/:from",
    "/gfy/:name/:from",
    "/give/:from",
    "/holygrail/:from",
    "/horse/:from",
    "/idea/:from",
    "/immensity/:from",
    "/ing/:name/:from",
    "/jinglebells/:from",
    "/keep/:name/:from",
    "/keepcalm/:reaction/:from",
    "/king/:name/:from",
    "/legend/:name/:from",
    "/life/:from",
    "/linus/:name/:from",
    "/logs/:from",
    "/look/:name/:from",
    "/looking/:from",
    "/lowpoly/:from",
    "/madison/:name/:from",
    "/maybe/:from",
    "/me/:from",
    "/mornin/:from",
    "/no/:from",
    "/nugget/:name/:from",
    "/off/:name/:from",
    "/outside/:name/:from",
    "/particular/:thing/:from",
    "/pink/:from",
    "/problem/:name/:from",
    "/programmer/:from",
    "/question/:from",
    "/ratsarse/:from",
    "/retard/:from",
    "/ridiculous/:from",
    "/rockstar/:name/:from",
    "/rtfm/:from",
    "/sake/:from",
    "/shakespeare/:name/:from",
    "/shit/:from",
    "/shutup/:name/:from",
    "/single/:from",
    "/thanks/:from",
    "/that/:from",
    "/think/:name/:from",
    "/thinking/:name/:from",
    "/this/:from",
    "/thumbs/:name/:from",
    "/too/:from",
    "/tucker/:from",
    "/understand/:name/:from",
    "/version",
    "/waste/:name/:from",
    "/what/:from",
    "/xmas/:name/:from",
    "/yeah/:from",
    "/yoda/:name/:from",
    "/you/:name/:from",
    "/zayn/:from",
    "/zero/:from"
]

header = {
    "Accept": "application/json"
}

def foaas(name):

    request_url = f"{FOAAS_URL}{random.choice(ENDPOINTS)}"

    if ":name" in request_url:
        populated_url = request_url.replace(":name", name)
        request_url = populated_url

    if ":company" in request_url:
        populated_url = request_url.replace(":company", name)
        request_url = populated_url

    if ":from" in request_url:
        populated_url = request_url.replace(":from", "Mookie")

    r = requests.get(populated_url, headers=header)

    response_json = r.json()

    return response_json.get("message")