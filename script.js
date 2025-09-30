function hitungUsia() {
    const inputTglLahir = document.getElementById('tanggalLahir').value;
    const hasilElement = document.getElementById('hasilUsia');

    // 1. Validasi Input
    if (inputTglLahir === "") {
        hasilElement.innerHTML = "<p>ERROR! Masukkan tanggal lahir untuk memulai.</p>";
        return;
    }

    // Konversi tanggal
    const tglLahir = new Date(inputTglLahir);
    const tglSaatIni = new Date();

    // 2. Cek Tanggal Masa Depan
    if (tglLahir > tglSaatIni) {
        hasilElement.innerHTML = "<p>Waktu tidak bisa diputar mundur! Tanggal lahir tidak valid.</p>";
        return;
    }

    // 3. Perhitungan Detail (Tahun, Bulan, Hari)
    // Menggunakan Date Object untuk perhitungan yang lebih akurat
    let tahun = tglSaatIni.getFullYear() - tglLahir.getFullYear();
    let bulan = tglSaatIni.getMonth() - tglLahir.getMonth();
    let hari = tglSaatIni.getDate() - tglLahir.getDate();
    
    // Penyesuaian bulan dan tahun
    if (hari < 0) {
        bulan--;
        // Menghitung jumlah hari di bulan sebelumnya
        const hariDiBulanSebelumnya = new Date(tglSaatIni.getFullYear(), tglSaatIni.getMonth(), 0).getDate();
        hari += hariDiBulanSebelumnya;
    }

    if (bulan < 0) {
        tahun--;
        bulan += 12;
    }

    // 4. Perhitungan Total Hari
    const selisihWaktu = tglSaatIni.getTime() - tglLahir.getTime();
    // 1 hari = 1000ms * 60s * 60min * 24h
    const totalHari = Math.floor(selisihWaktu / (1000 * 60 * 60 * 24));


    // 5. Tampilkan Hasil dengan Tema Gaming
    hasilElement.innerHTML = `
        <p class="status-title">LVL Up Complete!</p>
        <p>Anda telah bermain selama:</p>
        <div class="detail-usia">
            <span>**${tahun}** Tahun</span>
            <span>**${bulan}** Bulan</span>
            <span>**${hari}** Hari</span>
        </div>
        <p class="total-hari">Total Durasi Permainan: **${totalHari} Hari**</p>
    `;
}