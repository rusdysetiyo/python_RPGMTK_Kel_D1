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
            "nama_monster": "Kapten B.Arie",
            "narasi": "samg pemimpin pasukan Termul, Kapten B.Arie muncul dengan membawa senjata andalannya, sebuah meriam yang sangat mematikan, dia menantangmu untuk melawannya jika ingin menerobos masuk ke dalam istana",
            "pertanyaan": "Berapa hasil dari (10 x 10)^2 - (50 : 5) ?",
            "pilihan": "A. 9880\nB. 9990\nC. 10000",
            "jawaban_benar": "B"
        },
        3: {
            "nama_monster": "Bahlwitch",
            "narasi": "Bahlwitch, sang penyihir kerajaan muncul dengan membawa senjata andalannya, Ethanol vial yang sangat mematikan, dia menantangmu untuk melawannya jika ingin mengadapi sang Sawit Knight",
            "pertanyaan": "berapakah hasil dari 67^3 ?",
            "pilihan": "A. 300763\nB. 29791\nC. 287496",
            "jawaban_benar": "A"
        },
        4: {
            "nama_monster": "Sawit Knight",
            "narasi": "Sang Sawit Knight muncul dengan membawa pedang yang terbuat dari batang sawit, dia menantangmu untuk melawannya jika ingin mengadapi sang Pangeran Soloman",
            "pertanyaan": "nilai apa yang memenuhi persamaan (3x)^2 + 9 = 450 ?",
            "pilihan": "A. 7\nB. 10\nC. 13",
            "jawaban_benar": "A"
        },
        5: {
            "nama_monster": "Pangeran Soloman",
            "narasi": "Sang Pangeran Nipunegoro keluar dari Temple of Soloman sembari berkata, 'Beraninya kau datang kesini dan menantangku!!. aku Sang Pangeran Solo akan membuatmu menyesal. WI WOK DE TOK NOT ANLI TOK DE TOK!! '",
            "pertanyaan": "jika sang raja memiliki 78 pekerja untuk mengelola perkebunan sawitnya, dan setiap pekerja dapat mengelola 5 hektar perkebunan,lalu terdapat 19 pekerja spesial yang dapat mengelola 9 hektar perkebunan, berapakah luas total perkebunan sawit yang dikelola oleh para pekerja tersebut?",
            "pilihan": "A. 571 hektar\nB. 582 hektar\nC. 561 hektar",
            "jawaban_benar": "C"
        }
    }

    # Mengambil data sesuai level. Kalau level sudah habis, otomatis mengembalikan None
    return stages.get(level, None)

