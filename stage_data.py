def get_stage(level):
    # Database level
    stages = {
        1: {
            "nama_monster": "pasukan Termul",
            "narasi": "19 juta penjaga istana menghadang jalanmu.selesaikan pertanyaan untuk mengalahkan mereka!",
            "pertanyaan": "Berapakah hasil dari 9 + 11 x 11 ?",
            "pilihan": "A. 130\nB. 120\nC. 140",
            "jawaban_benar": "A"
        },
        2: {
            "nama_monster": "Troll Jembatan",
            "narasi": "Troll besar meminta bayaran berupa jawaban yang benar!",
            "pertanyaan": "Berapa hasil dari 5 + 5 x 5?",
            "pilihan": "A. 50\nB. 30\nC. 25",
            "jawaban_benar": "B"
        },
        3: {
            "nama_monster": "Bahlwitch",
            "narasi": "Bahlwitch, sang penyihir kerajaan muncul dengan membawa senjata andalannya, Ethanol vial yang sangat mematikan, dia menantangmu untuk melawannya jika ingin mengadapi sang Sawit Knight",
            "pertanyaan": "",
            "pilihan": "A. Batu\nB. Kertas\nC. Kayu",
            "jawaban_benar": "B"
        },
        4: {
            "nama_monster": "Sawit Knight",
            "narasi": "Sang Sawit Knight muncul dengan membawa pedang yang terbuat dari batang sawit, dia menantangmu untuk melawannya jika ingin mengadapi sang Pangeran Soloman",
            "pertanyaan": "",
            "pilihan": "A. Batu\nB. Kertas\nC. Kayu",
            "jawaban_benar": "B"
        },
        5: {
            "nama_monster": "Pangeran Soloman",
            "narasi": "Sang Pangeran Nipunegoro keluar dari Temple of Soloman sembari berkata, 'Beraninya kau datang kesini dan menantangku!!. aku Sang Pangeran Solo akan membuatmu menyesal. WI WOK DE TOK NOT ANLI TOK DE TOK!! '",
            "pertanyaan": "",
            "pilihan": "A. Batu\nB. Kertas\nC. Kayu",
            "jawaban_benar": "B"
        }
    }

    # Mengambil data sesuai level. Kalau level sudah habis, otomatis mengembalikan None
    return stages.get(level, None)
