# Imports
import pandas as pd
from datetime import datetime

def dated(date_string):
    try:
        if date_string != datetime.strptime(date_string, "%Y-%m-%d").strftime("%Y-%m-%d"):
            raise ValueError
        return True
    except ValueError:
        return False