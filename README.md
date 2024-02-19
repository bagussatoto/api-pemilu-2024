<p align="center">
<img align="center" src="http://ForTheBadge.com/images/badges/built-with-love.svg"> <img align="center" src="http://ForTheBadge.com/images/badges/uses-html.svg"> <img align="center" src="http://ForTheBadge.com/images/badges/makes-people-smile.svg"> <img align="center" src="http://ForTheBadge.com/images/badges/built-by-developers.svg">
</p>

<!-- Garis Lurus -->
<img align="center" src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" alt="javascript" width="1000"/> 
<!-- End -->

<h1 align="center">DATA PEMILU 2024</h1>
<!-- Garis Lurus -->
<img align="center" src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" alt="javascript" width="1000"/> 
<!-- End -->

<img src="./assets/pemilu.gif" alt="Pemilu-2024" />
<!-- Garis Lurus -->
<img align="center" src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" alt="javascript" width="1000"/> 
<!-- End -->


  <b> <ul> Pemilu biasanya merupakan proses demokratis di mana warga negara memilih perwakilan mereka dalam pemerintahan. Pemilu dapat dilakukan untuk memilih presiden, anggota parlemen, gubernur, atau pejabat lainnya, tergantung pada sistem pemerintahan suatu negara.
  Jelang pemilu, seringkali terdapat persiapan yang melibatkan pendaftaran pemilih, pembentukan partai politik, kampanye politik, dan debat antar kandidat. Hari pemungutan suara adalah momen penting di mana warga memilih calon favorit mereka.
  Harap diingat bahwa rincian mengenai Pemilu 2024 sangat tergantung pada negara dan wilayah tertentu. Jika Anda mencari informasi spesifik tentang Pemilu 2024 di suatu negara atau wilayah tertentu, disarankan untuk memeriksa sumber-sumber berita terkini atau situs web resmi lembaga pemilihan setempat. </ul> </b>

<!-- Garis Lurus -->
<img align="center" src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" alt="javascript" width="1000"/> 
<!-- End -->

## API Reference

#### Get all api items

```http
  GET https://api-pemilu-2024.vercel.app/api
```
Response 
```json
{
  "endpoints": [
    "/api/data-paslon",
    "/api/data-wilayah",
    "/api/data-table"
  ],
  "message": "Welcome to API endpoint"
}
```
#### Get data-paslon

```http
  GET https://api-pemilu-2024.vercel.app/api/data-paslon
```
Response
```json
{
  "100025": {
    "nama": "H. ANIES RASYID BASWEDAN, Ph.D. - Dr. (H.C.) H. A. MUHAIMIN ISKANDAR",
    "nomor_urut": 1,
    "ts": "2024-02-14 18:44:00",
    "warna": "#8CB9BD"
  },
  "100026": {
    "nama": "H. PRABOWO SUBIANTO - GIBRAN RAKABUMING RAKA",
    "nomor_urut": 2,
    "ts": "2024-02-14 18:44:00",
    "warna": "#C7B7A3"
  },
  "100027": {
    "nama": "H. GANJAR PRANOWO, S.H., M.I.P. - Prof. Dr. H. M. MAHFUD MD",
    "nomor_urut": 3,
    "ts": "2024-02-14 18:44:00",
    "warna": "#B67352"
  }
}
```
<!-- Garis Lurus -->
<img align="center" src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" alt="javascript" width="1000"/> 
<!-- End -->


#### Get data-wilayah

