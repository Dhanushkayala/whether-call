"""
AI Multimodal Early Warning Advisory & Parametric Insurance Dispatch Engine
Generates multilingual actionable bulletins for municipal & disaster response bodies.
"""

from typing import Dict, Any, List

def generate_disaster_advisory(
    storm_name: str,
    timeline_phase: str,
    wind_speed_kmh: float,
    peak_surge_m: float,
    rainfall_24h_mm: float,
    landfall_location: str,
    target_audience: str = "NDRF_SDMA",
    language: str = "en"
) -> Dict[str, Any]:
    """
    Generates targeted actionable directives with multilingual support.
    """

    # 1. Evaluate Parametric Insurance Trigger
    parametric_trigger_breached = (wind_speed_kmh >= 140.0) or (peak_surge_m >= 2.0) or (rainfall_24h_mm >= 250.0)
    parametric_payout_amount_usd = 15000000 if parametric_trigger_breached else 0

    # 2. Audience Content Generation
    if target_audience == "NDRF_SDMA":
        title = f"EMERGENCY ACTION DIRECTIVE: CYCLONE {storm_name.upper()} ({timeline_phase})"
        bulletin_body_en = (
            f"URGENT: Landfall projected at {landfall_location} with sustained winds of {wind_speed_kmh} km/h "
            f"and catastrophic storm surge of {peak_surge_m}m above astronomical tide. "
            f"24h rainfall estimate: {rainfall_24h_mm} mm.\n\n"
            f"MANDATORY DIRECTIVES:\n"
            f"1. Complete Tier-1 coastal evacuation within 5km zone before T-12 hours.\n"
            f"2. Pre-position 14 NDRF battalions with inflatable motorboats & tree-clearing power saws along NH-516A.\n"
            f"3. Proactively island coastal power substations (PWR-01, PWR-02) 4 hours prior to landfall.\n"
            f"4. Direct emergency ambulance traffic exclusively via SH-9A elevated corridor."
        )
    elif target_audience == "MUNICIPAL_COLLECTORS":
        title = f"DISTRICT DISASTER MANAGEMENT ADVISORY: {storm_name.upper()}"
        bulletin_body_en = (
            f"To All Coastal Block Development Officers (BDOs) & Tehsildars:\n"
            f"1. Open and provision all Category-A Cyclone Shelters with 72-hour food rations and water bladders.\n"
            f"2. Enforce strict Section 144 along beaches and sea-dikes; zero human activity permitted.\n"
            f"3. High-capacity dewatering pumps to be staged at low-lying municipal wards.\n"
            f"4. Ensure diesel fuel stocks for hospital backup generators are filled to 100% capacity."
        )
    elif target_audience == "PORTS_MARITIME":
        title = f"GREAT DANGER SIGNAL #10 - MARITIME & PORT AUTHORITY"
        bulletin_body_en = (
            f"Hoist Great Danger Signal No. 10 at all local ports.\n"
            f"1. Cease all cargo handling, crane operations, and bunkering immediately.\n"
            f"2. Order all deep-sea trawlers and coastal vessels to secure in designated inner creek anchorages.\n"
            f"3. Evacuate all non-essential harbor personnel from berths prone to {peak_surge_m}m wave overtopping."
        )
    else:  # PUBLIC_FISHERFOLK
        title = f"RED ALERT FOR COASTAL RESIDENTS & FISHERMEN"
        bulletin_body_en = (
            f"Total suspension of fishing operations in deep sea and coastal waters.\n"
            f"Move to nearest designated cyclone shelter immediately.\n"
            f"Do not stay in thatched or kutcha houses. Keep emergency documents in waterproof bags."
        )

    # 3. Multilingual Translations
    translations = {
        "en": bulletin_body_en,
        "hi": (
            f"आपातकालीन कार्रवाई निर्देश: चक्रवात {storm_name.upper()} ({timeline_phase})\n"
            f"स्थान: {landfall_location}। हवा की गति: {wind_speed_kmh} किमी/घंटा, तूफानी लहरें: {peak_surge_m} मीटर।\n"
            f"1. 5 किमी तटीय क्षेत्र से तत्काल निकासी पूर्ण करें।\n"
            f"2. एनडीआरएफ की टीमों को मुख्य राजमार्गों पर तैनात किया गया है।\n"
            f"3. सभी तटीय बिजली सबस्टेशनों को समय रहते सुरक्षित करें।"
        ),
        "bn": (
            f"জরুরী বিপর্যয় সতর্কতা: ঘূর্ণিঝড় {storm_name.upper()} ({timeline_phase})\n"
            f"আছড়ে পড়ার স্থান: {landfall_location}। বাতাসের গতিবেগ: {wind_speed_kmh} কিমি/ঘন্টা, জলোচ্ছ্বাস: {peak_surge_m} মিটার।\n"
            f"১. উপকূলবর্তী ৫ কিলোমিটার এলাকার সমস্ত বাসিন্দাদের অবিলম্বে সাইক্লোন সেন্টারে সরিয়ে নিন।\n"
            f"২. মৎস্যজীবীদের সমুদ্রে যাওয়ার ওপর সম্পূর্ণ নিষেধাজ্ঞা জারি করা হয়েছে।"
        ),
        "or": (
            f"ଜରୁରୀକାଳୀନ ବାତ୍ୟା ସତର୍କତା: ବାତ୍ୟା {storm_name.upper()} ({timeline_phase})\n"
            f"ସ୍ଥଳଭାଗ ଛୁଇଁବା ସ୍ଥାନ: {landfall_location}। ପବନର ବେଗ: {wind_speed_kmh} କି.ମି/ଘଣ୍ଟା, ଜୁଆର ଉଚ୍ଚତା: {peak_surge_m} ମିଟର।\n"
            f"୧. ଉପକୂଳ ୫ କିଲୋମିଟର ପରିସୀମା ମଧ୍ୟରୁ ସମସ୍ତ ଲୋକଙ୍କୁ ଆଶ୍ରୟସ୍ଥଳକୁ ସ୍ଥାନାନ୍ତର କରନ୍ତୁ।"
        ),
        "ta": (
            f"அவசரகால புயல் எச்சரிக்கை: புயல் {storm_name.upper()} ({timeline_phase})\n"
            f"கரை கடக்கும் இடம்: {landfall_location}. காற்றின் வேகம்: {wind_speed_kmh} கி.மீ/மணி, கடல் அலை எழுச்சி: {peak_surge_m} மீ.\n"
            f"1. கடலோர பகுதியில் உள்ள மக்கள் உடனடியாக புயல் பாதுகாப்பு மையங்களுக்கு செல்லவும்."
        ),
        "te": (
            f"అత్యవసర తుఫాను హెచ్చరిక: తుఫాను {storm_name.upper()} ({timeline_phase})\n"
            f"తీరం దాటే ప్రదేశం: {landfall_location}. గాలి వేగం: {wind_speed_kmh} కిమీ/గం, ఉప్పెన ఎత్తు: {peak_surge_m} మీ.\n"
            f"1. తీరప్రాంత ప్రజలను తక్షణమే సురక్షిత తుఫాను పునరావాస కేంద్రాలకు తరలించండి."
        )
    }

    selected_content = translations.get(language, bulletin_body_en)

    return {
        "storm_name": storm_name,
        "timeline_phase": timeline_phase,
        "language": language,
        "target_audience": target_audience,
        "headline": title,
        "advisory_text": selected_content,
        "metrics_summary": {
            "wind_speed_kmh": wind_speed_kmh,
            "peak_surge_m": peak_surge_m,
            "rainfall_24h_mm": rainfall_24h_mm,
            "landfall_location": landfall_location
        },
        "parametric_insurance": {
            "trigger_breached": parametric_trigger_breached,
            "threshold_criteria": "Wind > 140 km/h OR Surge > 2.0m OR Rain > 250mm",
            "payout_liquidity_usd": parametric_payout_amount_usd,
            "payout_status": "AUTOMATIC DISBURSEMENT AUTHORIZED TO STATE DISASTER FUND" if parametric_trigger_breached else "MONITORING - NO TRIGGER"
        }
    }
