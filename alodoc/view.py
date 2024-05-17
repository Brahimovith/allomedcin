from flask import Flask, render_template, url_for, request, redirect, flash
from flask_login import LoginManager, login_user, logout_user, login_required
from .inscription import RegistrationForm
from .connexion import LoginForm
from .doctor import Docteurform
from .utils import save_new_client_en_db, authenticate
from .utils import save_new_doc_en_db
import sqlalchemy as sa

app = Flask(__name__)

app.config.from_object('config')

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/rendezvous')
def rdv():
    from .models import doctorvalide
    from .rdv import Rendezvous
    form = Rendezvous()
    doc = doctorvalide.query.all()
    form.i.choices=[(a.id, a.id) for a in doctorvalide.query.all()]
    if form.validate_on_submit():
        select=form.i.data
        date =form.date.data

    return render_template('rdv.html', form= form,doc=doc)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Traitez les données
        print("hhh")
        username = form.username.data
        email = form.email.data
        password = form.password.data
        nom = form.nom.data
        prenom = form.prenom.data
        sexe = form.genre.data
        adresse= form.adresse.data
        ville= form.ville.data
        pays= form.pays.data
        age = form.age.data
        save_new_client_en_db(username,email,password,nom,prenom,sexe,adresse,ville,pays,age)
        return redirect('/')

    return render_template('inscription.html', form=form,title="Registration Form" )


@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    from .models import client 
    from .models import db  
    form = LoginForm()
    
    if form.validate_on_submit():
        # Ici, vous pouvez appeler une fonction pour vérifier les informations de connexion
        # Par exemple, vous pouvez rechercher dans votre base de données si l'utilisateur existe et si le mot de passe est correct
        if authenticate(form.username.data, form.password.data):
            flash('Connexion réussie !', 'success')
            user = client.query.filter_by(username=form.username.data).first()
            login_user(user)
            return redirect('/')
        else:
            flash('Nom d\'utilisateur ou mot de passe incorrect', 'danger')
    return render_template('connexion.html', form=form,title = 'connexion')


@login_manager.user_loader
def load_user(user_id):
    # récupérer l'utilisateur à partir de votre base de données.
    from .models import client 
    from .models import db 
    return client.query.get(int(user_id))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/profile')
@login_required
def profile():
    return 'Bienvenue sur votre profil !'




@app.route('/doctor', methods=['GET', 'POST'])
def doctor():
    formulaire = Docteurform()
    if formulaire.validate_on_submit():
        nom = formulaire.nom.data
        prenom = formulaire.prenom.data
        sexe = formulaire.genre.data
        adresse= formulaire.adresse.data
        ville= formulaire.ville.data
        pays= formulaire.pays.data
        age = formulaire.age.data
        spe= formulaire.spe.data
        mail= formulaire.email.data
        save_new_doc_en_db(nom,prenom,sexe,age, adresse,ville,pays,spe,mail)
        flash('on va vous contacter')
        return redirect('/')
    return render_template('doctor.html', form = formulaire,title ='Docteur inscription')


@app.route('/admin/', methods=['GET', 'POST'])
@app.route('/admin', methods=['GET', 'POST'])
def page_adm_doc():
    from .models import doctor 
    from .models import db  
    from .models import doctorvalide
    docteurs = doctor.query.all()
    doc = doctorvalide.query.all()
    return render_template('page_adm_doc.html',doc=doc, docteurs=docteurs,title= 'Admin')

@app.route('/admin/ajouter_docteur/<int:docteur_id>', methods=['POST'])
def ajouter_docteur(docteur_id):
    from .models import doctor 
    from .models import doctorvalide
    from .models import db
    docteur_provisoire = doctor.query.get_or_404(docteur_id)
    nouveau_docteur = doctorvalide(first_name=docteur_provisoire.first_name,last_name =docteur_provisoire.last_name,age = docteur_provisoire.age,gender= docteur_provisoire.gender,address=docteur_provisoire.address,city=docteur_provisoire.city,country=docteur_provisoire.country,specialite=docteur_provisoire.specialite,email=docteur_provisoire.email)
    db.session.add(nouveau_docteur)
    db.session.delete(docteur_provisoire)
    db.session.commit()
    return redirect(url_for('page_adm_doc'))

@app.route('/admin/supprimer_docteur/<int:docteur_id>', methods=['POST'])
def supprimer_docteur(docteur_id):
    from .models import doctor 
    from .models import doctorvalide
    from .models import db 
    docteur_provisoire = doctor.query.get_or_404(docteur_id)
    db.session.delete(docteur_provisoire)
    db.session.commit()
    return redirect(url_for('page_adm_doc'))





if __name__ == "__main__":
    app.run()