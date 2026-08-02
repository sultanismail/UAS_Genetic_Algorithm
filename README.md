# UAS Genetic Algorithm - Penjadwalan Mata Kuliah

## Nama
M. Sultan Ismail

## NIM
24146091

## Mata Kuliah
Kecerdasan Buatan

## Deskripsi
Project ini mengimplementasikan **Algoritma Genetika (Genetic Algorithm)** untuk menyelesaikan masalah penjadwalan mata kuliah. Algoritma bekerja dengan proses seleksi, crossover, mutasi, dan elitism untuk menghasilkan jadwal dengan konflik seminimal mungkin.

## Struktur Project

```
UAS_Genetic_Algorithm/
│
├── chromosome.py
├── data.py
├── fitness.py
├── genetic_algorithm.py
├── visualization.py
├── main.py
├── README.md
├── requirements.txt
├── notebook/
│   └── UAS_Genetic_Algorithm.ipynb
├── hasil/
│   ├── grafik.png
│   ├── jadwal.csv
│   └── hasil.txt
```

## Parameter Algoritma

- Population Size : 60
- Generations : 100
- Crossover Rate : 85%
- Mutation Rate : 20%
- Elitism : 2

## Cara Menjalankan

Install library:

```bash
pip install matplotlib
```

Jalankan program:

```bash
python main.py
```

## Output

Program menghasilkan:

- Jadwal terbaik
- Nilai fitness
- Jumlah konflik
- Grafik perkembangan fitness
- File `jadwal.csv`
- File `hasil.txt`

## Penulis

M. Sultan Ismail  
NIM: 24146091