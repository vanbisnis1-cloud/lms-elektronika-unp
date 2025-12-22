import sqlite3
import hashlib

def hash_password(password):
    """Mengubah password teks biasa menjadi hash aman (SHA-256)"""
    return hashlib.sha256(str.encode(password)).hexdigest()

def create_db():
    """Membuat database dan tabel pengguna jika belum ada"""
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS userstable
                 (username TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()

def add_user(username, password):
    """Menambahkan pengguna baru ke database"""
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    hashed_pw = hash_password(password)
    try:
        c.execute('INSERT INTO userstable(username, password) VALUES (?,?)', (username, hashed_pw))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False # Username sudah ada
    finally:
        conn.close()

def login_user(username, password):
    """Memverifikasi username dan password dari database"""
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    hashed_pw = hash_password(password)
    c.execute('SELECT * FROM userstable WHERE username = ? AND password = ?', (username, hashed_pw))
    data = c.fetchall()
    conn.close()
    return data

# Inisialisasi database saat file ini dijalankan pertama kali
if __name__ == "__main__":
    create_db()
    # Menambahkan user default ivan untuk percobaan
    if add_user("ivan", "unp123"):
        print("User default 'ivan' berhasil dibuat!")
    else:
        print("User sudah tersedia.")