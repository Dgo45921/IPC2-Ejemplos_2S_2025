# Cómo sucede un conflicto en Git

Un conflicto en Git ocurre cuando dos ramas tienen cambios en las mismas líneas de un archivo y Git no puede determinar automáticamente cuál de los cambios debe mantenerse. A continuación, se detallan los pasos para crear un conflicto de manera intencional:

## Pasos para Crear un Conflicto

1. **Clonar el Repositorio**
   
   Se debe tener un repositorio clonado localmente. Si no se tiene, clonarlo con el siguiente comando:

   ```bash
   git clone <url-del-repositorio>
   ```

2. **Crear y Cambiar a una Nueva Rama**
   
   Crea una nueva rama y úsala:

   ```bash
   git checkout -b rama-conflicto
   ```

3. **Modificar un Archivo en la Nueva Rama**
   
   Abrir un archivo existente y realizar cambios en él. Por ejemplo, edita un archivo llamado `archivo.txt` y añade la siguiente línea:

   ```
   Cambio en la rama-conflicto
   ```

   Guardar los cambios y realiza un commit:

   ```bash
   git add .
   git commit -m "Cambio en rama-conflicto"
   ```

4. **Cambiar a la Rama Principal (master)**
   
   Cambiamos de vuelta a la rama principal:

   ```bash
   git checkout master
   ```

5. **Modificar el Mismo Archivo en la Rama Principal**
   
   Realizar un cambio diferente en el mismo archivo `archivo.txt`. Por ejemplo, agregando la siguiente línea:

   ```
   Cambio en la rama principal
   ```

   Guarda los cambios y realiza un commit:

   ```bash
   git add archivo.txt
   git commit -m "Cambio en rama principal"
   ```

6. **Fusionar las Ramas**
   
   Intenta fusionar la rama `rama-conflicto` en la rama principal:

   ```bash
   git merge rama-conflicto
   ```

   Git detectará un conflicto y mostrará un mensaje indicando que hay conflictos que deben resolverse.

## Resolver el Conflicto

1. Al ver un archivo con conflicto. El editor de código nos permitirá ver

   ```
   <<<<<<< HEAD
   Cambio en la rama principal
   =======
   Cambio en la rama-conflicto
   >>>>>>> rama-conflicto
   ```

2. Editar el archivo para resolver el conflicto. Por ejemplo, se pueden combinar los cambios o elegir uno de ellos:

   ```
   Cambio en la rama principal
   Cambio en la rama-conflicto
   ```

3. Una vez resuelto, agreganis el archivo al área de staging:

   ```bash
   git add .
   ```

4. Completa la fusión(merge):

   ```bash
   git commit -m "Resuelto conflicto entre main y rama-conflicto"
   ```

¡Listo! Se ha creado y resuelto un conflicto en Git.
