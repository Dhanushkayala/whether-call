# AegisCyclone - Cyclone Impact & Infrastructure Vulnerability Forecaster
## Track 5: Anticipatory Action, Storm Surge Modeling & GEE AI Platform

### Overview
**AegisCyclone** is an end-to-end, AI-powered predictive risk and vulnerability modeling platform designed for the Bay of Bengal and coastal APAC regions. It shifts disaster management from reactive post-landfall relief to **proactive pre-landfall anticipatory action**.

---

### Core Features

1. **Storm Surge & Inundation Physics Modeling**:
   - Modified SLOSH and parametric coastal bathymetric wind-stress modeling.
   - Computes dynamic surge height based on central pressure drop ($\Delta P$), sustained wind velocity ($U_{10}$), fetch length, shallow shelf bathymetry, and astronomical tidal phase superposition.
   - Interactive cross-sectional coastal transect depth profile from 0km coastline inland to 15km.

2. **Critical Infrastructure Multi-Hazard Exposure Graph**:
   - Live vulnerability tracking of 220kV/132kV power substations, arterial highways, bridges, multi-purpose cyclone shelters, trauma hospitals, and telecom cellular towers.
   - Dynamic threshold breach evaluation for wind shear ($>120\text{ km/h}$) and inundation depth ($>0.3\text{m}$ for roads, $>0.5\text{m}$ for substations).

3. **Google Earth Engine (GEE) Sentinel-1 SAR & Sentinel-2 Optical Feeds**:
   - Synthetic Aperture Radar (SAR) double-bounce backscatter thresholding ($-15.5\text{ dB}$) for cloud-penetrating water inundation detection.
   - Real-time flood area estimation ($km^2$), cropland loss hectares, and vegetation defoliation index.

4. **Timeline Forecasting Engine**:
   - Interactive scrubber tracking storm progression through $T-72\text{h}$, $T-48\text{h}$, $T-24\text{h}$, $T-12\text{h}$, $T-0$ (Landfall), $T+12\text{h}$, and $T+24\text{h}$.
   - Auto-simulation playback with live updating of storm metrics and map markers.

5. **AI Multimodal Advisory & Multilingual Early-Warning Dispatch**:
   - Automated generation of structured Incident Command Directives.
   - Tailored targeting for:
     - **NDRF & State Disaster Management Authorities (SDMA)**
     - **District Magistrates & Municipal Collectors**
     - **Port & Maritime Authorities**
     - **Coastal Fisherfolk & Vulnerable Communities**
   - Instant translation across 6 regional coastal languages: **English, Hindi, Bengali, Odia, Tamil, and Telugu**.
   - One-click export to official **PDF Emergency Action Directive** and Common Alerting Protocol (CAP) SMS simulation.

6. **Flood-Safe Evacuation Route Optimizer**:
   - Computes flood-safe evacuation corridors avoiding inundated causeways (e.g. routing via elevated SH-9A instead of submerged NH-516A).
   - Computes convoy transit times and flags wind-shear bridge choke points.

7. **Parametric Insurance Immediate Liquidity Trigger**:
   - Automated real-time parametric threshold evaluation ($140\text{ km/h}$ wind OR $2.0\text{m}$ surge OR $250\text{mm}$ rainfall).
   - Authorizes immediate $\$15,000,000$ USD emergency SDRF liquidity payout within 24 hours without waiting for physical claims adjustment.

---

### Pre-loaded Scenarios
- **Cyclone Dana (2024)**: Very Severe Cyclonic Storm hitting Dhamra / Bhitarkanika Coast, Odisha.
- **Super Cyclone Amphan (2020)**: Category-5 Super Cyclonic Storm hitting Sundarbans & West Bengal.
- **Cyclone Michaung (2023)**: Severe Cyclonic Storm affecting Chennai / Bapatla, South Andhra Coast.
- **Custom Real-Time Physics Simulator**: Interactive sliders for custom central pressure, wind velocity, and tidal stage.

---

### Quick Start Guide

#### Option A: Run Standalone Web Dashboard (Zero Setup)
Simply open `output/index.html` directly in any web browser (Chrome, Edge, Firefox, Safari). All GIS mapping, simulation controls, PDF generation, and advisory capabilities work out of the box with zero installation!

#### Option B: Run with Python FastAPI Backend
1. Open a terminal in `output/backend/`:
   ```bash
   cd "C:\projects\cyclone detection app\output\backend"
   pip install -r requirements.txt
   ```
2. Start the FastAPI server:
   ```bash
   python main.py
   ```
3. The API server will be live at `http://localhost:8000` with interactive Swagger docs at `http://localhost:8000/docs`.
