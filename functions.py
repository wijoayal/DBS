import mysql.connector

def connect():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="project"
  )

def add_cliente():
  mycursor = mydb.cursor()
  print("***Agregando cliente***")
  cedula = input("Ingrese el numero de cedula:  ")
  nombre = input("Ingrese el nombre:  ")
  telefono = input("Ingrese el numero de telefono:  ")
  direccion = input("Ingrese la direccion:  ")
  val = "INSERT INTO `project`.`cliente` (`num_cedula`, `nombre`, `telefono`, `direccion_cliente`) VALUES ('"+ cedula+"', '"+nombre+"', '"+telefono+"', '"+direccion+"')"
  mycursor.execute(val)
  print('Cliente agregado exitosamente')

def add_promocion():
  mycursor = mydb.cursor()
  print("***Agregando promocion***")
  cod_promocion= input("Ingrese el codigo de la promocion:  ")
  nombre = input("Ingrese el nombre:  ")
  valor = input("Ingrese el valor del porcentaje del descuento:  ")
  val = "INSERT INTO `project`.`descuento` (`cod_promocion`, `nombre`, `valor`) VALUES ('"+cod_promocion+"', '"+nombre+"', '"+valor+"');"
  mycursor.execute(val)
  print('Promocion agregada exitosamente')

def add_trabajador():
  mycursor = mydb.cursor()
  print("***Agregando trabajador***")
  cedula = input("Ingrese el numero de cedula:  ")
  nombre = input("Ingrese el nombre:  ")
  profesion = input("Ingrese la profesion del trabajador")
  telefono = input("Ingrese el numero de telefono:  ")
  direccion = input("Ingrese la direccion:  ")
  about_me = input("Ingrese una breve resena sobre el trabajador")
  val = "INSERT INTO `project`.`trabajador` (`num_cedula`, `nombre`, `profesion`, `telefono`, `direccion_trabajador`, `about_me`) VALUES ('"+cedula+"', '"+nombre+"', '"+profesion+"', '"+telefono+"', '"+direccion+"', '"+about_me+"')"
  mycursor.execute(val)
  print('Cliente agregado exitosamente')

def add_trabajo():
  mycursor = mydb.cursor()
  print("***Agregando trabajo***")
  factura = input("Ingrese el numero de factura:  ")
  costo = input("Ingrese el costo en dolares:  ")
  direccion = input("Ingrese la direccion del trabajo:  ")
  mensaje = input("Ingrese retroalimentacion del cliente:  ")
  pago = input("Ingrese el numero de telefono:  ")
  cedulatr= input("Ingrese el numero de cedula del trabajador:  ")
  cedulacl = input("Ingrese el numero de cedula del cliente:  ")
  calificacion = input("Ingrese la calificacion del trabajo (1-5):  ")
  val = "INSERT INTO `project`.`trabajo` (`num_factura`, `costo`, `direccion_trabajo`, `mensajes`, `pago`, `trabajador_num_cedula`, `cliente_num_cedula`, `calificacion`) VALUES ('"+factura+"', '"+costo+"', '"+direccion+"', '"+mensaje+"', '"+pago+"', '"+cedulatr+"', '"+cedulacl+"', '"+calificacion+"')"
  mycursor.execute(val)
  print('Cliente agregado exitosamente')

def show_trabajador():  
  mycursor = mydb.cursor()
  print("Mostrando datos de trabajadores:\n")
  mycursor.execute("SELECT * FROM trabajador")
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)
  print()

def show_trabajo():  
  mycursor = mydb.cursor()
  print("Mostrando datos de trabajo:\n")
  mycursor.execute("SELECT * FROM trabajo")
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)
  print()

def show_descuento():  
  mycursor = mydb.cursor()
  print("Mostrando datos de promociones:\n")
  mycursor.execute("SELECT * FROM descuento")
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)
  print()

def show_cliente():  
  mycursor = mydb.cursor()
  print("Mostrando datos de cliente:\n")
  mycursor.execute("SELECT * FROM cliente")
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)
  print()
  
def query_trabajosNombreTrabajador():
  print("Consulta de trabajos por nombre de trabajador: ")
  nombre = input("Escriba el nombre del trabajador: ")
  val = "SELECT * FROM trabajo tr JOIN trabajador t ON t.num_cedula = tr.trabajador_num_cedula WHERE nombre = '" + nombre + "'"
  print("MOSTRANDO LOS TRABAJOS DE "+nombre)
  mycursor.execute(val)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

def query_totalPagosTrabajador():
  print("Consulta total de pagos realizado a trabajador: ")
  data = input("Escriba el nombre del trabajador: ")
  val = "SELECT nombre, SUM(pago) AS total FROM trabajo tr JOIN trabajador t ON t.num_cedula = tr.trabajador_num_cedula WHERE nombre = '"+ data + "'"
  print("MOSTRANDO LOS PAGOS REALIZADOS A "+data)
  mycursor.execute(val)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

def query_clientesFrecuentes():
  print("Consulta de clientes frecuentes (Muestra en orden descendente la cantidad de trabajos que han contratado los clientes ")
  val = "SELECT nombre, num_cedula, COUNT(*) AS total FROM trabajo tr JOIN cliente c ON c.num_cedula = tr.cliente_num_cedula GROUP BY c.num_cedula ORDER BY COUNT(*) DESC"
  mycursor.execute(val)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

def query_nombreClienteCedula():
  print("Consulta de nombres de cliente por numero de cedula: ")
  data = input("Escriba el numero de cedula del cliente: ")
  val = "SELECT nombre, num_cedula FROM trabajo tr JOIN cliente c ON c.num_cedula = tr.cliente_num_cedula WHERE num_cedula = '"+ data + "'"
  print("MOSTRANDO NOMBRE DE CLIENTE CON NUMERO DE CEDULA "+data)
  mycursor.execute(val)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

def query_pagosClienteMontoMinimo():
  print("Consulta de pagos de cada cliente por monto: ")
  data = input("Escriba el monto minimo: $ ")
  val = "SELECT num_factura, nombre, SUM(pago) FROM trabajo tr JOIN cliente c ON c.num_cedula = tr.cliente_num_cedula GROUP BY nombre HAVING SUM(pago)> "+ data
  print("MOSTRANDO LOS PAGOS REALIZADOS DE MAS DE "+data+ "DOLARES")
  mycursor.execute(val)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)