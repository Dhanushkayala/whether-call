"""
Critical Infrastructure Vulnerability & Exposure Analytics Engine
Quantifies multi-hazard risk: Risk = Hazard_Intensity * Exposure * Fragility_Index
"""

from typing import List, Dict, Any

class InfrastructureEngine:
    def __init__(self):
        # Sample coastal infrastructure graph dataset (Bay of Bengal / APAC coastal nodes)
        self.nodes = [
            {
                "id": "PWR-01",
                "name": "Dhamra 220kV High-Voltage Coastal Substation",
                "type": "power_substation",
                "lat": 20.812,
                "lon": 86.974,
                "elevation_m": 1.8,
                "wind_tolerance_kmh": 150,
                "flood_tolerance_m": 0.6,
                "criticality": "Extremely High (Powers 350,000 residents + Port)",
                "population_served": 350000
            },
            {
                "id": "PWR-02",
                "name": "Paradeep 132kV Thermal Distribution Yard",
                "type": "power_substation",
                "lat": 20.264,
                "lon": 86.671,
                "elevation_m": 2.2,
                "wind_tolerance_kmh": 140,
                "flood_tolerance_m": 0.8,
                "criticality": "Critical (Industrial & Water supply)",
                "population_served": 220000
            },
            {
                "id": "RD-01",
                "name": "Arterial Coastal Highway NH-516A (Causeway Bridge)",
                "type": "arterial_road",
                "lat": 20.655,
                "lon": 86.892,
                "elevation_m": 1.2,
                "wind_tolerance_kmh": 120,
                "flood_tolerance_m": 0.3,
                "criticality": "Primary Evacuation Corridor #1",
                "population_served": 180000
            },
            {
                "id": "RD-02",
                "name": "State Highway SH-9A Bypass Corridor",
                "type": "arterial_road",
                "lat": 20.520,
                "lon": 86.540,
                "elevation_m": 4.5,
                "wind_tolerance_kmh": 130,
                "flood_tolerance_m": 0.5,
                "criticality": "Secondary Inbound Relief Route",
                "population_served": 120000
            },
            {
                "id": "SHT-01",
                "name": "Bhitarkanika Multi-Purpose Cyclone Shelter",
                "type": "shelter",
                "lat": 20.720,
                "lon": 86.870,
                "elevation_m": 5.2,
                "wind_tolerance_kmh": 260,
                "flood_tolerance_m": 3.5,
                "criticality": "Life Safety (Capacity: 3,500 people)",
                "capacity": 3500,
                "generator_elevated": True
            },
            {
                "id": "SHT-02",
                "name": "Kendrapara District Emergency Medical Center",
                "type": "medical_shelter",
                "lat": 20.501,
                "lon": 86.422,
                "elevation_m": 6.8,
                "wind_tolerance_kmh": 220,
                "flood_tolerance_m": 2.5,
                "criticality": "Regional Trauma & ICU Center",
                "capacity": 1200,
                "generator_elevated": True
            },
            {
                "id": "TEL-01",
                "name": "Chandbali Coastal Cellular & Microwave Tower",
                "type": "telecom_tower",
                "lat": 20.778,
                "lon": 86.745,
                "elevation_m": 2.5,
                "wind_tolerance_kmh": 135,
                "flood_tolerance_m": 1.2,
                "criticality": "Emergency SOS / CAP Broadcast Node",
                "battery_backup_hours": 18
            },
            {
                "id": "WTR-01",
                "name": "Mahanadi Delta Fresh Water Intake & Treatment Facility",
                "type": "water_treatment",
                "lat": 20.312,
                "lon": 86.589,
                "elevation_m": 1.5,
                "wind_tolerance_kmh": 160,
                "flood_tolerance_m": 0.5,
                "criticality": "Potable Water for 400,000 people",
                "population_served": 400000
            }
        ]

    def evaluate_vulnerability(
        self,
        wind_speed_kmh: float,
        surge_height_m: float,
        rainfall_24h_mm: float
    ) -> List[Dict[str, Any]]:
        results = []
        for node in self.nodes:
            # 1. Flood depth calculation at node site
            local_flood_depth = max(0.0, surge_height_m - node["elevation_m"])
            # Additional rain accumulation factor
            rain_ponding_m = (rainfall_24h_mm / 1000.0) * 0.45
            total_inundation_m = round(local_flood_depth + (rain_ponding_m if node["elevation_m"] < 3.0 else 0.0), 2)

            # 2. Fragility evaluation
            wind_fail = wind_speed_kmh >= node["wind_tolerance_kmh"]
            flood_fail = total_inundation_m >= node["flood_tolerance_m"]

            # Failure Probability / Severity
            severity = "Operational / Safe"
            risk_score = 15
            actions = ["Maintain standard monitoring"]

            if flood_fail and wind_fail:
                severity = "Catastrophic Failure / Submerged"
                risk_score = 95
                actions = [
                    "Immediate proactive de-energization / isolation",
                    "Evacuate personnel immediately",
                    "Divert arterial traffic to secondary inland corridors"
                ]
            elif flood_fail:
                severity = "Critical Risk - Inundation Breach"
                risk_score = 80
                actions = [
                    "Deploy high-capacity de-watering submersibles",
                    "Activate elevated backup gen-sets",
                    "Restrict vehicular passage (Depth > 30cm)"
                ]
            elif wind_fail:
                severity = "High Warning - Wind Shear Danger"
                risk_score = 65
                actions = [
                    "Pre-position rapid restoration line-crews",
                    "Secure antenna mast guy-wires",
                    "Lock down moveable mechanical fixtures"
                ]
            elif (wind_speed_kmh >= node["wind_tolerance_kmh"] * 0.8) or (total_inundation_m >= node["flood_tolerance_m"] * 0.6):
                severity = "Elevated Alert - Approaching Threshold"
                risk_score = 45
                actions = ["Standby rapid response teams"]

            results.append({
                "id": node["id"],
                "name": node["name"],
                "type": node["type"],
                "lat": node["lat"],
                "lon": node["lon"],
                "elevation_m": node["elevation_m"],
                "projected_flood_depth_m": total_inundation_m,
                "wind_exposure_kmh": round(wind_speed_kmh, 1),
                "severity": severity,
                "risk_score": risk_score,
                "criticality": node["criticality"],
                "recommended_actions": actions
            })
        return results
