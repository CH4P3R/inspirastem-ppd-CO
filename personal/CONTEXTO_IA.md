# 🤖 GUÍA Y CONTEXTO MAESTRO PARA EL AGENTE DE IA (INSPIRASTEM 2026)

> ⚠️ **INSTRUCCIÓN OBLIGATORIA INICIAL PARA CUALQUIER AGENTE DE IA:**  
> Al leer este archivo al inicio de una nueva conversación o sesión, **LO PRIMERO QUE DEBES HACER ANTES DE RESPONDER O EJECUTAR CUALQUIER ACCIÓN** es saludar al usuario y realizar la siguiente pregunta interactiva de selección:  
>  
> ---  
> *"¡Hola! He leído tu archivo de contexto maestro de InspiraSTEM 2026. Para brindarte la mejor asistencia posible, por favor indícame en cuál de las 3 fases nos encontramos hoy:"*  
>  
> 1. **Fase 1: Preparación y Estudio Intensivo PRE-Curso**  
>    *(Estamos estudiando a fondo desde cero, analizando la física, matemáticas y código a nivel NASA / Silicon Valley en la carpeta `personal/`).*  
>  
> 2. **Fase 2: EN EL CURSO (Taller Activo)**  
>    *(Estamos participando activamente en las sesiones del taller. Sé que ya estudiaste las bases, pero entiendo que puedes necesitar repasar conceptos olvidados o ayuda con los notebooks grupales).*  
>  
> 3. **Fase 3: Entorno Diferente / Proyecto Externo / Post-Curso**  
>    *(Estás trabajando en otro repositorio, computadora o programa, y necesitas conectar o adaptar el conocimiento y archivos que construimos en este proyecto original).*  
> ---  
>  
> **ESPERA A QUE EL USUARIO INDIQUE EL NÚMERO (1, 2 O 3) ANTES DE CONTINUAR CON CUALQUIER OTRA TAREA.**

---

## 🎯 PERFIL DEL USUARIO Y FILOSOFÍA DE TRABAJO

- **Usuario:** Apasionado, altamente motivado, con mentalidad de superación y búsqueda de excelencia académica sin conformismos.
- **Meta:** Dominar la astrofísica de discos protoplanetarios, el procesamiento de datos astronómicos y la espectroscopía molecular a nivel de investigación de vanguardia (estándar NASA, Caltech, ESO, Silicon Valley).
- **Enfoque Pedagógico Requerido:** **Primeros Principios (*First Principles*)**. No le des código o fórmulas como "cajas negras". Explica el *por qué* físico, la matemática subyacente y la estructura informática de bajo nivel.

---

## 📚 CONTEXTO 1: FASE PRE-CURSO (Estudio Intensivo y Fundamentos Profundos)

### 1.1 Objetivo de esta Fase
Preparar al usuario antes del taller para que domine el 100% de los temas teóricos, numéricos e informáticos. Debe ir **mucho más allá** del nivel introductorio del taller.

### 1.2 Módulos de Conocimiento a Desarrollar en `personal/`
1. **Especificación FITS (IAU Standard):**
   - Bloques de 2880 bytes, `PrimaryHDU`, `ImageHDU`, `BinTableHDU`.
   - Encabezados WCS: `BITPIX`, `NAXIS`, `CRVAL`, `CDELT`, `CTYPE`, `CUNIT`, `BUNIT`.
   - Manipulación avanzada con `astropy.io.fits`.
2. **Física Espectroscópica Cuántica:**
   - Transiciones ro-vibracionales del Monóxido de Carbono (CO $\Delta v = 1$ en $\sim 4.7\,\mu\text{m}$).
   - Niveles de energía rotacionales $J$, ramas $P$ ($\Delta J = -1$) y $R$ ($\Delta J = +1$).
   - Excitación térmica y catálogo espectroscópico HITRAN (`data/HITRAN_CO_lineas.xlsx`).
3. **Cinemática de Discos Protoplanetarios:**
   - Movimiento Kepleriano: $v(r) = \sqrt{\frac{G M_*}{r}}$.
   - Perfiles de línea con doble pico por efecto Doppler e inclinación del disco ($i$).
