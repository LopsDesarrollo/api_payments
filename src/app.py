from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from config import config
from waitress import serve

import datetime

app = Flask(__name__)

app.config['MYSQL_HOST']='127.0.0.1'
app.config['MYSQL_PORT']=3308
app.config['MYSQL_USER']='test'
app.config['MYSQL_PASSWORD']='t3st'
app.config['MYSQL_DB']='app_payments'

conexion = MySQL(app)

@app.route('/payments')
def list_payments():
  try:
    cursor = conexion.connection.cursor()
    sql = "SELECT id, folio, quantity, date_entry FROM payments ORDER BY id DESC"
    cursor.execute(sql)
    datos = cursor.fetchall()
    payments = []
    for fila in datos:
      pay = {'id': fila[0], 'folio': fila[1], 'quantity': fila[2], 'date_entry': fila[3]}
      payments.append(pay)
    return jsonify({'payments': payments, 'Mensaje': "Pagos Registrados"})
  except Exception as ex:
    print(ex)
    return jsonify({'mensaje': "Error"})
  
@app.route('/daypayments')
def day_payments():
  try:

    startDate=str(datetime.date.today())
    cursor = conexion.connection.cursor()
    sql = "SELECT SUM(quantity) FROM payments WHERE date_entry BETWEEN '"+startDate+" 00:00:00' AND NOW();"
    cursor.execute(sql)
    datos = cursor.fetchall()
    for fila in datos:
      pay=fila[0]

    if pay is None:
      return jsonify({'daypayments': 0})
    else:
      return jsonify({'daypayments': pay})
  except Exception as ex:
    print(ex)
    return jsonify({'mensaje': "Error"})
  
@app.route('/payments', methods=['POST'])
def add_pay():
  try:
    folio = generateFolio()
    if folio != None:
      cursor = conexion.connection.cursor()
      sql = "SELECT id, folio, quantity, date_entry FROM payments WHERE folio = '{0}'".format(folio)
      cursor.execute(sql)
      datos = cursor.fetchone()

      if datos == None:      
        sql = """INSERT INTO payments ( folio, quantity) 
                        VALUES ('{0}', '{1}')""".format(folio, request.json['quantity'])
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'folio': folio,'Mensaje': "Pago Registrado"})
      else:
        return jsonify({'mensaje': "Error: Folio ya fue registrado"})
    else:
      return jsonify({'mensaje': "Error: No se logro generar el Folio"})
  except Exception as ex:
    return jsonify({'mensaje': "Error"})

def pagina_no_encontrada(error):
  return "<h1> La pagina que intentas buscar no existe....</h1>", 404

def generateFolio():
  cursor = conexion.connection.cursor()
  sql = "SELECT id, folio, quantity, date_entry FROM payments ORDER BY id DESC"
  cursor.execute(sql)
  datos = cursor.fetchone()

  if datos == None:
    return 1
  else:
    previousFolio = int(datos[1]);
    return previousFolio + 1  


mode = "dev"

if __name__ == '__main__':
  #app.config.from_object(config['development'])
  app.register_error_handler(404, pagina_no_encontrada)

  if mode == "dev":
    app.run()
  else:
    serve(app, host='0.0.0.0' ,port=5000,threads=1)
