# DAVS Mis Colores 🎨

Aplicación web Full-Stack desarrollada enteramente en **Python** utilizando el framework **Reflex**. Este proyecto funciona como un generador y gestor de paletas de colores profesional, diseñado con una interfaz moderna en "Modo Oscuro" y una experiencia de usuario altamente interactiva.

## 🚀 Características Principales

* **Generación Dinámica:** Creación de paletas de colores aleatorias en formato hexadecimal.
* **Gestión de Estado Compleja:** Uso de estados heredados en Reflex para separar la lógica de UI de la lógica de persistencia de datos.
* **Persistencia de Datos:** Sistema de guardado, edición y eliminación (CRUD) de paletas favoritas, utilizando **SQLModel** y **SQLite**.
* **Interacciones al Portapapeles:** Copia rápida de colores individuales o de la paleta completa con notificaciones visuales (Toasts) integradas.
* **Diseño UI/UX Personalizado:** Interfaz responsiva con componentes estilizados dinámicamente mediante variables (Tailwind CSS subyacente), adoptando un esquema *Dark Mode* con acentos rojizos y tarjetas circulares.

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.14
* **Framework Web:** Reflex 0.9.x
* **Base de Datos:** SQLite gestionado a través de SQLModel y Alembic (Migraciones).

## ⚙️ Instalación y Despliegue Local

Sigue estos pasos para probar el proyecto en tu entorno de desarrollo:

### 1. Clonar el repositorio
\`\`\`bash
git clone https://github.com/davsdevelop/DAVS_mis_colores.git
cd DAVS_mis_colores
\`\`\`

### 2. Configurar el Entorno Virtual
\`\`\`bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
\`\`\`

### 3. Configurar Base de Datos e Inicializar Frontend
\`\`\`bash
# Inicializa el directorio web de Reflex
reflex init

# Aplica las migraciones para crear colors.db
reflex db migrate
\`\`\`

### 4. Iniciar el Servidor de Desarrollo
\`\`\`bash
reflex run
\`\`\`
La aplicación estará disponible de forma local en \`http://localhost:3000/\`.

---
*Desarrollado por **Diego Videla Silva***