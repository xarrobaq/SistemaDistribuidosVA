# SistemaDistribuidosVA
Sistema Distribuidos Vicente Arroba

Este proyecto tiene como objetivo diseñar y construir una plataforma tecnológica para
la transmisión, almacenamiento y verificación de datos de un censo poblacional.

base_datos.xlsx .- Archivo con 1000 registros de formularios de usuarios

file.json .- Archivo con formato Json generado de archivo de Excel

CapturaDatos.py
- Simulador de Módulo de Captura de Datos.- En esta etapa se ha utilizado como insumo un archivo de excel con los
  registros de formularios ingresados por los usuarios.
  
EnviarFormulario.py
- Cola de Mensajes de entrada.-  En esta etapa se seleccionan la cantidad de formularios que se desean transmitir en la cola de mensajes
  en formato Json
  
RecibeFormulario.py
- Módulo de validación y deduplicación de formularios.- En esta etapa se recibe la cola de mensaje en formato Json, se realiza la validación y deduplicación de formularios luego de la consulta al repositorio por medio de la API REST.

App.py
- API REST se la realiza por medio de Flask 
  
- Módulo de Almacenamiento Distribuido de Datos de Alta Disponibilidad.
- Módulo de Reportes / Analítica
