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
                 delay: int = 2,
                 intervall: int = 5,
                 solar_ip1: str = "192.168.178.35",
                 solar_ip2: str = "",
                 heizon: int = -6500,
                 heizoff: int = -100,
                 g_length: int = 9):
        self.heiz = False
        self.skip = False
        self.offset = time.time()
        self.delay = delay
        self.intervall = intervall
        self.load = 0
        self.pv1 = 0
        self.g_akku = 0
        self.g_netz = 0
        self.soc = 0
        self.counter = -1
        self.g_length = g_length

        self.solar_ip1 = solar_ip1
        self.solar_ip2 = solar_ip2
        self.heizon = heizon
        self.heizoff = heizoff

        self.netz_values = []
        self.akku_values = []
        self.logger = logging.getLogger("API_Logger")

        self.power_data = None

    def get_data_from_url(self, ip, endpoint):
        """Ruft Daten von einer URL ab und gibt sie als JSON zurück. Gibt None zurück bei Fehler."""
        url = f"http://{ip}/{endpoint}"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            self.power_data = response.json()
        except requests.RequestException as e:
            self.logger.error(f"Erroor {e}")

if __name__ == "__main__":
    api = Dataexport(offset=time.time())
    api.get_data_from_url(ip = api.solar_ip1, endpoint = "solar_api/v1/GetPowerFlowRealtimeData.fcgi")