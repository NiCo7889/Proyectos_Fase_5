# Import the sys module
import sys

# Create a variable to store the database path
DATABASE_PATH = "inventario.csv"

# If the current script is being run by pytest, change the database path
if "pytest" in sys.argv[0]:
    DATABASE_PATH = "tests/inventario_test.csv"