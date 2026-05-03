from django.shortcuts import render
from django.http import Http404

PRODUK_LIST = [
    {
        'id': 1,
        'nama': 'Lilin Aroma Vanilla Rose',
        'kategori': 'Aromaterapi',
        'tag': 'Bestseller',
        'emoji': '🕯️',
        'gambar': 'produk/img/lilin.jpg',
        'warna': 'linear-gradient(135deg, #F2C4C4 0%, #EABABA 100%)',
        'harga': 'Rp 85.000',
        'deskripsi_singkat': 'Lilin aromaterapi dengan perpaduan vanilla hangat dan rose yang menenangkan jiwa.',
        'deskripsi': 'Ciptakan suasana yang hangat dan romantis di rumahmu dengan Lilin Aroma Vanilla Rose dari Lumine. Terbuat dari bahan lilin kedelai (soy wax) premium yang dipadukan dengan minyak esensial vanilla dan mawar asli. Didesain untuk tahan lama hingga 45 jam.',
        'fitur': [
            {'icon': '🌿', 'teks': 'Soy Wax Premium'},
            {'icon': '⏱️', 'teks': 'Tahan 45 Jam'},
            {'icon': '🌸', 'teks': 'Minyak Esensial Asli'},
            {'icon': '♻️', 'teks': 'Ramah Lingkungan'},
        ],
        'reviews': [
            {'teks': 'Wanginya lembut banget, bikin kamar jadi zen. Beli lagi deh!', 'nama': 'Aulia R.'},
            {'teks': 'Packaging cantik, perfect buat kado. Langsung ketagihan sama wanginya!', 'nama': 'Sinta D.'},
            {'teks': 'Beneran tahan lama, sudah 3 minggu masih nyala. Kualitas juara!', 'nama': 'Mega P.'},
        ],
    },
    {
        'id': 2,
        'nama': 'Sabun Susu Lavender',
        'kategori': 'Perawatan Kulit',
        'tag': 'Natural',
        'emoji': '🧼',
        'gambar': 'produk/img/sabun.jpg',
        'warna': 'linear-gradient(135deg, #D4C4F2 0%, #C4BADF 100%)',
        'harga': 'Rp 45.000',
        'deskripsi_singkat': 'Sabun handmade dari susu kambing asli dengan aroma lavender yang menenangkan.',
        'deskripsi': 'Sabun Susu Lavender Lumine diformulasikan khusus untuk melembutkan dan menutrisi kulitmu secara alami. Menggunakan susu kambing asli yang kaya akan vitamin dan mineral, dipadukan dengan minyak esensial lavender pilihan. Cocok untuk semua jenis kulit, termasuk kulit sensitif.',
        'fitur': [
            {'icon': '🐐', 'teks': 'Susu Kambing Asli'},
            {'icon': '🌿', 'teks': 'Bebas SLS & Paraben'},
            {'icon': '✋', 'teks': 'Cocok Kulit Sensitif'},
            {'icon': '🧴', 'teks': 'Melembapkan Alami'},
        ],
        'reviews': [
            {'teks': 'Kulit jadi lembut dan halus setelah pakai ini. Rekomended banget!', 'nama': 'Dinda K.'},
            {'teks': 'Wangi lavender-nya enak, nggak overwhelming. Packaging pun estetik!', 'nama': 'Ratna S.'},
            {'teks': 'Endorse ke temen-temen deh, beneran bagus untuk kulit kering saya.', 'nama': 'Yuli A.'},
        ],
    },
    {
        'id': 3,
        'nama': 'Diffuser Bambu Minimalis',
        'kategori': 'Dekorasi',
        'tag': 'New',
        'emoji': '🎋',
        'gambar': 'produk/img/diffuser.jpg',
        'warna': 'linear-gradient(135deg, #C4D4C4 0%, #B4C8B4 100%)',
        'harga': 'Rp 120.000',
        'deskripsi_singkat': 'Reed diffuser dengan rangka bambu alami. Mengharumkan ruangan hingga 30 hari.',
        'deskripsi': 'Hadirkan ketenangan alam ke dalam rumahmu dengan Diffuser Bambu Minimalis dari Lumine. Dibuat dari bambu yang dipanen secara berkelanjutan, dilengkapi dengan campuran minyak wewangian eksklusif.',
        'fitur': [
            {'icon': '🎋', 'teks': 'Bambu Berkelanjutan'},
            {'icon': '📅', 'teks': 'Tahan 30 Hari'},
            {'icon': '🏠', 'teks': 'Dekorasi Estetik'},
            {'icon': '🌬️', 'teks': '8 Batang Reed'},
        ],
        'reviews': [
            {'teks': 'Cantik banget di atas meja kerja. Wanginya subtle dan bikin fokus!', 'nama': 'Risa M.'},
            {'teks': 'Desainnya minimalis tapi elegan. Sesuai dengan estetika kamarku.', 'nama': 'Nadia P.'},
            {'teks': 'Sudah sebulan masih wangi. Worth it banget harganya!', 'nama': 'Clara H.'},
        ],
    },
    {
        'id': 4,
        'nama': 'Bath Salt Eucalyptus Mint',
        'kategori': 'Perawatan Diri',
        'tag': 'Relax',
        'emoji': '🛁',
        'gambar': 'produk/img/bath_salt.jpg',
        'warna': 'linear-gradient(135deg, #C4DCF2 0%, #B4CDE2 100%)',
        'harga': 'Rp 65.000',
        'deskripsi_singkat': 'Garam mandi premium dengan eucalyptus dan mint untuk relaksasi total setelah hari yang panjang.',
        'deskripsi': 'Manjakan dirimu dengan Bath Salt Eucalyptus Mint Lumine setelah hari yang melelahkan. Formula campuran Dead Sea Salt, Himalayan Pink Salt, dan minyak eucalyptus + mint membantu merelaksasi otot tegang.',
        'fitur': [
            {'icon': '🌊', 'teks': 'Dead Sea & Himalayan Salt'},
            {'icon': '💆', 'teks': 'Merelaksasi Otot'},
            {'icon': '🫧', 'teks': 'Membersihkan Pori'},
            {'icon': '❄️', 'teks': 'Sensasi Segar'},
        ],
        'reviews': [
            {'teks': 'Setelah rendam 20 menit, badan jadi ringan banget! Like spa at home.', 'nama': 'Feli T.'},
            {'teks': 'Wanginya fresh dan menyegarkan. Cocok banget habis olahraga!', 'nama': 'Intan W.'},
            {'teks': 'Favorit baru saya! Kulit jadi lebih halus dan nggak kering.', 'nama': 'Putri N.'},
        ],
    },
    {
        'id': 5,
        'nama': 'Hand Cream Rose Hip',
        'kategori': 'Perawatan Kulit',
        'tag': 'Organic',
        'emoji': '🌹',
        'gambar': 'produk/img/hand_cream.jpg',
        'warna': 'linear-gradient(135deg, #F2D4C4 0%, #E8C4B0 100%)',
        'harga': 'Rp 55.000',
        'deskripsi_singkat': 'Krim tangan ringan dari rosehip oil dan shea butter untuk tangan lembut sepanjang hari.',
        'deskripsi': 'Hand Cream Rose Hip Lumine diformulasikan dengan rosehip oil murni kaya vitamin C dan antioksidan, dipadu dengan shea butter organik yang melembapkan. Teksturnya ringan, cepat meresap, dan tidak lengket.',
        'fitur': [
            {'icon': '🌹', 'teks': 'Rosehip Oil Murni'},
            {'icon': '🧈', 'teks': 'Shea Butter Organik'},
            {'icon': '⚡', 'teks': 'Cepat Meresap'},
            {'icon': '💧', 'teks': 'Non-Greasy Formula'},
        ],
        'reviews': [
            {'teks': 'Tangan jadi halus banget! Nggak lengket dan cepat meresap.', 'nama': 'Lena S.'},
            {'teks': 'Akhirnya ketemu hand cream yang cocok buat kulit tanganku yang kering.', 'nama': 'Vina R.'},
            {'teks': 'Wangi rose-nya subtle dan enak. Packaging-nya pun menggemaskan!', 'nama': 'Mira K.'},
        ],
    },
    {
        'id': 6,
        'nama': 'Buket Kering Pampas',
        'kategori': 'Dekorasi',
        'tag': 'Trending',
        'emoji': '🌾',
        'gambar': 'produk/img/buket_kering.jpg',
        'warna': 'linear-gradient(135deg, #F5EDD5 0%, #EAD9B8 100%)',
        'harga': 'Rp 150.000',
        'deskripsi_singkat': 'Buket bunga kering pampas grass yang elegan untuk mempercantik interior rumahmu.',
        'deskripsi': 'Lumine Pampas Dry Bouquet menghadirkan keindahan alam yang abadi ke dalam rumahmu. Setiap buket dikurasi dengan hati-hati dari pampas grass pilihan dengan warna alami yang elegan.',
        'fitur': [
            {'icon': '🌾', 'teks': 'Pampas Grass Pilihan'},
            {'icon': '♾️', 'teks': 'Tahan Bertahun-Tahun'},
            {'icon': '🎨', 'teks': 'Warna Natural Elegan'},
            {'icon': '🏡', 'teks': 'Tanpa Perawatan Khusus'},
        ],
        'reviews': [
            {'teks': 'Cantik banget! Bikin sudut ruang tamu jadi jauh lebih estetik.', 'nama': 'Dara F.'},
            {'teks': 'Kualitasnya premium, pampas grass-nya besar dan penuh. Worth it!', 'nama': 'Rani O.'},
            {'teks': 'Sudah 6 bulan masih cantik. Nggak perlu disiram, perfect!', 'nama': 'Tia G.'},
        ],
    },
]


def index(request):
    context = {'produk_list': PRODUK_LIST[:3]}
    return render(request, 'produk/index.html', context)

def daftar_produk(request):
    context = {'produk_list': PRODUK_LIST}
    return render(request, 'produk/daftar_produk.html', context)

def detail_produk(request, id):
    produk = next((p for p in PRODUK_LIST if p['id'] == id), None)
    if produk is None:
        raise Http404("Produk tidak ditemukan")
    return render(request, 'produk/detail_produk.html', {'produk': produk})

def kontak(request):
    return render(request, 'produk/kontak.html')
