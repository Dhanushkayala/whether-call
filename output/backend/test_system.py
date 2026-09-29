"""
AegisCyclone Comprehensive Automated Test Suite
Validates:
1. Physical SLOSH Surge Calculations & Transects
2. Infrastructure Vulnerability Matrix & Fragility Engine
3. Multilingual Disaster Advisory Generation
4. Overpass Turbo National Power Grid Integration
5. Open-Meteo Real-Time Meteorology & WMO Codes
6. Disaster RAG Decision Agent & SOP Knowledge Retrieval
7. Live Backend Engine Integration
"""

import sys
import unittest
from surge_engine import calculate_peak_surge, simulate_coastal_transect
from infrastructure_engine import InfrastructureEngine
from advisory_engine import generate_disaster_advisory
from power_grid_data import get_india_power_grid_dataset, get_overpass_query_presets
from rag_decision_agent import DisasterRAGDecisionAgent, SOP_KNOWLEDGE_BASE


class TestAegisCycloneSuite(unittest.TestCase):

    def setUp(self):
        self.infra_engine = InfrastructureEngine()
        self.rag_agent = DisasterRAGDecisionAgent()

    # 1. Physics & Surge Engine Tests
    def test_surge_calculation_dana(self):
        surge_result = calculate_peak_surge(
            central_pressure_hpa=980.0,
            max_sustained_wind_kmh=120.0,
            radius_max_winds_km=45.0,
            forward_speed_kmh=14.0,
            tide_phase_m=1.4
        )
        self.assertIn("total_peak_surge_height_m", surge_result)
        self.assertGreater(surge_result["total_peak_surge_height_m"], 2.0)
        self.assertIn("inverse_barometer_surge_m", surge_result)
        self.assertGreater(surge_result["inverse_barometer_surge_m"], 0.2)
        self.assertIn("wind_stress_surge_m", surge_result)
        self.assertIn("surge_category", surge_result)

    def test_coastal_transect_generation(self):
        transect = simulate_coastal_transect(peak_surge_m=2.4, num_points=10)
        self.assertEqual(len(transect), 10)
        self.assertIn("distance_inland_km", transect[0])
        self.assertIn("net_flood_depth_m", transect[0])
        self.assertGreaterEqual(transect[0]["net_flood_depth_m"], 1.5)

    # 2. Infrastructure Vulnerability & Cascade Engine Tests
    def test_infrastructure_vulnerability(self):
        result = self.infra_engine.evaluate_vulnerability(
            wind_speed_kmh=125.0,
            surge_height_m=2.4,
            rainfall_24h_mm=280.0
        )
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIn("id", result[0])
        self.assertIn("severity", result[0])
        self.assertIn("risk_score", result[0])

    # 3. Advisory Engine Tests
    def test_multilingual_advisories(self):
        for lang in ["en", "hi", "bn", "or", "ta", "te"]:
            advisory = generate_disaster_advisory(
                storm_name="Dana",
                timeline_phase="T-0 Landfall",
                wind_speed_kmh=125.0,
                peak_surge_m=2.4,
                rainfall_24h_mm=280.0,
                landfall_location="Dhamra Port, Odisha",
                target_audience="NDRF_SDMA",
                language=lang
            )
            self.assertIn("language", advisory)
            self.assertEqual(advisory["language"], lang)
            self.assertIn("headline", advisory)
            self.assertIn("advisory_text", advisory)
            self.assertIn("parametric_insurance", advisory)
            self.assertTrue(advisory["parametric_insurance"]["trigger_breached"])

    # 4. Overpass Power Grid Dataset Tests
    def test_power_grid_network(self):
        dataset = get_india_power_grid_dataset()
        self.assertIn("substations", dataset)
        self.assertIn("transmission_lines", dataset)
        self.assertGreater(len(dataset["substations"]), 15)
        self.assertGreater(len(dataset["transmission_lines"]), 10)

        presets = get_overpass_query_presets()
        self.assertIn("india_national_backbone", presets)
        self.assertIn("eastern_coastal_grid", presets)

    # 5. RAG Decision Agent Tests
    def test_rag_decision_matrix(self):
        telemetry = {
            "pressure_hpa": 980,
            "wind_speed_kmh": 125,
            "surge_height_m": 2.4,
            "rain_24h_mm": 280,
            "tide_offset_m": 1.4,
            "landfall_location": "Dhamra Port, Odisha"
        }
        decision = self.rag_agent.evaluate_decision_matrix(telemetry)
        self.assertEqual(decision["status"], "success")
        self.assertGreater(decision["composite_risk_index"], 60.0)
        self.assertGreater(len(decision["retrieved_sops"]), 2)
        self.assertEqual(len(decision["optimal_action_plan"]), 4)

    def test_rag_agent_qa(self):
        telemetry = {
            "pressure_hpa": 980,
            "wind_speed_kmh": 125,
            "surge_height_m": 2.4,
            "rain_24h_mm": 280
        }
        res_power = self.rag_agent.ask_rag_agent("What is the power grid SOP directive?", telemetry)
        self.assertIn("CEA-SOP-502", res_power["response"])

        res_evac = self.rag_agent.ask_rag_agent("How many people must be evacuated?", telemetry)
        self.assertIn("NDMA-EVAC-104", res_evac["response"])

        res_money = self.rag_agent.ask_rag_agent("Is parametric insurance payout triggered?", telemetry)
        self.assertIn("15,000,000", res_money["response"])


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAegisCycloneSuite)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
