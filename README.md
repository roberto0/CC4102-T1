# CC4102-T1
Tarea 1 de Diseño y Análisis de Algoritmos CC4102-1 Primavera 2020

Para correr la prueba unitaria de cada algorimo debe utilizar:

sh run_one.sh R K BINARY OUTPATH
  - R: Cantidad de porciones
  - K: Valor de k, corresponde a la cantidad de itreciones en promedio
  - BINARY: Nombre del binario .py
  - OUTPATH: Dirección del archivo de salida

Para obtener el caso promedio:

sh benchmark STARTN ENDN DN BINARY OUTPATH
  - SRTARTN: Debe ser 1
  - ENDN: Cantidad itreaciones totales
  - DN: Salto entre itreaciones
  - BINARY: Nombre del binario
  - OUTPATH: Dirección del archivo de salida
  
  Para correr todo los binarios:
  
  sh run_all.sh
  
  by Roberto Carrasco
  from Valdivia, Chile