```http
  GET  https://api-pemilu-2024.vercel.app/api/data-wilayah
```
Response
```json
[
  {
    "id": 100054,
    "kode": "11",
    "nama": "ACEH",
    "tingkat": 1
  },
  {
    "id": 191103,
    "kode": "51",
    "nama": "BALI",
    "tingkat": 1
  },
  {
    "id": 191100,
    "kode": "36",
    "nama": "BANTEN",
    "tingkat": 1
  },
  {
    "id": 191092,
    "kode": "17",
    "nama": "BENGKULU",
    "tingkat": 1
  },
  {
    "id": 191098,
    "kode": "34",
    "nama": "DAERAH ISTIMEWA YOGYAKARTA",
    "tingkat": 1
  },
  {
    "id": 191095,
    "kode": "31",
    "nama": "DKI JAKARTA",
    "tingkat": 1
  },
  {
    "id": 191053,
    "kode": "75",
    "nama": "GORONTALO",
    "tingkat": 1
  },
  {
    "id": 191089,
    "kode": "15",
    "nama": "JAMBI",
    "tingkat": 1
  },
  {
    "id": 191096,
    "kode": "32",
    "nama": "JAWA BARAT",
    "tingkat": 1
  },
  {
    "id": 191097,
    "kode": "33",
    "nama": "JAWA TENGAH",
    "tingkat": 1
  },
  {
    "id": 191099,
    "kode": "35",
    "nama": "JAWA TIMUR",
    "tingkat": 1
  },
  {
    "id": 191101,
    "kode": "61",
    "nama": "KALIMANTAN BARAT",
    "tingkat": 1
  },
  {
    "id": 191106,
    "kode": "63",
    "nama": "KALIMANTAN SELATAN",
    "tingkat": 1
  },
  {
    "id": 191102,
    "kode": "62",
    "nama": "KALIMANTAN TENGAH",
    "tingkat": 1
  },
  {
    "id": 191107,
    "kode": "64",
    "nama": "KALIMANTAN TIMUR",
    "tingkat": 1
  },
  {
    "id": 191108,
    "kode": "65",
    "nama": "KALIMANTAN UTARA",
    "tingkat": 1
  },
  {
    "id": 191094,
    "kode": "19",
    "nama": "KEPULAUAN BANGKA BELITUNG",
    "tingkat": 1
  },
  {
    "id": 191091,
    "kode": "21",
    "nama": "KEPULAUAN RIAU",
    "tingkat": 1
  },
  {
    "id": 191093,
    "kode": "18",
    "nama": "LAMPUNG",
    "tingkat": 1
  },
  {
    "id": 200001,
    "kode": "99",
    "nama": "Luar Negeri",
    "tingkat": 1
  },
  {
    "id": 191115,
    "kode": "81",
    "nama": "MALUKU",
    "tingkat": 1
  },
  {
    "id": 191116,
    "kode": "82",
    "nama": "MALUKU UTARA",
    "tingkat": 1
  },
  {
    "id": 191104,
    "kode": "52",
    "nama": "NUSA TENGGARA BARAT",
    "tingkat": 1
  },
  {
    "id": 191105,
    "kode": "53",
    "nama": "NUSA TENGGARA TIMUR",
    "tingkat": 1
  },
  {
    "id": 191117,
    "kode": "91",
    "nama": "P A P U A",
    "tingkat": 1
  },
  {
    "id": 191118,
    "kode": "92",
    "nama": "PAPUA BARAT",
    "tingkat": 1
  },
  {
    "id": 191121,
    "kode": "96",
    "nama": "PAPUA BARAT DAYA",
    "tingkat": 1
  },
  {
    "id": 191120,
    "kode": "95",
    "nama": "PAPUA PEGUNUNGAN",
    "tingkat": 1
  },
  {
    "id": 191114,
    "kode": "93",
    "nama": "PAPUA SELATAN",
    "tingkat": 1
  },
  {
    "id": 191119,
    "kode": "94",
    "nama": "PAPUA TENGAH",
    "tingkat": 1
  },
  {
    "id": 191088,
    "kode": "14",
    "nama": "RIAU",
    "tingkat": 1
  },
  {
    "id": 191113,
    "kode": "76",
    "nama": "SULAWESI BARAT",
    "tingkat": 1
  },
  {
    "id": 191111,
    "kode": "73",
    "nama": "SULAWESI SELATAN",
    "tingkat": 1
  },
  {
    "id": 191110,
    "kode": "72",
    "nama": "SULAWESI TENGAH",
    "tingkat": 1
  },
  {
    "id": 191112,
    "kode": "74",
    "nama": "SULAWESI TENGGARA",
    "tingkat": 1
  },
  {
    "id": 191109,
    "kode": "71",
    "nama": "SULAWESI UTARA",
    "tingkat": 1
  },
  {
    "id": 191087,
    "kode": "13",
    "nama": "SUMATERA BARAT",
    "tingkat": 1
  },
  {
    "id": 191090,
    "kode": "16",
    "nama": "SUMATERA SELATAN",
    "tingkat": 1
  },
  {
    "id": 191086,
    "kode": "12",
    "nama": "SUMATERA UTARA",
    "tingkat": 1
  }
]
```
<!-- Garis Lurus -->
<img align="center" src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" alt="javascript" width="1000"/> 
<!-- End -->


