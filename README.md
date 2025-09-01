Nombres del Grupo
Estudiante 1: Yury Andrea Dorado Lucas
Estudiante 1: Cristian David Rodriguez ruiz 
Estudiante 1: Jonathan David Lancheros Bello

Proceso de trabajo
Cada miembro del grupo se encargó de implementar una de las operaciones con lenguajes y sus respectivos ejercicios:
Estudiante 1: Unión de lenguajes
Estudiante 2: Intersección de lenguajes
Estudiante 3: Concatenación de lenguajes

Comandos Git utilizados
Creación del repositorio:

1.Creación del repositorio:
git init
git remote add origin [URL_DEL_REPOSITORIO]

2.Creación de ramas para cada estudiante:
git checkout -b rama-estudiante1
git checkout -b rama-estudiante2  
git checkout -b rama-estudiante3

3.Flujo de trabajo para cada estudiante:
git checkout rama-estudianteX
# Realizar cambios en el código
git add .
git commit -m "Descripción de los cambios realizados"
git push origin rama-estudianteX

4.Proceso de fusión mediante Pull Requests:
-Cada estudiante creó un Pull Request desde su rama hacia main
-Los otros miembros revisaron el código y aprobaron los cambios
-Se fusionaron los Pull Requests después de la revisión

Resumen del proceso de Pull Request
-Estudiante 1 creó PR desde rama-estudiante1 a main
-Estudiante 2 y 3 revisaron el código, hicieron comentarios y aprobaron
-Se fusionó el PR después de incorporar las sugerencias
-Se repitió el proceso para los otros estudiantes

Estructura del Proyecto
lenguajes.py
Archivo principal que contiene:

°Definición de los lenguajes base L1, L2, L3, L4, L5
°Funciones para operaciones con lenguajes:
-union_lenguajes(L, M): Calcula la unión de dos lenguajes
-interseccion_lenguajes(L, M): Calcula la intersección de dos lenguajes
-concatenacion_lenguajes(L, M): Calcula la concatenación de dos lenguajes
-pertenece(palabra, lenguaje): Verifica si una palabra pertenece a un lenguaje
°Funciones con los ejercicios resueltos:
-ejercicios_union(): 10 ejercicios de unión de lenguajes
-ejercicios_interseccion(): 10 ejercicios de intersección de lenguajes
-ejercicios_concatenacion(): 10 ejercicios de concatenación de lenguaje

Clonar el repositorio:
git clone [URL_DEL_REPOSITORIO]
cd [NOMBRE_DEL_REPOSITORIO]

Ejecutar el script principal:
python lenguajes.py