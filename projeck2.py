import time
import streamlit as st


st.image('https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiVnPoVvR9x9yOg62nFdET1NSD0OjxEVqjpVl90qxmqshdrHskAELPPiWlSKVZurtvhlYW1EyCUiVn8C_At7Pw1lY_3ShPSrgkcnpVIdSe6MJGP70v1t6dU5-3XIXwAIh_s0UfkU1JE8qR1Y6wSp3NlgzmRVi5Kjce8zkjnBle_a3g2D792k0fgpvCb-ZFI/s1794/g.jpg', caption=None, width=700, use_column_width="never", clamp=False, channels="RGB", output_format="auto")

st.title("----Program Penggajian PT. AIDA----")
class Karyawan:
    def __init__(self, nip):
        self.nip = nip
def format_rupiah(amount):
    angka = str(amount)
    ribuan = ''
    if len(angka) <= 3:
        return f"Rp. {angka}"
    else:
        while len(angka) > 3:
            ribuan = '.' + angka[-3:] + ribuan
            angka = angka[:-3]
        return f"Rp. {angka}{ribuan}"
    
def cari_data(nip):
    data = {
        101: {'nama': 'Rifan Fadlan Ramadlan', 'jabatan': 'General Marketing', 'alamat': 'jln. Gobras No 12', 'jenis_kelamin': 'Laki-Laki', 'ttl': 'Tasikmalaya, 20 Juni 2003', 'gaji_pokok': 25000000},
        102: {'nama': 'Ferdi Nuraripin', 'jabatan': 'Regional Sales Manager', 'alamat': 'jln Cibangun no.127', 'jenis_kelamin': 'Laki-Laki', 'ttl': 'Tasikmalaya, 08 Mei 2003', 'gaji_pokok': 18000000},
        103: {'nama': 'Megale Oktana', 'jabatan': 'Sales Manager Marketing', 'alamat': 'jln Manonjaya', 'jenis_kelamin': 'Laki-Laki', 'ttl': 'Tasikmalaya, 02 Januari 2003', 'gaji_pokok': 10000000},
        104: {'nama': 'Hari Fitriana', 'jabatan': 'Supervisor', 'alamat': 'jln Mangkubumi', 'jenis_kelamin': 'Laki-Laki', 'ttl': 'Tasikmalaya, 08 Agustus 2002', 'gaji_pokok': 3500000},
        105: {'nama': 'M. Alif Kudsian Putra', 'jabatan': 'Sales Taking Order', 'alamat': 'Nagarawanagi', 'jenis_kelamin': 'Laki-Laki', 'ttl': 'Tasikmalaya, 21 September 2003', 'gaji_pokok': 2700000},
        106: {'nama': 'Salman Faturrohman', 'jabatan': 'Helper', 'alamat': 'Jakarta', 'jenis_kelamin': 'Laki-Laki', 'ttl': 'Tasikmalaya, 29 September 2003', 'gaji_pokok': 2200000},
        107: {'nama': 'Gilang', 'jabatan': 'Driver', 'alamat': 'Pangandaran', 'jenis_kelamin': 'Laki-Laki', 'ttl': 'Tasikmalaya, 04 Desember 2002', 'gaji_pokok': 2200000},
    }

    if nip in data:
        return data[nip]
    else:
        return None
    

