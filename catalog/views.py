from django.shortcuts import render
from pathlib import Path
import json
from django.http import HttpResponse

# Create your views here.
def index(request):
    path = Path('catalog/db.json')
    dbase = json.loads(path.read_text())
    list = dbase["Список организаций"]
    num_organizations = len(list)
    num_orders = 0
    for organization in list:
        num_orders += len(organization["orders"])
    return render(request, "index.html", {"db": list, "num_organizations": num_organizations, "num_orders": num_orders})

def organizations(request):
    path = Path('catalog/db.json')
    dbase = json.loads(path.read_text())
    list = dbase["Список организаций"]
    return render(request, "organizations.html", {"db": list})

def organizationInfo(request):
    if request.method == 'GET':
        name = request.GET.get('name')
    print(name)
    path = Path('catalog/db.json')
    dbase = json.loads(path.read_text())
    for organization in dbase["Список организаций"]:
        if organization["name"] == name:
            break
    return render(request, "organizationInfo.html", {"organization": organization})

def orders(request):
    path = Path('catalog/db.json')
    dbase = json.loads(path.read_text())
    list = dbase["Список организаций"]
    return render(request, "orders.html", {"db": list})

def orderInfo(request):
    path = Path('catalog/db.json')
    dbase = json.loads(path.read_text())
    name = request.GET.get('name')
    title = request.GET.get('title')
    for organization in dbase["Список организаций"]:
        if organization["name"] == name:
            for order in organization["orders"]:
                if order["title"] == title:
                    print(order)
                    break
            break
    return render(request, "orderInfo.html", {"order": order, "organization": name})

def authentication(request):
    return render(request, "authentication.html")

def auth(request):
    login = request.POST.get("login")
    password = request.POST.get("password")
    print(login)
    print(password)
    path = Path('catalog/db.json')
    dbase = json.loads(path.read_text())
    for user in dbase["users"]:
        if user["status"] == "admin" and login == user["login"] and password == user["password"]:
            return render(request, "admin.html", {"db": dbase["Список организаций"]})
    else:
        return render(request, "index.html")

def addOrder(request):
    title = request.POST.get("title")
    organizationName = request.POST.get("organization")
    description = request.POST.get("description")
    customerName = request.POST.get("customerName")
    customerSecondname = request.POST.get("customerSecondname")
    startdate = request.POST.get("startdate")
    enddate = request.POST.get("enddate")
    status = request.POST.get("status")
    print(title)
    print(organizationName)
    path = Path('catalog/db.json')
    dbase = json.loads(path.read_text())
    order = {
        "title":title,
        "description": description,
        "customer": {
            "name": customerName,
            "secondname": customerSecondname
            },
        "startdate": startdate,
        "enddate": enddate,
        "status": status
    }
    for organization in dbase["Список организаций"]:
        if organization["name"] == organizationName:
            organization["orders"].append(order)
    path.write_text(json.dumps(dbase, ensure_ascii=False, indent=4))
    return render(request, "admin.html", {"db": dbase["Список организаций"]})

def addOrganization(request):
    name = request.POST.get("name")
    directorName = request.POST.get("directorName")
    directoSecondname = request.POST.get("directoSecondname")
    dateOfBirth = request.POST.get("dateOfBirth")
    print(name)
    print(directorName)
    path = Path('catalog/db.json')
    dbase = json.loads(path.read_text())
    organization = {
        "name": name,
        "director": {
            "name": directorName,
            "secondname": directoSecondname,
            "dateOfBirth": dateOfBirth
            },
        "orders": []
    }
    dbase["Список организаций"].append(organization)
    path.write_text(json.dumps(dbase, ensure_ascii=False, indent=4))
    return render(request, "admin.html", {"db": dbase["Список организаций"]})

def removeOrganization(request):
    organizationName = request.POST.get("organization")
    path = Path('catalog/db.json')
    dbase = json.loads(path.read_text())
    for organization in dbase["Список организаций"]:
        if organization["name"] == organizationName:
            dbase["Список организаций"].remove(organization)
    path.write_text(json.dumps(dbase, ensure_ascii=False, indent=4))
    return render(request, "admin.html", {"db": dbase["Список организаций"]})

def removeOrder(request):
    orderTitle = request.POST.get("order")
    path = Path('catalog/db.json')
    dbase = json.loads(path.read_text())
    for organization in dbase["Список организаций"]:
        for order in organization["orders"]:
            if order["title"] == orderTitle:
                organization["orders"].remove(order)
    path.write_text(json.dumps(dbase, ensure_ascii=False, indent=4))
    return render(request, "admin.html", {"db": dbase["Список организаций"]})
