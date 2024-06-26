
def save_new_client_en_db(username,email,password,nom,prenom,sexe,adresse,ville,pays,age):
    from .models import client 
    from .models import db  
    print("je suis la")
    user = client(username=username,email=email,password=password,first_name=nom,last_name=prenom,gender=sexe,address=adresse,city=ville,country=pays,age=age)
    db.session.add(user)
    db.session.commit()
    print(user)

def authenticate(username, password):
    from .models import client 
    from .models import db
    user = client.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return True
    else:
        return False


def save_new_doc_en_db(nom,prenom,sexe,age,adresse,ville,pays,spe,mail):
    from .models import doctor 
    from .models import db  
    doc = doctor(first_name=nom,last_name =prenom,age =age,gender= sexe,address=adresse,city=ville,country=pays,specialite=spe,email=mail)
    db.session.add(doc)
    db.session.commit()