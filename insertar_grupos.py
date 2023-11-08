from config import db  # Reemplaza "tu_aplicacion" con el nombre real de tu aplicGrupoación
from modelos import Grupos  # Reemplaza "tu_modelo" con el nombre real de tu modelo de Grupo

# Define los grupos para Docentes y Directivos
todos = Grupos(grupo='Todos')
grupo_docentes = Grupos(grupo="Docentes")
grupo_directivos = Grupos(grupo="Directivos")

# Agrega los grupos a la base de datos
db.session.add(todos)
db.session.add(grupo_docentes)
db.session.add(grupo_directivos)

# Define los grupos para Preescolar y los grados de 1ro a 11vo
grupos_preescolar = [Grupos(grupo=f"Preescolar-{i}") for i in range(1, 7)]
grupos_grados = [Grupos(grupo=f"{i}-{j}") for i in range(1, 12) for j in range(1, 11)]

# Agrega los grupos de Preescolar y grados a la base de datos
db.session.add_all(grupos_preescolar)
db.session.add_all(grupos_grados)

# Guarda los cambios en la base de datos
db.session.commit()
