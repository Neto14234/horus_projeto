import datetime
from app import app
from flask import render_template, request, flash, redirect, url_for, session
from app.models.models import db
from app.models.User import User
from app.models.cvli import Cvli
from app.models.fotos import Fotos


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(minutes=60*24*30)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':

        req = request.form
        missing = list()

        for k, v in req.items():
            if v == "":
                missing.append(k)
        
        if missing:
            feedback = f"Campos vazios para {', '.join(missing)}"
            flash(feedback, 'alert-danger')
            return redirect(url_for('login'))
        
        
        user = User.query.filter_by(email=request.form['email']).first()
        if user:
            if user.senha == request.form['password']:
                session['id_user'] = user.id
                return redirect(url_for('dashboard'))
            else:
                flash('senha incorreta', 'alert-danger')
                return redirect(url_for('login'))
        else:
            flash('Nenhum usuário foi encontrado', 'alert-danger')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route("/cadastro", methods=["GET", "POST"])   
def cadastro():
    if request.method == 'POST':
        req = request.form
        missing = list()

        for k, v in req.items():
         if v == "":
                 missing.append(k)
        
        if missing:
         feedback = f"Campos vazios para {', '.join(missing)}"
         flash(feedback, 'alert-danger')
         return redirect(url_for('cadastro'))
        user = User()
        user.nome=request.form['nome_completo']
        user.email=request.form['email']
        user.cpf=request.form['cpf']
        user.senha=request.form['password']
        session['id_user'] = user.id
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('cadastro.html')

@app.route("/dashboard")
def dashboard():
    if 'id_user' in session:
        id_user = session['id_user']
        cvlis = Cvli.query.all()
        print(cvlis)
        return render_template('dashboard.html', cvlis=cvlis)
    return redirect(url_for('login'))

@app.route("/cadastrocvli", methods=["GET", "POST"])
def cvli():
    if 'id_user' in session:
        id_user = session['id_user']
        if request.method == 'POST':

            if request.method == 'POST':
                req = request.form
                missing = list()

                for k, v in req.items():
                    if v == "":
                        missing.append(k)
                
                if missing:
                    feedback = f"Campos vazios para {', '.join(missing)}"
                    flash(feedback, 'alert-danger')
                    return redirect(url_for('cvli'))
                cvli = Cvli()
                date_time_obj = datetime.datetime.fromisoformat(request.form['data']) 
                cvli.data = date_time_obj 
                cvli.hora = request.form['hora']
                cvli.local = request.form['local']
                cvli.ocorrido = request.form['ocorrido']
                cvli.id_usuario = id_user
                db.session.add(cvli)
                db.session.commit()
                return redirect(url_for('dashboard'))
                
        return render_template('cvli.html')
    return redirect(url_for('login'))

@app.route("/logout")   
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route("/editar/<id>", methods=["GET", "POST"])
def editar(id):
    if 'id_user' in session:
        id_user = session['id_user']
        cvli=Cvli.query.get(id)
        if request.method == "POST":
            cvli.data = request.form['data']
            cvli.hora = request.form['hora']
            cvli.local = request.form['local']
            cvli.ocorrido = request.form['ocorrido']
            db.session.commit()
            return redirect(url_for('dashboard'))
        return render_template("editar.html", cvli=cvli)
    return redirect(url_for('login'))

@app.route("/deletar/<id>")
def deletar(id):
    cvli=Cvli.query.get(id)
    if cvli:
        db.session.delete(cvli)
        db.session.commit()
    return redirect(url_for('dashboard'))

#  CRUD 2

@app.route("/users")
def users():
    users = User.query.all()
    return render_template("admin/usuarios.html", users=users)

@app.route("/users/delete/<id>")
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("users"))







