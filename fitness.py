"""
FITNESS FUNCTION
Menghitung nilai fitness berdasarkan jumlah konflik.
"""

def fitness(individual):
    """
    Mengembalikan:
    - fitness_score
    - jumlah konflik
    """

    conflicts = 0

    room_schedule = {}
    lecturer_schedule = {}
    lecturer_day = {}

    for gene in individual:

        room = gene["room"]
        timeslot = gene["timeslot"]
        lecturer = gene["lecturer"]

        # Mengambil nama hari (Senin, Selasa, dst.)
        day = timeslot.split("-")[0]

        # ===================================================
        # Konflik Ruang
        # Dua mata kuliah tidak boleh memakai ruang
        # yang sama pada waktu yang sama
        # ===================================================
        if (room, timeslot) in room_schedule:
            conflicts += 1
        else:
            room_schedule[(room, timeslot)] = True

        # ===================================================
        # Konflik Dosen-Waktu
        # Dosen tidak boleh mengajar
        # dua mata kuliah pada slot yang sama
        # ===================================================
        if (lecturer, timeslot) in lecturer_schedule:
            conflicts += 1
        else:
            lecturer_schedule[(lecturer, timeslot)] = True

        # ===================================================
        # Konflik Dosen-Hari
        # Sesuai soal:
        # dosen hanya boleh mengajar sekali dalam sehari
        # ===================================================
        if (lecturer, day) in lecturer_day:
            conflicts += 1
        else:
            lecturer_day[(lecturer, day)] = True

    # Rumus fitness (semakin sedikit konflik semakin besar nilainya)
    fitness_score = 100 / (1 + conflicts)

    return fitness_score, conflicts