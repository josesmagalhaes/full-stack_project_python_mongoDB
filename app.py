from flask import Flask, render_template, request, url_for, redirect, session
import pymongo
import bcrypt
#definir o aplicativo como uma instância do Flask 
app = Flask(__name__)
#a criptografia depende de chaves secretas para que possam ser executadas
app.secret_key = "testing"
#conecte-se ao seu banco de dados Mongodb
client = pymongo.MongoClient("mongodb+srv://root:root@cluster0.qqxjf.mongodb.net/test")

#pega o nome do banco de dados
db = client.get_database('soulcode')
#obter a coleção particular que contém os dados
records = db.register


#Roteamento do aplicativo Flask
#atribuir URLs para ter uma rota particular
@app.route("/", methods=['post', 'get'])
def index():
    message = ''
    #se método postar no índex
    if "email" in session:
        return redirect(url_for("logged_in"))
    if request.method == "POST":
        user = request.form.get("fullname")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        #se for encontrado no mostruário do banco de dados que foi encontrado
        user_found = records.find_one({"name": user})
        email_found = records.find_one({"email": email})
        if user_found:
            message = 'Já existe um usuário com este nome'
            return render_template('index.html', message=message)
        if email_found:
            message = 'Já existe um email com este título no banco de dados'
            return render_template('index.html', message=message)
        if password1 != password2:
            message = 'Senhas devem ser iguais!'
            return render_template('index.html', message=message)
        else:
            #hash a senha e codificá-la
            hashed = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
            #atribua-os em um dicionário em pares de valores-chave
            user_input = {'name': user, 'email': email, 'password': hashed}
            #insira-o na coleção de discos
            records.insert_one(user_input)
            
            #encontre a nova conta criada e seu e-mail
            user_data = records.find_one({"email": email})
            new_email = user_data['email']
            #se registrado, redirecionar para logado como o usuário registrado
            return render_template('logged_in.html', email=new_email)
    return render_template('index.html')



@app.route("/login", methods=["POST", "GET"])
def login():
    message = 'Por favor, logue em sua conta!'
    if "email" in session:
        return redirect(url_for("logged_in"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        #check if email exists in database
        email_found = records.find_one({"email": email})
        if email_found:
            email_val = email_found['email']
            passwordcheck = email_found['password']
            #encode the password and check if it matches
            if bcrypt.checkpw(password.encode('utf-8'), passwordcheck):
                session["email"] = email_val
                return redirect(url_for('logged_in'))
            else:
                if "email" in session:
                    return redirect(url_for("logged_in"))
                message = 'Senha incorreta!'
                return render_template('login.html', message=message)
        else:
            message = 'Email não encontrado!'
            return render_template('login.html', message=message)
    return render_template('login.html', message=message)

@app.route('/logged_in')
def logged_in():
    if "email" in session:
        email = session["email"]
        return render_template('logged_in.html', email=email)
    else:
        return redirect(url_for("login"))

@app.route("/logout", methods=["POST", "GET"])
def logout():
    if "email" in session:
        session.pop("email", None)
        return render_template("signout.html")
    else:
        return render_template('index.html')







if __name__ == "__main__":
  app.run(debug=True)
