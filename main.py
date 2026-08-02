from genetic_algorithm import run_genetic_algorithm
from fitness import fitness
from visualization import plot_fitness

# Jalankan Genetic Algorithm
best_individual, max_history, avg_history = run_genetic_algorithm()

# Hitung fitness terbaik
fitness_score, konflik = fitness(best_individual)

print("\n" + "=" * 60)
print("               JADWAL TERBAIK")
print("=" * 60)

for gene in best_individual:
    print(
        f"MK: {gene['course']:<12}"
        f"| Ruang: {gene['room']:<2}"
        f"| Waktu: {gene['timeslot']:<10}"
        f"| Dosen: {gene['lecturer']}"
    )

print("\n" + "=" * 60)
print("HASIL EVALUASI AKHIR")
print("=" * 60)

print(f"Fitness Terbaik : {fitness_score:.2f}")
print(f"Jumlah Konflik  : {konflik}")

# Simpan hasil ke file
with open("hasil/hasil.txt", "w", encoding="utf-8") as file:
    file.write("===== HASIL EVALUASI =====\n")
    file.write(f"Fitness : {fitness_score:.2f}\n")
    file.write(f"Konflik : {konflik}\n")

# Simpan jadwal ke CSV
import csv

with open("hasil/jadwal.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Mata Kuliah",
        "Dosen",
        "Ruang",
        "Slot Waktu"
    ])

    for gene in best_individual:
        writer.writerow([
            gene["course"],
            gene["lecturer"],
            gene["room"],
            gene["timeslot"]
        ])

# Tampilkan grafik
plot_fitness(max_history, avg_history)