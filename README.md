# Integración con API de Khipu - Prueba Técnica

Este proyecto corresponde a la etapa técnica del proceso de selección para el cargo de **Customer Success en Khipu**.

---

## ✔ Objetivo

Simular una integración funcional con la API de pagos de Khipu utilizando llamadas HTTP mediante `receiver_id` y `secret`, en modo desarrollador, sin crear cobros manuales desde el portal.

---

## 🛠 Implementación

- Lenguaje: Python
- Plataforma usada: Replit
- Endpoint usado: `POST https://khipu.com/api/2.0/payments`
- Autenticación: HTTP Basic (con `receiver_id` y `secret`)
- Sin uso de portal para la creación de cobros

---

## 🔎 Pruebas realizadas

Se trabajó con **tres cuentas distintas**:

### 1. Cuenta personal (ID: 498308)
- Creada el mismo día de la prueba
- Modo desarrollador activado
- Contrato firmado
- Llave secreta generada
- **Resultado:** `403 – El mensaje no está firmado correctamente`

---

### 2. Cuenta de Moabi Store (ID: 480060)
- Cuenta más antigua, creada aproximadamente en agosto 2024
- También activada en modo desarrollador
- No se encuentra en producción ni ha sido usada comercialmente
- Solo utilizada para descartar que el error fuera por ser una cuenta recién creada
- **Resultado:** `403 – El mensaje no está firmado correctamente`

---

### 3. Cuenta de documentación pública (ID: 254187)
- Usada en ejemplos oficiales de Khipu
- También con `receiver_id` y `secret` conocidos
- **Resultado:** `403 – El mensaje no está firmado correctamente`

---

## 🧩 Conclusión

Ninguna de las cuentas utilizadas (ni nueva, ni antigua, ni pública) logró ejecutar una firma válida en el endpoint `/payments`.

> Este comportamiento indica que actualmente el entorno de pruebas de Khipu **no permite firmar pagos con HTTP Basic Auth usando secret**, incluso en cuentas activadas y verificadas. Es un detalle que debe ser activado manualmente por soporte o está restringido en el entorno DemoBank.

---

## ✅ Valor del ejercicio

- Se ejecutaron todas las configuraciones requeridas.
- Se aplicó correctamente la estructura de autenticación y firma.
- Se investigó documentación oficial y otros endpoints como `/banks`.
- Se abordó el error con persistencia y criterio técnico.

---

## 📁 Archivos

- `main.py`: código de integración real con llamada a API
- `README.md`: resumen y justificación del proceso

---

## 👤 Postulante

**Erick Daniel Guerra Montañez**  
Mayo 2025  
