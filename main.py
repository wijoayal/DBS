import os
import functions
import mysql.connector

mydb = functions.connect()

def menu():
	
	os.system('cls')
	print ("Selecciona una opción")
	print ("\t1 - Op. Cliente")
	print ("\t2 - Op. Trabajador")
	print ("\t3 - Op. Trabajo")
	print ("\t4 - Op. Promociones")
	print ("\t5 - Otras Consultas")
	print ("\t6 - Salir")
 
def menuc():

	print ("Selecciona una opción")
	print ("\t1 - Añadir cliente")
	print ("\t2 - Consultar clientes")
	print ("\t3 - Editar cliente")
	print ("\t4 - Eliminar cliente")
	print ("\t5 - Salir")

def menut():
	
	print ("Selecciona una opción")
	print ("\t1 - Añadir trabajador")
	print ("\t2 - Consultar trabajadores")
	print ("\t3 - Editar trabajador")
	print ("\t4 - Eliminar trabajador")
	print ("\t5 - Salir")

def menutr():

	print ("Selecciona una opción")
	print ("\t1 - Añadir trabajo")
	print ("\t2 - Consultar trabajos")
	print ("\t3 - Editar trabajos")
	print ("\t4 - Eliminar trabajos")
	print ("\t5 - Salir")

def menup():

	print ("Selecciona una opción")
	print ("\t1 - Añadir promocion")
	print ("\t2 - Consultar promociones")
	print ("\t3 - Editar promocion")
	print ("\t4 - Eliminar promocion")
	print ("\t5 - Salir")

def menuoc():

	print ("Selecciona una opción")
	print ("\t1 - Consulta de trabajos por nombre de trabajador")
	print ("\t2 - Consulta total de pagos realizado a trabajador")
	print ("\t3 - Consulta de clientes frecuentes")
	print ("\t4 - Consulta de nombres de cliente por numero de cedula")
	print ("\t5 - Consulta de pagos de cada cliente por monto")
	print ("\t6 - Salir")


while True:
	# Mostramos el menu
	menu()

	# solicituamos una opción al usuario
	opcionMenu = input("Ingrese  una opcion >> ")
 
	if opcionMenu=="1": #menu cliente
		print ("")
		menuc()
		opcionMenuc = input("Ingrese una opcion >> ")
		if opcionMenuc=="1":
			print ("")
			functions.add_cliente(mydb)
		elif opcionMenuc=="2":
			print ("")
			functions.show_cliente(mydb)
		elif opcionMenuc=="3":
			print ("")
			functions.edit_cliente(mydb)
		elif opcionMenuc=="4":
			print ("")
			functions.del_cliente(mydb)
		elif opcionMenuc=="5":
			break
		else:
			print ("")
			input("No ha pulsado ninguna opción correcta.  .")
	elif opcionMenu=="2": #menu trabajador
		print ("")
		menut()
		opcionMenut = input("Ingrese una opcion >> ")
		if opcionMenut=="1":
			print ("")
			functions.add_trabajador(mydb)
		elif opcionMenut=="2":
			print ("")
			functions.show_trabajador(mydb)
		elif opcionMenut=="3":
			print ("")
			functions.edit_trabajador(mydb)
		elif opcionMenut=="4":
			print ("")
			functions.del_trabajador(mydb)
		elif opcionMenut=="5":
			break
		else:
			print ("")
			input("No ha pulsado ninguna opción correcta.  .")
	elif opcionMenu=="3": #menu trabajo
		print ("")
		menutr()
		opcionMenutr = input("Ingrese una opcion >> ")
		if opcionMenutr=="1":
			print ("")
			functions.add_trabajo(mydb)
		elif opcionMenutr=="2":
			print ("")
			functions.show_trabajo(mydb)
		elif opcionMenutr=="3":
			print ("")
			functions.edit_trabajo(mydb)
		elif opcionMenutr=="4":
			print ("")
			functions.del_trabajo(mydb)
		elif opcionMenutr=="5":
			break
		else:
			print ("")
			input("No ha pulsado ninguna opción correcta.  .")
	elif opcionMenu=="4": #menu promociones
		print ("")
		menup()
		opcionMenup = input("Ingrese una opcion >> ")
		if opcionMenup=="1":
			print ("")
			functions.add_promocion(mydb)
		elif opcionMenup=="2":
			print ("")
			functions.show_descuento(mydb)
		elif opcionMenup=="3":
			print ("")
			functions.edit_descuento(mydb)
		elif opcionMenup=="4":
			print ("")
			functions.del_descuento(mydb)
		elif opcionMenup=="5":
			break
		else:
			print ("")
			input("No ha pulsado ninguna opción correcta.  .")
	elif opcionMenu=="5": #menu otras consultas
		print ("")
		menuoc()
		opcionMenuoc = input("Ingrese una opcion >> ")
		if opcionMenuoc=="1":
			print ("")
			functions.query_trabajosNombreTrabajador(mydb)
		elif opcionMenuoc=="2":
			print ("")
			functions.query_totalPagosTrabajador(mydb)
		elif opcionMenuoc=="3":
			print ("")
			functions.query_clientesFrecuentes(mydb)
		elif opcionMenuoc=="4":
			print ("")
			functions.query_nombreClienteCedula(mydb)
		elif opcionMenuoc=="5":
			print("")
			functions.query_pagosClienteMontoMinimo(mydb)
		elif opcionMenuoc == "6":
			break
		else:
			print ("")
			input("No ha pulsado ninguna opción correcta.  .")
	elif opcionMenu=="6": #salir del menu
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...")