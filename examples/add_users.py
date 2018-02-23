import sys
from xmcuserimporter import Parser

# python add_user.py <config_file> <csv_file>

if __name__ == "__main__":
    config_filename = sys.argv[1]
    csv_filename = sys.argv[2]

    Parser(config_filename, csv_filename).import_users()