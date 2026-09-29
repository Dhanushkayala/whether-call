"""
Storm Surge & Inundation Physics Simulation Engine for AegisCyclone.
Implements modified SLOSH (Sea, Lake, and Overland Surges from Hurricanes)
and parametric coastal bathymetric wind-stress models.
"""

import math
from typing import Dict, List, Any, Tuple

def calculate_peak_surge(
    central_pressure_hpa: float,
    max_sustained_wind_kmh: float,
    radius_max_winds_km: float,
    forward_speed_kmh: float,
    tide_phase_m: float = 1.2,
    coastal_bathymetry_slope: float = 0.001,  # typical shallow Bay of Bengal shelf
    ambient_pressure_hpa: float = 1013.25
) -> Dict[str, Any]:
    """
    Computes peak storm surge height and dynamic surge profile at landfall.
    """
    # 1. Inverse Barometer Effect (approx 1 cm rise per 1 hPa drop)
    delta_p = max(0.0, ambient_pressure_hpa - central_pressure_hpa)
    inverse_barometer_m = delta_p * 0.0101

    # 2. Wind Stress Driven Surge over continental shelf (Proudman resonance & wind drag)
    # Wind speed in m/s
    v_ms = max_sustained_wind_kmh / 3.6
    # Drag coefficient Cd parameterized with wind speed (Wu, 1982)
    cd = (0.8 + 0.065 * v_ms) * 1e-3
    rho_air = 1.225      # kg/m^3
    rho_water = 1025.0   # kg/m^3
    g = 9.81             # m/s^2
    fetch_length_km = 80.0  # effective shallow water fetch
    avg_depth_m = 18.0   # shallow coastal shelf depth

    wind_surge_m = (rho_air * cd * (v_ms ** 2) * (fetch_length_km * 1000.0)) / (rho_water * g * avg_depth_m)

    # 3. Forward Motion & Bay Funneling Factor (Bay of Bengal apex amplifies by 1.2 - 1.45x)
    funneling_factor = 1.32
    forward_motion_bonus = (forward_speed_kmh / 30.0) * 0.35

    total_dynamic_surge = (inverse_barometer_m + wind_surge_m) * funneling_factor + forward_motion_bonus
    total_water_level = total_dynamic_surge + tide_phase_m

    # Inundation extent (inland penetration in km depending on slope and vegetation roughness)
    # Inland penetration approx = Total Water Level / coastal slope * attenuation factor (0.45 due to roughness)
    inland_penetration_km = (total_water_level / (coastal_bathymetry_slope * 1000.0)) * 0.35

    return {
        "central_pressure_hpa": central_pressure_hpa,
        "max_sustained_wind_kmh": max_sustained_wind_kmh,
        "inverse_barometer_surge_m": round(inverse_barometer_m, 2),
        "wind_stress_surge_m": round(wind_surge_m, 2),
        "astronomical_tide_m": round(tide_phase_m, 2),
        "total_peak_surge_height_m": round(total_water_level, 2),
        "inland_inundation_extent_km": round(inland_penetration_km, 1),
        "surge_category": classify_surge_severity(total_water_level)
    }

def classify_surge_severity(surge_height_m: float) -> str:
    if surge_height_m < 1.5:
        return "Moderate (Yellow Alert)"
    elif surge_height_m < 3.0:
        return "Severe (Orange Alert)"
    elif surge_height_m < 5.0:
        return "Very Severe (Red Alert - Mandatory Evacuation)"
    else:
        return "Catastrophic (Purple Alert - Extreme Structural Risk)"

def simulate_coastal_transect(
    peak_surge_m: float,
    num_points: int = 10
) -> List[Dict[str, Any]]:
    """
    Generates depth profile along coastal transect from 0km coastline inland up to 15km.
    """
    transect = []
    for i in range(num_points):
        dist_km = i * 1.5
        # Exponential attenuation inland + elevation rise
        elevation_m = 0.5 + (dist_km * 0.6)
        water_surface_m = peak_surge_m * math.exp(-0.18 * dist_km)
        inundation_depth_m = max(0.0, water_surface_m - elevation_m)

        transect.append({
            "distance_inland_km": round(dist_km, 1),
            "land_elevation_m": round(elevation_m, 2),
            "water_surface_level_m": round(water_surface_m, 2),
            "net_flood_depth_m": round(inundation_depth_m, 2),
            "status": "Flooded" if inundation_depth_m > 0.05 else "Dry / Safe"
        })
    return transect
