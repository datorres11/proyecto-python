from flask import Flask, render_template,request
import psycopg2

app=Flask(__name__)

PSQL_HOST="localhost"
PSQL_PORT="5432"
PSQL_USER="postgres"
PSQL_PASS="root"
PSQL_DB="tocogu"

connection_address= """
host=%s port=%s user=%s password=%s dbname=%s
""" % (PSQL_HOST,PSQL_PORT,PSQL_USER,PSQL_PASS,PSQL_DB)
connection=psycopg2.connect(connection_address)


@app.route("/")

def loguin():
    return render_template("login.html")

@app.route("/recuperar_contraseña")

def recuperarContraseña():
    return render_template("forgot-password.html")

@app.route("/pantalla_principal")

def pantallaPrincipal():
    return render_template("index.html")
    
@app.route("/registrar")

def registrar():
    return render_template("register.html")

@app.route('/regresar_al_login',methods = ['POST'])

def regresarAlLogin():
    #usuarioData=usuario.Usuarios(1,,,)
    cursor=connection.cursor()
    uQuery="Insert into usuarios(contrasena, ideusuario, nombre, rol, email)"
    uQuery=uQuery+" Values(%s,%s,%s,%s,%s)"
    try:
        cursor.execute(uQuery,(request.form['password'],2,request.form['firstName']+' '+request.form['lastName'],1,request.form['email']))
        connection.commit()
    except psycopg2.DataError as error:
        print("Error al insertar un usuario: "+str(error),'alert-warning')
    return render_template("login.html")

if __name__ == "__main__":
    #conect=conexion.Conexion()
    #conexion.connect
    #app.run()
    app.run(debug=True)