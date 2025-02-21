def chatbot():
    print("Halo! Aku adalah KAMU MASA DEPAN. Aku di sini untuk mendukungmu!")
    print("Dimasa depan kamu jadi orang sukses, Di semesta lain kamu akan terpuruk. Terdengar lucukan? tapi tenang ini demi masa depanmu.")
    print("ceritakan saja, keluh kesahmu. aku akan menyemangatimu")
    print("Ketik 'keluar' untuk mengakhiri percakapan.")


    while True:
        user_input = input("Kamu: ").lower()

        if user_input == "keluar":
            print("Kamu Masa Depan: Tetap semangat ya! Aku selalu di sini jika kamu butuh dukungan. Sampai jumpa!")
            break

        elif "menyerah" in user_input or "tidak sanggup" in user_input or "asa" in user_input or "aku berhenti" in user_input or "aku berhenti mencoba" in user_input or "Aku sudah tidak sanggup lagi" in user_input or "Aku berhenti mencoba" in user_input or "Aku tak bisa melanjutkannya" in user_input or "Aku lelah berusaha" in user_input or "Aku tak tahu harus bagaimana lagi" in user_input: 
            print("Kamu Masa Depan: Jangan menyerah! Ingat, dimasa depan kamu jadi orang yang sukses!")
        elif "capek" in user_input or "lelah" in user_input or "capek banget" in user_input or "Aku lelah" in user_input or "Aku merasa letih" in user_input or "Aku sudah tidak bertenaga" in user_input or "Aku penat" in user_input or "Aku butuh istirahat" in user_input or "Aku merasa lesu" in user_input or "Aku lelah sekali" in user_input or "Aku tidak kuat lagi" in user_input:
            print("Kamu Masa Depan: Gpp. Tidur, Makan, atau main. Tapi jangan terlalu lama. Berusaha lagi!")
        elif "gagal" in user_input or "aku gagal" in user_input or "selalu saja gagal" in user_input or"aku tidak berhasil" in user_input or "usahaku sia-sia" in user_input or "aku belum bisa" in user_input or "aku tidak mencapai hasil" in user_input or "aku tidak lulus" in user_input or "aku kalah" in user_input or "aku terjatuh" in user_input or "aku belum berhasil" in user_input: 
            print("Kamu Masa Depan: Gagal bukan akhir dari segalanya. Dari kegagalan, kita belajar dan menjadi lebih baik. Kamu hebat!")        
        elif "putus" in user_input or "putus tujuan" in user_input or "putus asa" in user_input or "aku sudah berpisah" in user_input or "aku mengakhiri hubungan ini" in user_input or "aku dan dia sudah selesai" in user_input or "hubungan kami sudah berakhir" in user_input or "aku tidak bersama dia lagi" in user_input or "aku telah meninggalkannya" in user_input or "kami sudah tidak bersama" in user_input:
            print("Kamu Masa Depan: Putus bukan akhir ketahuilah. Jangan menyerah, ada hasil yang menanti didepanmu. Liat saja, Kamu hebat kok!")       
        elif "sendiri" in user_input or "selalu sendiri" in user_input or "aku merasa sendiri" in user_input or "Aku sendirian" in user_input or "Aku sebatang kara" in user_input or "Aku seorang diri" in user_input or "Hanya aku saja" in user_input or "Tak ada yang menemani" in user_input or "Aku tanpa teman" in user_input or "Aku tanpa siapa-siapa" in user_input or "Aku seorang" in user_input: 
            print("Kamu Masa Depan: Sendiri?, kamu dimasa depan selalu sendiri. Namun, kamu selalu baik terhadap orang. ketauilah kamu orang kuat!")
        elif "kosong" in user_input or "aku merasa kosong" in user_input or "kosong banget" in user_input or "Aku kosong" in user_input or "Aku merasa kosong" in user_input or "Aku kehilangan makna" in user_input or "Aku tidak merasakan apa-apa" in user_input or "Aku merasa hampa" in user_input or "Aku kehilangan arah" in user_input or "Aku tanpa tujuan" in user_input or "Aku merasa tak berarti" in user_input:
            print("Kamu Masa Depan: Apanya yang kosong? saat kamu masih kecil bukankah banyak cita-cita?. Kejar saja salah satu, mungkin dimasa depan aku akan berubah")
        elif "tak berdaya" in user_input or "aku tak berdaya" in user_input or "hidupku tak berdaya" in user_input or "aku tak berdaya" in user_input or "aku tidak sanggup" in user_input or "aku kehilangan kekuatan" in user_input or "aku merasa lemah" in user_input or "aku tidak mampu" in user_input or "aku tidak kuat" in user_input or "aku tidak punya daya" in user_input or "aku pasrah" in user_input:
            print("Kamu Masa Depan: Kan sudah kubilang kamu itu kuat, jalani saja dulu Ok ")        
        elif "tak berguna" in user_input or "aku tak berguna" in user_input or "selalu tak berguna" in user_input or "Aku tidak berarti" in user_input or "Aku merasa sia-sia" in user_input or "Aku tidak punya arti" in user_input or "Aku tidak ada gunanya" in user_input or "Aku merasa tidak berguna" in user_input or "Aku merasa hampa" in user_input or "Aku tidak ada nilainya" in user_input:
            print("Kamu Masa Depan: Haa...? ngomong apassih, kamu lo jago dalam banyak hal.")
        elif "sakit" in user_input or "sakit hati" in user_input or "sakit semuanya" in user_input or "Aku merasa terluka" in user_input or "Aku kecewa berat" in user_input or "Hatiku hancur" in user_input or "Aku merasa dikhianati" in user_input or "Aku tersinggung" in user_input or "Aku merasa tidak dihargai" in user_input or "Aku sakit sekali" in user_input:
            print("Kamu Masa Depan: Diobati saja gak selalu harus pil. Bisa melakukan hal yang kamu suka atau belajar memaafkan ")
        elif "tak berdaya" in user_input or "aku tak berdaya" in user_input or "tak berdaya sekali" in user_input or "Aku tidak kuat" in user_input or "Aku sudah tak sanggup" in user_input or "Aku tidak sanggup lagi" in user_input or "Aku tidak tahan" in user_input or "Aku merasa lemah" in user_input or "Aku tak mampu lagi" in user_input or "Aku tak berdaya" in user_input:
            print("Kamu Masa Depan: Apasih...., kamu lo kuat. Ingat kamu dimasa depan mampu mengahandel banyak hal ")
        elif "gelap" in user_input or "hatiku gelap" in user_input or "Hatiku gelap" in user_input or "Hatiku suram" in user_input or "Aku merasa kosong" in user_input or "Aku merasa hampa" in user_input or "Jiwaku kelam" in user_input or "Aku merasa gelisah" in user_input or "Hidupku terasa suram" in user_input or "Aku tidak punya harapan" in user_input:
            print("Kamu Masa Depan: Nyalakan saja lampuya? Ahahaha, bercanda. Cukup berhenti sejenak, kontrol emosi, lalu eksekusi rancanamu")
        elif "masa depan" in user_input or "masa depanku bagaimana" in user_input or "apakah masa depanku suram" in user_input or "Bagaimana nasibku nanti" in user_input or "Apa yang akan terjadi padaku" in user_input or "Bagaimana hidupku ke depan" in user_input or "Apa rencanaku selanjutnya" in user_input or "Ke mana arah hidupku" in user_input: 
            print("Kamu Masa Depan: Masa depan? masa depanmu sangat baik dan bagus Tapi, tergantung kamu sekarang. Makannya don't give up!")
        elif "beban" in user_input or "aku beban" in user_input or "akulah beban semua orang" in user_input or "aku tidak berguna" in user_input or "aku tidak diinginkan" in user_input or "aku menyusahkan" in user_input or "aku tidak berarti" in user_input or "aku hanya masalah" in user_input or "aku beban" in user_input or "aku tidak membantu" in user_input: 
            print("Kamu Masa Depan: Beban? Berat badan? diet aja. Kan kamu hebat kamu orang jago jelas kamu bukan beban apalagi ke sekitar. Ingat kamu Mcnya")
        elif "galau" in user_input or "aku galau" in user_input or "galau banget" in user_input or "galau sekali" in user_input or "aku galau" in user_input or "aku resah" in user_input or "aku gelisah" in user_input or "aku bingung" in user_input or "aku bimbang" in user_input or "aku dilema" in user_input or "aku gundah" in user_input or "aku murung" in user_input:
            print("Kamu Masa Depan: Idih...., galau kek BOCAH. Lagian dimasa depan kamu jadi orang sukses. jalanin aja dulu")
        elif "ditinggalkan" in user_input or "aku ditinggalkan" in user_input or "ditinggal mereka" in user_input or "ditinggal kekasih" in user_input or "aku ditinggalkan" in user_input or "aku sendiri" in user_input or "aku diabaikan" in user_input or "aku terlupakan" in user_input or "aku disisihkan" in user_input or "aku ditinggal" in user_input:
            print("Kamu Masa Depan: Ngapain takut? kamu memang sering ditinggal karena mereka takut akan kehebatnmu. Tapi lihat nanti akan banyak orang yang mengagumimu suatu saat")
        elif "hilang" in user_input or "aku hilang harapan" in user_input or "aku hilang tujuan" in user_input or "hilang harapan" in user_input or "hilang tujuan" in user_input or "aku hilang tujuan" in user_input or "aku tersesat" in user_input or "aku kehilangan arah" in user_input or "aku tidak tahu harus ke mana" in user_input:
            print("Kamu Masa Depan: ingat cita citamu dulu sangat banyak. harapnmu banyak masa depanmu pasti bagus, jalanin aja dulu")
        elif "aku kepikiran" in user_input or "aku tadi kepikiran" in user_input or "aku selalu kepikiran" in user_input or "aku pusing kepikiran" in user_input or "aku pusing karena kepikiran terus" in user_input or "kepikiran terus aku" in user_input or "aku selalu saja berfikir" in user_input or "berpikir terus aku hari ini" in user_input:
            print("Kamu Masa Depan: kenapa kepikiran terus, padahal kamu cukup selesaikan satu lalu baru masalah yang lain")
        elif "aku mengerti" in user_input or "aku paham" in user_input or "ok" in user_input or "aku paham" in user_input or "saya mengerti" in user_input or "aku ngerti" in user_input or "saya paham" in user_input or "aku faham" in user_input or "saya faham" in user_input or "aku memahami" in user_input:
            print("Kamu Masa Depan:Sip gitu dong, kan kamu jagoannya. jangan menyerah tetap berusaha. ok ")
        elif "terimakasih" in user_input or "terima kasih" in user_input or "makasih" in user_input or "trims" in user_input or "aku berterimakasih" in user_input or "saya bersyukur" in user_input or "terima kasih" in user_input or "saya menghargai" in user_input or "saya berterima kasih" in user_input:
            print("Kamu Masa Depan: ok aku senang bisa membantu, jangan menyerah ya")
        elif "Setiap hari aku capek" in user_input or "Hari-hari aku penat" in user_input or "Aku selalu merasa lelah" in user_input or "Aku capek setiap hari" in user_input or "Harian ku penuh dengan kelelahan" in user_input or "Aku merasa kelelahan tiap hari" in user_input or "Aku letih setiap hari" in user_input:
            print("Kamu Masa Depan: Coba makan yang bergizi, istirahat yang cukup dan jangan terlalu overthinking. Ntar kamu gak bakal capek kok...")
        elif "kata hari ini" in user_input or "motivasi hari ini" in user_input or "hari ini kata katanya" in user_input or "kata katanya hari ini" in user_input or "kata hari ini" in user_input:
            print("Kamu Masa Depan: Kamu lebih kuat dari yang kamu pikirkan. Ingat, badai pun pasti berlalu.")
        elif "kata katanya" in user_input or "kata kata" in user_input or "kata motivasi" in user_input or "kata kata motivasi" in user_input or "satu kata motivasi" in user_input or "1 kata motivasi" in user_input or "satu kata motivasi saja" in user_input or "1 kata moytivasi saja" in user_input:
            print("Kamu Masa Depan: Istirahat itu boleh, menyerah tidak. Pelan-pelan saja, kamu akan sampai di sana.")
        elif "semangatin dong" in user_input or "kasih semangat dong" in user_input or "kasih semangat aku membutuhkannya" in user_input or "kasih semangat dong" in user_input:
            print("Kamu Masa Depan: Hari buruk bukan berarti hidupmu buruk. Ini hanya sebuah bab dalam cerita panjang yang penuh harapan.")
        elif "berikan aku semangat" in user_input or "semangatin lagi" in user_input or "lagi semangatin lagi" in user_input:
            print("kamu Masa Depan: semakin sering besi bisa diasah maka besi tersebut dapat menebas apa saja didepannya")    
        elif "kata yang lucu" in user_input or "lucu" in user_input or "lawak" in user_input or "motivasi lucu" in user_input or "kata kata lucu ada" in user_input or "motivasi lucu ada" in user_input:
            print("Kamu Masa Depan: fisik bisa diperbaiki, materi bisa dicari. Tapi kalo yang jago kamu sendiri, senggol dong....")
        elif "yang lebih lucu" in user_input or "lebih lucu" in user_input or "lebih lucu lagi" in user_input:
            print("Kamu Masa Depan: Kamu mewek, putus asa, galau. Itu yang lucu, sampai aku ketawa. Padahal kalau kamu berusaha sebenarnya baik-baik saja. ahahaha....")
        
        else:
            print("Kamu Masa Depan: Aku mendengarkan. Ceritakan saja apa yang kamu rasakan. Aku di sini untuk mendukungmu.")
            
if __name__ == "__main__":
    chatbot()

