# 🚀 Plan de Estudio de Alto Nivel: Astrofísica de Discos Protoplanetarios y Espectroscopía (NASA / Silicon Valley Standard)

Este documento define la ruta de aprendizaje exhaustiva, rigurosa y práctica para dominar el procesamiento de datos astronómicos, la física de discos protoplanetarios y la espectroscopía moleculares con **Python** y **Astropy**.

---

## 📌 Módulo 1: Estándar FITS (Flexible Image Transport System) y Manipulación con `Astropy`
- **Fundamentos del formato FITS (IAU standard):**
  - Estructura de bloques de 2880 bytes.
  - Concepto de HDU (*Header Data Unit*): `PrimaryHDU`, `ImageHDU`, `BinTableHDU`.
  - Anatomía del Header: Pares clave-valor (`BITPIX`, `NAXIS`, `CRVAL`, `CDELT`, `CTYPE`, `CUNIT`, `BUNIT`).
  - Sistema de Coordenadas del Mundo (WCS - *World Coordinate System*).
- **Práctica en `personal/01_fits_deep_dive.ipynb`:**
  - Inspección profunda de los FITS en `data/discos/` y `data/lineas_apiladas/`.
  - Extracción de datos tabulares binarios (`BinTableHDU`) y metadatos de observación.

---

## 📌 Módulo 2: Fundamentos de Espectroscopía Molecular y Astrofísica de Discos
- **Mecanismos Físicos:**
  - Transiciones ro-vibracionales del Monóxido de Carbono (CO $\Delta v = 1$ cerca de $4.7\,\mu\text{m}$).
  - Ramas $P$, $R$ y $Q$ en espectros diatómicos.
  - Catálogo de transiciones HITRAN (lectura de `data/HITRAN_CO_lineas.xlsx`).
- **Cinemática del Disco Protoplanetario:**
  - Rotación Kepleriana $v(r) = \sqrt{\frac{G M_*}{r}}$.
  - Efecto Doppler y perfiles de línea con doble pico (*double-peaked profiles*).
  - Ángulo de inclinación del disco ($i$) y ensanchamiento térmico/turbulento.

---

## 📌 Módulo 3: Procesamiento de Datos y Análisis Espectroscópico
- **Normalización de Continuo:**
  - Separación de la emisión del continuo estelar/polvo de la emisión de líneas de gas.
  - Ajuste polinomial por tramos (*spline* / orden 1-3).
- **Medición de Flujo e Integración:**
  - Integración numéricas del flujo en las líneas $P1, P2, \dots, R0, R1$.
  - Propagación rigurosa de errores estadísticos ($\sigma_{flux}$).
  - Apilamiento de líneas (*Line Stacking*) para incrementar la relación señal/ruido ($S/N$).

---

## 📌 Módulo 4: Modelado Espectroscópico y Diagramas de Rotación (LTE)
- **Equilibrio Térmico Local (LTE):**
  - Población de niveles según la distribución de Boltzmann: $\frac{N_u}{g_u} = \frac{N_{tot}}{Q(T)} e^{-E_u / k_B T}$.
  - Construcción del Diagrama de Rotación (Boltzmann Plot): $\ln(N_u / g_u)$ vs $E_u / k_B$.
  - Determinación de la Temperatura Rotacional ($T_{rot}$) y la Densidad de Columna ($N_{CO}$).

---

## 📌 Módulo 5: Contexto Astrofísico y Comparación de la Muestra
- Caracterización individual de la muestra (`TWHya`, `EXLup`, `HD142527`, `DoAr44`, `RULup`, etc.).
- Comparación de condiciones físicas en discos de estrellas T Tauri vs Herbig Ae/Be.
- Implicaciones en la formación de exoplanetas y estructura de discos (cavidades, gaps).
