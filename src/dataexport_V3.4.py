# Philipp Hildenbrand
# 07.12.2024 12:45
# philipphildenbrand@t-online.de
class Dataexport():
    def __init__(self):
        self.heiz = 0
        self.skip = 0
        self.offset = time.time()
        print(f"Beginn offset {self.offset}")
        self.delay = 2
        self.intervall = 30
        self.load = 0
        self.pv1 = 0
        self.g_akku = 0
        self.g_netz = 0
        self.soc = 0
        self.counter = 0

        # Konfiguration
        self.solar_ip1 = "ip"
        self.solar_ip2 = "ip"
        self.heizon = -6500
        self.heizoff = -100

        self.netz_values = []
        self.akku_values = []
    def get_data_from_url(self, ip, endpoint):
        """Ruft Daten von einer URL ab und gibt sie als JSON zurück. Gibt None zurück bei Fehler."""
        url = f"http://{ip}/{endpoint}"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return None                             # Bei Fehler None zurückgeben
