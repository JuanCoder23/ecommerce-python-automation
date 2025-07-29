# 🛒 E-commerce UI Test Automation with Python & Selenium

Este proyecto demuestra la automatización de pruebas funcionales para una aplicación e-commerce usando **Python**, **Selenium WebDriver** y **PyTest**, aplicando el patrón de diseño **Page Object Model (POM)**.

Diseñado como portafolio profesional para mostrar habilidades de **QA Automation** y buenas prácticas.

---

## 🚀 Tecnologías utilizadas

- 🐍 Python 3.10+
- 🧪 PyTest
- 🌐 Selenium WebDriver
- 🧰 WebDriver Manager
- 📄 Page Object Model (POM)
- 🧪 pytest.ini
- 💻 Visual Studio Code

---

## 📁 Estructura del proyecto

Ecommerce - Python/
│
├── pages/                     # Clases de páginas (Page Object Model)
│   ├── base_pages.py
│   ├── login_pages.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── test/                      # Casos de prueba automatizados
│   ├── test_login.py
│   ├── test_invalid_login.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── utils/                     # Utilidades (driver y configuración)
│   ├── config.py
│   └── driver_factory.py
│
├── venv/                      # Entorno virtual (no subir al repo)
├── pytest.ini                 # Configuración de PyTest
├── requirements.txt           # Lista de dependencias
└── README.md                  # Documentación del proyecto

## ✅ Casos de prueba automatizados

| Test ID | Descripción                                  | Estado |
|--------:|----------------------------------------------|--------|
| 01      | Login exitoso con usuario válido             | ✅     |
| 02      | Login con credenciales inválidas             | ✅     |
| 03      | Agregar producto al carrito                  | ✅     |
| 04      | Eliminar producto del carrito                | ✅     |
| 05      | Flujo completo de checkout (compra)          | ✅     |

---

## ⚙️ Cómo ejecutar los tests

1. 🔁 Clona este repositorio:

```bash
git clone https://github.com/JuanCoder23/ecommerce-python-automation
cd ecommerce-python-automation
```
---

## 📎 Repositorio

🔗 [https://github.com/JuanCoder23/ecommerce-python-automation](https://github.com/JuanCoder23/ecommerce-python-automation)

---

## 👨‍💻 Autor

**Juan Pablo Sandoval**  
QA Engineer | Test Automation  
🔗 [LinkedIn](https://www.linkedin.com/in/juan-pablo-sandoval-gutierrez-7533451b1)  
🐙 [GitHub](https://github.com/JuanCoder23)