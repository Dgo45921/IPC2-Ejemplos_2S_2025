# Comandos Básicos de Git

Git es un sistema de control de versiones distribuido que permite a los desarrolladores rastrear cambios en el código, colaborar con otros y mantener un historial de versiones. A continuación, se presentan algunos de los comandos básicos de Git con ejemplos para principiantes.

## Configuración Inicial
Antes de comenzar a usar Git, es importante configurarlo con tu nombre y correo electrónico:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@example.com"
```

## Crear un Repositorio
Para iniciar un nuevo repositorio en un directorio:

```bash
git init
```

Esto crea un repositorio vacío en el directorio actual.

## Clonar un Repositorio
Para clonar un repositorio existente desde un servidor remoto:

```bash
git clone <url-del-repositorio>
```

Ejemplo:

```bash
git clone https://github.com/usuario/repositorio.git
```

## Ver el Estado del Repositorio
Para ver los cambios realizados en el repositorio:

```bash
git status
```

## Añadir Cambios al Área de Staging
Para añadir archivos específicos al área de staging:

```bash
git add <archivo>
```

Para añadir todos los archivos modificados:

```bash
git add .
```

## Confirmar Cambios (Commit)
Para guardar los cambios en el historial del repositorio:

```bash
git commit -m "Mensaje del commit"
```

Ejemplo:

```bash
git commit -m "Añadí la funcionalidad X"
```

## Ver el Historial de Cambios
Para ver el historial de commits:

```bash
git log
```

Para un historial más compacto:

```bash
git log --oneline
```

## Crear y Cambiar de Rama
Para crear una nueva rama:

```bash
git branch <nombre-de-la-rama>
```

Para cambiar a una rama existente:

```bash
git checkout <nombre-de-la-rama>
```

O, para crear y cambiar a una nueva rama en un solo paso:

```bash
git checkout -b <nombre-de-la-rama>
```

## Fusionar Ramas (Merge)
Para fusionar una rama en la rama actual:

```bash
git merge <nombre-de-la-rama>
```

## Subir Cambios al Repositorio Remoto
Para subir los cambios confirmados al repositorio remoto:

```bash
git push origin <nombre-de-la-rama>
```

Ejemplo:

```bash
git push origin main
```

## Actualizar el Repositorio Local
Para obtener los últimos cambios del repositorio remoto:

```bash
git pull
```

## Deshacer Cambios
Para deshacer cambios en el área de staging:

```bash
git reset <archivo>
```

Para deshacer un commit (manteniendo los cambios en el área de trabajo):

```bash
git reset --soft HEAD~1
```

Para deshacer un commit y eliminar los cambios:

```bash
git reset --hard HEAD~1
```

## Eliminar Archivos
Para eliminar un archivo del repositorio y del sistema de archivos:

```bash
git rm <archivo>
```

Para eliminar un archivo solo del repositorio (manteniéndolo en el sistema de archivos):

```bash
git rm --cached <archivo>
```

## Ignorar Archivos
Para ignorar archivos específicos, crea un archivo `.gitignore` y añade los patrones de los archivos que deseas ignorar. Ejemplo de un `.gitignore`:

```
# Ignorar archivos temporales
*.log
*.tmp

# Ignorar directorios
/build/
/node_modules/
```

## Ver Cambios
Para ver los cambios realizados en los archivos:

```bash
git diff
```

Para ver los cambios entre commits:

```bash
git diff <commit1> <commit2>
```

## Etiquetas (Tags)
Para crear una etiqueta:

```bash
git tag -a <nombre-de-la-etiqueta> -m "Mensaje de la etiqueta"
```

Para listar todas las etiquetas:

```bash
git tag
```

## Ayuda
Para obtener ayuda sobre un comando específico:

```bash
git help <comando>
```

## Crear un Conflicto en Git
Para aprender a crear un conflicto en Git, consulta [este archivo](./crear_conflicto_git.md).

---
