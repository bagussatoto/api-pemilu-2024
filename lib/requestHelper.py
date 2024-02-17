import requests


class requestHelper:
    BASE_URL = "https://sirekap-obj-data.kpu.go.id/"

    def __init__(self):
        self.request = requests.Session()
        self.request.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.response = None

    def get_wilayah(self):
        self.response = self.request.get(self.BASE_URL + "wilayah/pemilu/ppwp/0.json")
        return self.response.json()

    def get_paslon(self):
        self.response = self.request.get(self.BASE_URL + "pemilu/ppwp.json")
        return self.response.json()

    def get_table(self):
        self.response = self.request.get(self.BASE_URL + "pemilu/hhcw/ppwp.json")
        return self.response.json()

    def get_count(self):
        serialized_data_wilayah = []
        serialized_data_paslon = []
        final_data = []

        data_paslon = self.get_paslon()
        for paslon in data_paslon:
            serialized_data_paslon.append({
                "id_paslon": paslon,
                "nama": data_paslon[paslon]["nama"],
                "nomor_urut": data_paslon[paslon]["nomor_urut"],
            })

        data_wilayah = self.get_wilayah()
        for wilayah in data_wilayah:
            serialized_data_wilayah.append({
                "id": wilayah["id"],
                "nama": wilayah["nama"],
                "kode": wilayah["kode"],
            })

        data_table = self.get_table()
        for wilayah in range(len(serialized_data_wilayah)):
            wilayah_data = data_table.get("table")[serialized_data_wilayah[wilayah].get("kode")]
            modified_data = {}
            for key, value in wilayah_data.items():
                if key in [str(paslon['id_paslon']) for paslon in serialized_data_paslon]:
                    nomor_urut = next(paslon['nomor_urut'] for paslon in serialized_data_paslon if paslon['id_paslon'] == key)
                    modified_data[nomor_urut] = value
                else:
                    modified_data[key] = value

            final_data.append({
                "data_wilayah": serialized_data_wilayah[wilayah],
                "data_paslon": modified_data
            })



        return {
            'data': final_data,
            'data_paslon': serialized_data_paslon,
            'chart': data_table.get('chart'),
            'last_updated': data_table.get('ts'),
            'progres': data_table.get('progres'),
        }