def main():
    tunjangan_jabatan = {
        'General Marketing': {'tunjangan_jabatan': 3000000, 'tunjangan_makan': 750000},
        'Regional Sales Manager': {'tunjangan_jabatan': 1500000, 'tunjangan_makan': 400000},
        'Sales Manager Marketing': {'tunjangan_jabatan': 700000, 'tunjangan_makan': 200000},
        'Supervisor': {'tunjangan_jabatan': 200000, 'tunjangan_makan': 100000},
        'Sales Taking Order': {'tunjangan_jabatan': 50000, 'tunjangan_makan': 0},
        'Helper': {'tunjangan_jabatan': 0, 'tunjangan_makan': 0},
        'Driver': {'tunjangan_jabatan': 0, 'tunjangan_makan': 0},
    }

    target = {
        'General Marketing': 30000,
        'Regional Sales Manager': 25000,
        'Sales Manager Marketing': 20000,
        'Supervisor': 35000,
        'Sales Taking Order': 50000,
        'Helper': 200,
        'Driver': 1000,
    }

    bonuses = {
        'General Marketing': 10000000,
        'Regional Sales Manager': 6000000,
        'Sales Manager Marketing': 4000000,
        'Supervisor': 2000000,
        'Sales Taking Order': 1500000,
        'Helper': 400000,
        'Driver': 400000,
    }
    
    data_target_per_bulan = {
        'Oktober 2023': {
            'General Marketing': 30200,
            'Regional Sales Manager': 27000,
            'Sales Manager Marketing': 20100,
            'Supervisor': 36000,
            'Sales Taking Order': 50100,
            'Helper': 180,
            'Driver': 1200,
        },
        'November 2023': {
            'General Marketing': 28000,
            'Regional Sales Manager': 24000,
            'Sales Manager Marketing': 20150,
            'Supervisor': 32000,
            'Sales Taking Order': 48000,
            'Helper': 205,
            'Driver': 950,
        },
        'Desember 2023': {
            'General Marketing': 31000,
            'Regional Sales Manager': 25500,
            'Sales Manager Marketing': 18000,
            'Supervisor': 31000,
            'Sales Taking Order': 55000,
            'Helper': 300,
            'Driver': 1350,
        },
    }

    nip_dicari = st.number_input("Masukkan NIP yang ingin Anda cari:", min_value=0, step=1)
    bulan = st.selectbox("Masukkan Bulan :", ("Oktober 2023", "November 2023", "Desember 2023"))

    if st.button("CARI"):                                       
        with st.status("Downloading data...", expanded=True) as status:
            st.write("Mencari data...")
            time.sleep(2)
            st.write("Data gaji...")
            time.sleep(1)
            st.write("Downloading data...")
            time.sleep(1)
            status.update(label="Download complete!", state="complete", expanded=True)

            hasil_pencarian = cari_data(nip_dicari)

            if hasil_pencarian:
                nama = hasil_pencarian['nama']
                jabatan = hasil_pencarian['jabatan']
                alamat = hasil_pencarian['alamat']
                jenis_kelamin = hasil_pencarian['jenis_kelamin']
                ttl = hasil_pencarian['ttl']
                gaji_pokok = hasil_pencarian['gaji_pokok']

                tunjangan = tunjangan_jabatan.get(jabatan, {'tunjangan_jabatan': 0, 'tunjangan_makan': 0})
                gaji_total = gaji_pokok + tunjangan['tunjangan_jabatan'] + tunjangan['tunjangan_makan']

                st.success(f"Data ditemukan untuk NIP {nip_dicari}")
                st.markdown(f"**Informasi Data Diri**")
                st.markdown(f"*Nama: {nama}*")
                st.markdown(f"*Jabatan: {jabatan}*")
                st.markdown(f"*Alamat: {alamat}*")
                st.markdown(f"*Jenis Kelamin : {jenis_kelamin}*")
                st.markdown(f"*Tempat dan Tanggal Lahir : {ttl}*")

                gaji_pokok_rupiah = format_rupiah(gaji_pokok)
                tunjangan_jabatan_rupiah = format_rupiah(tunjangan['tunjangan_jabatan'])
                tunjangan_makan_rupiah = format_rupiah(tunjangan['tunjangan_makan'])
                
                st.markdown("**Informasi Detail Gaji**")
                st.markdown(f"*- Gaji Pokok:  {gaji_pokok_rupiah}*")
                st.markdown(f"*- Tunjangan Jabatan: {tunjangan_jabatan_rupiah}*")
                st.markdown(f"*- Tunjangan Makan: {tunjangan_makan_rupiah}*")
                
                if bulan == "Oktober 2023" or bulan == "November 2023" or bulan == "Desember 2023":
                    if jabatan in target and data_target_per_bulan[bulan][jabatan] >= target[jabatan] :
                        bonus = bonuses[jabatan]
                        st.success(f"+Insentif BONUS! : {format_rupiah(bonus)} karena mencapai target.")
                        st.info(f"*Total Gaji pada bulan {bulan} sebesar {format_rupiah(gaji_total + bonuses.get(jabatan, 0))}*")
                    else:
                        st.warning("Maaf, Anda belum mencapai target untuk mendapatkan bonus.")
                        st.info(f"*Total Gaji pada Bulan {bulan} sebesar {format_rupiah(gaji_total)}*")
            else :
                st.warning(f"Tidak ada data yang ditemukan untuk NIP {nip_dicari}") 

if __name__ == "__main__":
    main()