#### Get data-table

```http
  GET https://api-real-count-2024.vercel.app/api/data-table
```
Response
```json
{
  "chart": {
    "100025": 5459425,
    "100026": 12476925,
    "100027": 4300835,
    "persen": 41.01
  },
  "progres": {
    "progres": 337602,
    "total": 823236
  },
  "psu": "Reguler",
  "table": {
    "11": {
      "100025": 232838,
      "100026": 66265,
      "100027": 10456,
      "persen": 37.87,
      "psu": "Reguler",
      "status_progress": true
    },
    "12": {
      "100025": 229334,
      "100026": 442551,
      "100027": 101586,
      "persen": 36.45,
      "psu": "Reguler",
      "status_progress": true
    },
    "13": {
      "100025": 216728,
      "100026": 139532,
      "100027": 16657,
      "persen": 42.31,
      "psu": "Reguler",
      "status_progress": true
    },
    "14": {
      "100025": 127283,
      "100026": 165361,
      "100027": 39114,
      "persen": 27.39,
      "psu": "Reguler",
      "status_progress": true
    },
    "15": {
      "100025": 59532,
      "100026": 150101,
      "100027": 28007,
      "persen": 35.9,
      "psu": "Reguler",
      "status_progress": true
    },
    "16": {
      "100025": 114863,
      "100026": 360203,
      "100027": 67790,
      "persen": 38.09,
      "psu": "Reguler",
      "status_progress": true
    },
    "17": {
      "100025": 36400,
      "100026": 131108,
      "100027": 21806,
      "persen": 33.62,
      "psu": "Reguler",
      "status_progress": true
    },
    "18": {
      "100025": 133277,
      "100026": 517135,
      "100027": 113725,
      "persen": 45.32,
      "psu": "Reguler",
      "status_progress": true
    },
    "19": {
      "100025": 36188,
      "100026": 94765,
      "100027": 27338,
      "persen": 46.33,
      "psu": "Reguler",
      "status_progress": true
    },
    "21": {
      "100025": 43119,
      "100026": 70964,
      "100027": 14945,
      "persen": 31.69,
      "psu": "Reguler",
      "status_progress": true
    },
    "31": {
      "100025": 388801,
      "100026": 417759,
      "100027": 193059,
      "persen": 50.36,
      "psu": "Reguler",
      "status_progress": true
    },
    "32": {
      "100025": 1311770,
      "100026": 2355799,
      "100027": 455761,
      "persen": 43.85,
      "psu": "Reguler",
      "status_progress": true
    },
    "33": {
      "100025": 655014,
      "100026": 2648342,
      "100027": 1726124,
      "persen": 55.12,
      "psu": "Reguler",
      "status_progress": true
    },
    "34": {
      "100025": 73999,
      "100026": 163531,
      "100027": 102460,
      "persen": 41.4,
      "psu": "Reguler",
      "status_progress": true
    },
    "35": {
      "100025": 503222,
      "100026": 2061285,
      "100027": 582423,
      "persen": 42.15,
      "psu": "Reguler",
      "status_progress": true
    },
    "36": {
      "100025": 351337,
      "100026": 545660,
      "100027": 113784,
      "persen": 49.77,
      "psu": "Reguler",
      "status_progress": true
    },
    "51": {
      "100025": 14171,
      "100026": 186142,
      "100027": 157320,
      "persen": 35.38,
      "psu": "Reguler",
      "status_progress": true
    },
    "52": {
      "100025": 80317,
      "100026": 207734,
      "100027": 34082,
      "persen": 36.46,
      "psu": "Reguler",
      "status_progress": true
    },
    "53": {
      "100025": 14454,
      "100026": 82997,
      "100027": 45051,
      "persen": 22.98,
      "psu": "Reguler",
      "status_progress": true
    },
    "61": {
      "100025": 106139,
      "100026": 186546,
      "100027": 54687,
      "persen": 32.63,
      "psu": "Reguler",
      "status_progress": true
    },
    "62": {
      "100025": 22357,
      "100026": 76251,
      "100027": 16319,
      "persen": 27.78,
      "psu": "Reguler",
      "status_progress": true
    },
    "63": {
      "100025": 104612,
      "100026": 153358,
      "100027": 22738,
      "persen": 34.05,
      "psu": "Reguler",
      "status_progress": true
    },
    "64": {
      "100025": 65946,
      "100026": 208537,
      "100027": 35281,
      "persen": 36.7,
      "psu": "Reguler",
      "status_progress": true
    },
    "65": {
      "100025": 5436,
      "100026": 14251,
      "100027": 4397,
      "persen": 19.22,
      "psu": "Reguler",
      "status_progress": true
    },
    "71": {
      "100025": 21627,
      "100026": 199998,
      "100027": 45397,
      "persen": 50.57,
      "psu": "Reguler",
      "status_progress": true
    },
    "72": {
      "100025": 20941,
      "100026": 50767,
      "100027": 8500,
      "persen": 16.44,
      "psu": "Reguler",
      "status_progress": true
    },
    "73": {
      "100025": 262300,
      "100026": 374499,
      "100027": 38090,
      "persen": 39.59,
      "psu": "Reguler",
      "status_progress": true
    },
    "74": {
      "100025": 32956,
      "100026": 91872,
      "100027": 8710,
      "persen": 31.91,
      "psu": "Reguler",
      "status_progress": true
    },
    "75": {
      "100025": 14261,
      "100026": 33487,
      "100027": 3031,
      "persen": 30.4,
      "psu": "Reguler",
      "status_progress": true
    },
    "76": {
      "100025": 15843,
      "100026": 39065,
      "100027": 5963,
      "persen": 29.25,
      "psu": "Reguler",
      "status_progress": true
    },
    "81": {
      "100025": 6339,
      "100026": 33680,
      "100027": 9580,
      "persen": 23.3,
      "psu": "Reguler",
      "status_progress": true
    },
    "82": {
      "100025": 13366,
      "100026": 27407,
      "100027": 4787,
      "persen": 14.1,
      "psu": "Reguler",
      "status_progress": true
    },
    "91": {
      "100025": 1195,
      "100026": 8758,
      "100027": 2693,
      "persen": 13.12,
      "psu": "Reguler",
      "status_progress": true
    },
    "92": {
      "100025": 855,
      "100026": 4524,
      "100027": 1723,
      "persen": 10.97,
      "psu": "Reguler",
      "status_progress": true
    },
    "93": {
      "100025": 1801,
      "100026": 8458,
      "100027": 1343,
      "persen": 11.24,
      "psu": "Reguler",
      "status_progress": true
    },
    "94": {
      "100025": 1240,
      "100026": 2362,
      "100027": 817,
      "persen": 1.76,
      "psu": "Reguler",
      "status_progress": true
    },
    "95": {
      "persen": 0,
      "psu": "Reguler",
      "status_progress": false
    },
    "96": {
      "100025": 2831,
      "100026": 9785,
      "100027": 3569,
      "persen": 19.06,
      "psu": "Reguler",
      "status_progress": true
    },
    "99": {
      "100025": 136733,
      "100026": 146086,
      "100027": 181722,
      "persen": 22.63,
      "psu": "Reguler",
      "status_progress": true
    }
  },
  "ts": "2024-02-15 09:00:20"
}
```

<!-- Garis Lurus -->
<img align="center" src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" alt="javascript" width="1000"/> 
<!-- End -->

Generated by [Bagus Budi Satoto](https://github.com/bagussatoto/)