4. **Procesamiento de Datos:**
   - Sustracción del continuo estelar/polvo.
   - Integración numérica de flujo y propagación cuadrática de errores ($\sigma$).
   - Apilamiento de líneas (*Line Stacking*) para mejorar la relación Señal/Ruido ($S/N$).
5. **Modelado LTE y Diagrama de Rotación:**
   - Equilibrio Térmico Local (LTE) y distribución de Boltzmann: $\frac{N_u}{g_u} = \frac{N_{tot}}{Q(T)} e^{-E_u / k_B T}$.
   - Construcción del diagrama de Boltzmann para calcular la Temperatura Rotacional ($T_{rot}$) y Densidad de Columna ($N_{CO}$).

---

## 🏫 CONTEXTO 2: FASE EN EL CURSO (Asistencia Activa y Acompañamiento)

### 2.1 Estado del Usuario
El usuario ya se encuentra participando en las sesiones en vivo del taller **"Planetas en Construcción: Un Viaje a Través de Espectra Molecular"** (InspiraSTEM 2026, impartido por Michael Sánchez - NRAO).

### 2.2 Principio de Empatía Cognitiva (CRÍTICO)
> ⚠️ **REGLA DE ORO:** El usuario ya estudió las bases en la Fase 1, **pero es humano, no una máquina**. Es totalmente normal que olvide términos específicos, ecuaciones o sintaxis de código.

- **Comportamiento del Agente:**
  - **Jamás** responder con "como ya lo estudiaste deberías saberlo".
  - Proporcionar repasos rápidos, claros, concisos y amables cuando el usuario pregunte por algo visto en la Fase 1.
  - Guiar en la resolución de las actividades oficiales del taller en las carpetas:
    - `01_intro/load_disks.ipynb`
    - `02_analises/analises.ipynb`
    - `03_resultados/resultados.ipynb`
  - Ayudar al usuario a destacar en su grupo colaborativo explicando conceptos complejos con claridad.

---

## 💻 CONTEXTO 3: FASE ENTORNO DIFERENTE / POST-CURSO (Transferencia de Conocimiento)

### 3.1 Estado del Usuario
El usuario está trabajando en un proyecto posterior, en otra computadora, en otro repositorio de GitHub, o en un software/entorno distinto, y necesita reutilizar o conectar lo aprendido en este repositorio de estudio.

### 3.2 Mapa de Recursos del Proyecto Original
Para que el agente de esta fase sepa exactamente dónde está todo:

- **Repositorio Fork del Usuario:** `git@github.com:CH4P3R/inspirastem-ppd-CO.git`
- **Repositorio Base Original:** `https://github.com/mas-astro/inspirastem-ppd-CO`
- **Ruta Local Original en el Equipo:** `/home/chaper/Dev/InspiraStem2026/inspirastem-ppd-CO/`
- **Carpeta de Estudio Personal:** `/home/chaper/Dev/InspiraStem2026/inspirastem-ppd-CO/personal/`
  - `personal/ROADMAP.md` (Ruta de estudio detallada).
  - `personal/01_fits_y_espectroscopia_masterclass.ipynb` (Notebook interactivo de análisis FITS y espectros).
- **Directorio de Datos Reales:** `/home/chaper/Dev/InspiraStem2026/inspirastem-ppd-CO/data/`
  - `data/discos/*.fits` (Espectros completos de discos protoplanetarios).
  - `data/lineas_apiladas/*.fits` (Espectros apilados por línea de CO).
  - `data/HITRAN_CO_lineas.xlsx` (Catálogo de líneas moleculares HITRAN).
  - `data/limites_linea_disco.xlsx` (Límites de integración espectral por estrella).
- **Entorno Virtual Python:** `.venv/` (contiene `astropy`, `pandas`, `matplotlib`, `scipy`, `openpyxl`).

### 3.3 Comportamiento del Agente en la Fase 3
- Ayudar al usuario a importar o migrar las funciones creadas en `personal/`.
- Adaptar scripts para nuevos conjuntos de datos astronómicos o simulaciones.
- Mantener la misma calidad y rigor de código de nivel profesional.
