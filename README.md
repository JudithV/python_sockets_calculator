# Calculadora cliente/servidor con Python

Este trabajo consiste en una calculadora, pensada de modo que el cliente introduzca los parámetros de la Ip del servidor y del puerto para conectarse y, una vez dentro del programa, indicará si quiere realizar una operación, y a continuación el operador y los dos operandos. El servidor calculará el resultado o enviará un mensaje de error al cliente (en caso de que no haya introducido un operador válido o que pretenda dividir entre 0). Por defecto el servidor solo admite dos conexiones y se utiliza el puerto 5050, pero es fácilmente modificable desde el código del servidor.

# Client/server calculator in Python

This work consists of a calculator, made so the client enters as a program parameter the IP of the server and the port to establish the connection. Once inside the program, the client will indicate if he wants to perform an operation (if they don't then they have to type 'salir' (exit)) and then enter the operator and the two operands. The server will perform the calculations and will send the result to the client or an error message (if the client enters an invalid operator or tries to divide a number by zero). The server uses the port 5050 and only admits two connections simultaneously as default, but it is easy to modify in the server code.
