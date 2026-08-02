"""
VISUALISASI FITNESS
"""

import matplotlib.pyplot as plt


def plot_fitness(max_history, avg_history):
    """
    Menampilkan dan menyimpan grafik fitness
    """

    plt.figure(figsize=(10, 6))

    plt.plot(
        max_history,
        label="Fitness Maksimum",
        linewidth=2
    )

    plt.plot(
        avg_history,
        label="Fitness Rata-rata",
        linewidth=2
    )

    plt.title("Perkembangan Fitness - Algoritma Genetika Penjadwalan Mata Kuliah")

    plt.xlabel("Generasi")
    plt.ylabel("Fitness")

    plt.grid(True)
    plt.legend()

    # Simpan gambar
    plt.savefig("hasil/grafik.png", dpi=300)

    # Tampilkan
    plt.show()