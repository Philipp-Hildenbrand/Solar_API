#       ___         __ _
#     / ___|      / _| |  _      ____   _    ___
#    \___ \ / _ \| |_| __\ \ /\ / / _` | '__/ _ \
#     ___) | (_) |  _| |_ \ V  V / (_| | | |  __/
#    |____/ \___/|_|  \__| \_/\_/ \__,_|_|  \___|
# Changes: convert all old code into class
# © Philipp Hildenbrand
# Created: 23.11.2024 16:33, Changed: 14.12.2024 12:45
# philipphildenbrand@t-online.de

# Imports
import requests, time, os, logging#, RPi.GPIO as GPIO
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.DEBUG)

#GPIO.setup(17, GPIO.OUT)
#GPIO.output(17, False)

# Configurations
class Dataexport():
    def __init__(self,
                 offset: float,
                 heiz: bool = False,
                 skip: bool = False,
                 delay: int = 2,
                 intervall: int = 5):
        self.heiz = heiz
        self.skip = skip
        self.offset = offset
        print(f"Beginn offset {self.offset}")
        self.delay = delay
        self.intervall = intervall
        self.load = 0
        self.pv1 = 0
        self.g_akku = 0
        self.g_netz = 0
        self.soc = 0
        self.counter = 0

        self.solar_ip1 = "ip"
        self.solar_ip2 = "ip"
        self.heizon = -6500
        self.heizoff = -100

        self.netz_values = []
        self.akku_values = []
        self.logger = logging.getLogger("API_Logger")


    def get_data_from_url(self, ip, endpoint):
        """Ruft Daten von einer URL ab und gibt sie als JSON zurück. Gibt None zurück bei Fehler."""
        url = f"http://{ip}/{endpoint}"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return None