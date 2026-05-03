# 🌸 Lumine Store — Katalog Produk Django

## Identitas

- **Nama**: Khalisha Adzraini Arif
- **NIM**: 2308107010031
- **Mata Kuliah**: Praktikum PPL A

---

## Deskripsi Program

**Lumine Store** adalah website katalog produk berbasis Django dengan desain modern dan minimalis bernuansa pastel. Website ini menampilkan koleksi produk lifestyle & perawatan alami.

### Halaman yang Tersedia

| URL | Halaman | Deskripsi |
|-----|---------|-----------|
| `/` | Homepage | Halaman utama dengan hero section dan produk unggulan |
| `/produk/` | Daftar Produk | Grid semua produk (6 produk hardcoded) |
| `/produk/<id>/` | Detail Produk | Detail lengkap satu produk berdasarkan ID |
| `/kontak/` | Kontak | Informasi kontak dan form pesan |

### Fitur

- ✅ 4 halaman dengan URL berbeda
- ✅ Routing menggunakan `urls.py`
- ✅ Template HTML dengan Django Template Engine
- ✅ Data produk hardcoded (tidak menggunakan database)
- ✅ Desain responsif & modern pastel aesthetic
- ✅ Animasi smooth fade-up pada setiap halaman

---

## Cara Menjalankan

### 1. Persyaratan
- Python 3.7+
- pip

### 2. Install Django
```bash
pip install django
```

### 3. Jalankan Server
```bash
cd toko
python manage.py runserver
```

### 4. Buka Browser
```
http://127.0.0.1:8000/
```

---

## Struktur Proyek

```
toko/
├── manage.py
├── README.md
├── toko/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── produk/
    ├── views.py          ← Logika & data produk
    ├── urls.py           ← Routing URL
    └── templates/
        └── produk/
            ├── base.html           ← Template dasar (navbar, footer)
            ├── index.html          ← Homepage
            ├── daftar_produk.html  ← Daftar semua produk
            ├── detail_produk.html  ← Detail produk
            └── kontak.html         ← Halaman kontak
```

---

## Teknologi

- **Framework**: Django 4.x
- **Bahasa**: Python 3 + HTML/CSS
- **Font**: DM Serif Display + DM Sans (Google Fonts)
- **Database**: Tidak digunakan (data hardcoded di `views.py`)
