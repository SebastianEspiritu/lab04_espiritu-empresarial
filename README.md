# Laboratorio 04: Relación de Modelos en Django

**Curso:** Desarrollo de Aplicaciones Empresariales  
**Estudiante:** Sebastián Espíritu  
**Repositorio:** https://github.com/SebastianEspiritu/lab04_espiritu-empresarial 
 
---

## Descripción del Proyecto

Este proyecto implementa un sistema de gestión bibliotecaria (`library`) desarrollado en **Django**, enfocado en la modelación y consulta de datos relacionales complejos mediante el ORM de Django. 

El objetivo principal es demostrar la integración y manipulación de las relaciones estándar entre entidades:
* **Uno a Uno (`OneToOneField`)**
* **Uno a Muchos (`ForeignKey`)**
* **Muchos a Muchos (`ManyToManyField`)** utilizando un **modelo intermedio personalizado (`through`)** para registrar metadatos adicionales en las transacciones relacionales.

---

## Esquema Relacional de Modelos

```text
+-------------------+       1:1        +-----------------------+
|   AuthorProfile   |<-----------------|        Author         |
+-------------------+                  +-----------------------+
| - id (PK)         |                  | - id (PK)             |
| - author_id (FK)  |                  | - name                |
| - biography       |                  | - email               |
| - website         |                  +-----------------------+
+-------------------+                              |
                                                   | 1:N
                                                   v
+-------------------+       M:N        +-----------------------+
|     Category      |<---------------->|         Book          |
+-------------------+                  +-----------------------+
| - id (PK)         |                  | - id (PK)             |
| - name            |                  | - title               |
+-------------------+                  | - summary             |
                                       | - author_id (FK)      |
                                       +-----------------------+
                                                   |
                                                   | 1:N
                                                   v
                                       +-----------------------+
                                       |      Publication      |
                                       +-----------------------+
                                       | - id (PK)             |
                                       | - book_id (FK)        |
                                       | - publisher_id (FK)   |
                                       | - publication_date    |
                                       | - edition             |
                                       +-----------------------+
                                                   ^
                                                   | N:1
                                       +-----------------------+
                                       |       Publisher       |
                                       +-----------------------+
                                       | - id (PK)             |
                                       | - name                |
                                       | - address             |
                                       +-----------------------+
```
## Entidades y Relaciones
* **Author & AuthorProfile (OneToOneField):**

Cada autor posee exactamente un perfil biográfico (biography, website).

* **Author & Book (ForeignKey):**

Relación 1:N donde un autor puede haber escrito múltiples libros.

* **Book & Category (ManyToManyField):**

Relación M:N donde un libro puede pertenecer a múltiples categorías literarias.

* **Book, Publisher & Publication (through='Publication'):**

Relación M:N implementada a través de un modelo asociativo (Publication) para guardar información del evento de publicación (publication_date, edition).

## Instalación y Configuración del Proyecto
Sigue estos pasos para clonar e iniciar el servidor localmente:

Clonar el repositorio:

Bash
git clone [https://github.com/SebastianEspiritu/lab04_espiritu-empresarial.git](https://github.com/SebastianEspiritu/lab04_espiritu-empresarial.git)
cd lab04_espiritu-empresarial
Crear y activar el entorno virtual:

```Bash
python -m venv venv
# En Windows:
venv\Scripts\activate
```
```Bash
pip install django
Ejecutar migraciones de base de datos:
```
```Bash
python manage.py makemigrations
python manage.py migrate
Crear superusuario (Administrador):
```
```Bash
python manage.py createsuperuser
Iniciar el servidor de desarrollo:
```
```Bash
python manage.py runserver
```

## Consultas Realizadas en Django Shell
Ejemplos de consultas mediante el ORM ejecutadas en python manage.py shell:
```Bash
Python
from library.models import Author, Book, Category, Publication, Publisher

# 1. Navegación directa e inversa
book = Book.objects.get(id=1)
print(f"Autor: {book.author.name}")

author = Author.objects.get(name="Gabriel García Márquez")
print(f"Libros escritos: {author.books.all()}")

# 2. Consulta filtrada de categorías cruzadas
magic_realism_books = Book.objects.filter(categories__name="Magical Realism")

# 3. Consulta del modelo intermedio Publication
publications = Publication.objects.filter(book=book)
for pub in publications:
    print(f"Editorial: {pub.publisher.name}, Fecha: {pub.publication_date}, Edición: {pub.edition
```

## Tecnologías Utilizadas
* Lenguaje: Python 3.x

* Framework: Django 5.x

* Base de Datos: SQLite3

* Control de Versiones: Git & GitHub

* IDE: Visual Studio Code
