from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
# Configuro los paráemtros de mi db
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'sistema2122'
mysql.init_app(app)

@app.route('/')
def index():
    # vamos a hacer que inserte un registro
    sql = "INSERT INTO `empleados` (`id`, `nombre`, `mail`, `foto`) VALUES (NULL, 'nachols', 'correo_electronico@gmail.com', 'foto.jpg');"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    return render_template('empleados/index.html')

if __name__ == '__main__':
    app.run(debug = True)

# comando insert
# INSERT INTO `empleados` (`id`, `nombre`, `mail`, `foto`) VALUES (NULL, 'nombre_prueba', 'correo_electronico@gmail.com', 'foto.jpg');