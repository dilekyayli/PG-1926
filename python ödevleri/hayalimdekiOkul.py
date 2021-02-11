class School:
    def __init__(self, name, stype, lessons, classRooms, teachers, total):
        self.name       = name
        self.stype      = stype
        self.lessons    = lessons
        self.classRooms = classRooms
        self.teachers   = teachers
        self.total      = total
 

Schools = [
    School("Karamanoğlu Mehmet Bey", "İlkokul", "İlkokul müfredat dersleri(Türkçe, Hayat Bilgisi, Matematik vs.)", 14, 40, 500),
    School("Yunus Emre", "Ortaokul", "Ortaokul müfredat dersleri(İnkılap Tarihi ve Atatürkçülük, Matematik, İngilizce vs.) & etkinlikler", 20, 50, 400),
    School("Abdullah Tayyar", "Anadolu Lisesi", "Lise müfredat dersleri(Fizik, Kimya, Matematik vs.)", 30, 60, 800),
    School("Akdeniz", "Üniversite","Resmi ve seçmeli müfredat", 250, 350, 30500)
]

for school in Schools:
    print(
        'Okul Adı: ' + school.name +'\n',
        'Okul Türü: ' + school.stype +'\n',
        'Okutulan Dersler: ' + school.lessons +'\n',
        'Sınıf/derslik Sayısı: ' + str(school.classRooms) +'\n',
        'Öğretmen Sayısı: ' + str(school.teachers) +'\n',
        'Mevcut: ' + str(school.total)
    )