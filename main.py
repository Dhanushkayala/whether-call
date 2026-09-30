import os
import sys
import importlib.util

# Ensure root and backend directory are in sys.path
root_dir = os.path.abspath(os.path.dirname(__file__))
backend_dir = os.path.join(root_dir, "output", "backend")

if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

# Load backend main.py explicitly to avoid circular 'main' import conflict
backend_main_file = os.path.join(backend_dir, "main.py")
spec = importlib.util.spec_from_file_location("weathercall_backend_main", backend_main_file)
weathercall_backend_main = importlib.util.module_from_spec(spec)
sys.modules["weathercall_backend_main"] = weathercall_backend_main
spec.loader.exec_module(weathercall_backend_main)

app = weathercall_backend_main.app

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
