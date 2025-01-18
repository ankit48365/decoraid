# tests/test_cpdec.py
# install local here ~ pip install -e .
# pytest -v tests/test_cpdec.py
import os
from decoraid.cpdec import check_package

def test_check_package():
    # Setup
    venv_path = os.getenv('VIRTUAL_ENV', '.venv')
    package = 'pytest'
    
    @check_package(package, venv_path)
    def dummy_function():
        return "Function executed successfully."
    
    # Execute and Assert
    result = dummy_function()
    assert result == "Function executed successfully."
