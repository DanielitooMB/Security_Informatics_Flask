from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from dotenv import load_dotenv
import os
from entities.account import Account
from entities.log import Log
from entities.user import User
from enums.log_type import LogType

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "index"

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@app.route('/movimiento')
@login_required
def movimiento():
    cuenta = Account.get_account_by_user(current_user.id)

    if not cuenta:
        return render_template('movimiento.html',
            cuenta=None,
            transacciones=[],
            balance=0.0
        )

    # El balance se calcula con las transacciones que ya vienen dentro de cuenta
    balance = sum(
        float(t.amount) if t.type.lower() in ('ingreso', 'income') else -float(t.amount)
        for t in cuenta.transactions
    )

    return render_template('movimiento.html',
        cuenta=cuenta,
        transacciones=cuenta.transactions,
        balance=balance
    )

@app.route('/api/users', methods=["POST"])
def create_user():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if User.check_email_exists(email):
        return jsonify({"success": False, "message": "El correo electrónico ingresado ya se encuentra registrado."}), 409

    if User.save(name, email, password):
        return jsonify({"success": True, "message": "Su cuenta fue creada correctamente."}), 201
    else:
        return jsonify({"success": False, "message": "Ocurrió un error al crear su cuenta. Intente de nuevo"}), 500

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = User.check_login(email, password)
    if user:
        #login is_active
        login_user(user)
        #Invocar el método
        Log.save_log(user, "TODO BIEN", LogType.LOGIN)
        return jsonify({
            "success": True,
            "message": "Sesión iniciada correctamente"
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Los datos de acceso ingresados no son correctos."
        }), 401

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run()