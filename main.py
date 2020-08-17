import os
import functions
import mysql.connector

mydb = functions.connect()

def menu():
	
	os.system('cls')
	print ("Selecciona una opción")
	print ("\t1 - Cliente")
	print ("\t2 - Trabajador")
	print ("\t3 - Trabajo")
	print ("\t4 - Consultas")
	print ("\t5 - Salir")
 
def menuc():

	print ("Selecciona una opción")
	print ("\t1 - Añadir informacion del cliente")
	print ("\t2 - Añadir de Promoción")
	print ("\t3 - Modificar informacion del cliente")
	print ("\t4 - Mostrar informacion de los cliente")
	print ("\t5 - salir")

def menut():
	
	print ("Selecciona una opción")
	print ("\t1 - Añadir informacion del trabajador")
	print ("\t2 - Modificar informacion del trabajador")
	print ("\t3 - Mostrar informacion de los trabajadores")
	print ("\t4 - Mostrar informacion de los descuentos")
	print ("\t5 - salir")

def menutra():

	print ("Selecciona una opción")
	print ("\t1 - Añadir informacion del trabajo")
	print ("\t2 - Mostrar informacion del trabajo")
	print ("\t3 - salir")

def menucon():

	print ("Selecciona consulta a realizar")
	print ("\t1 - Trabajos por nombre de trabajador")
	print ("\t2 - Total de pagos realizados a trabajador")
	print ("\t3 - Clientes frecuentes")
	print ("\t4 - Conocer clientes por numero de cedula")
	print ("\t5 - pagos de cada cliente")
	print ("\t6 - salir")


while True:
	# Mostramos el menu
	menu()

	# solicituamos una opción al usuario
	opcionMenu = input("inserta una opcion >> ")
 
	if opcionMenu=="1": #menu cliente
		print ("")
		menuc()
		if opcionMenu=="1":
			print ("")
			functions.add_cliente(mydb)
		elif opcionMenu=="2":
			print ("")
			functions.add_promocion(mydb)
		elif opcionMenu=="3":
			print ("")
			#modificar
		elif opcionMenu=="4":
			print ("")
			functions.show_cliente(mydb)
		elif opcionMenu=="5":
			break
		else:
			print ("")
			input("No has pulsado ninguna opción correcta...")
	elif opcionMenu=="2": #menu trabajador
		print ("")
		menut()
		if opcionMenu=="1":
			print ("")
			functions.add_trabajador(mydb)
		elif opcionMenu=="2":
			print ("")
			#modificar
		elif opcionMenu=="3":
			print ("")
			functions.show_trabajador(mydb)
		elif opcionMenu=="4":
			print ("")
			functions.show_descuento(mydb)
		elif opcionMenu=="5":
			break
		else:
			print ("")
			input("No has pulsado ninguna opción correcta...")
	elif opcionMenu=="3": #menu trabajo
		print ("")
		menutra()
		if opcionMenu=="1":
			print ("")
			functions.add_trabajo(mydb)
		elif opcionMenu=="2":
			print ("")
			functions.show_trabajo(mydb)
		elif opcionMenu=="3":
			break
		else:
			print ("")
			input("No has pulsado ninguna opción correcta...")
	elif opcionMenu=="4": #menu consultas
		print ("")
		menucon()
		if opcionMenu=="1":
			print ("")
			functions.query_trabajosNombreTrabajador(mydb)
		elif opcionMenu=="2":
			print ("")
			functions.query_totalPagosTrabajador(mydb)
		elif opcionMenu=="3":
			print ("")
			functions.query_clientesFrecuentes(mydb)
		elif opcionMenu=="4":
			print ("")
			functions.query_nombreClienteCedula(mydb)
		elif opcionMenu=="5":
			print ("")
			functions.query_pagosClienteMontoMinimo(mydb)
		elif opcionMenu=="6":
			break
		else:
			print ("")
			input("No has pulsado ninguna opción correcta...")
	elif opcionMenu=="5": #salir del menu
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...")