# Import the sys module
import sys

# Create a variable to store the database path
DATABASE_PATH = "clientes.csv"

# If the current script is being run by pytest, change the database path
if "pytest" in sys.argv[0]:
    DATABASE_PATH = "tests/clientes_test.csv"