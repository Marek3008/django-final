from django.db import models



class Class(models.Model):

    name = models.CharField(max_length=6)


class Student(models.Model):

    className = models.ForeignKey(Class, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Teacher(models.Model):

    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Theme(models.Model):

    STATES = (
        ("Dostupné", "Dostupné"),
        ("Nedostupné", "Nedostupné"),
        ("Čakajúce", "Čakajúce")
    )

    SECTIONS = (
        ("Problematika voľného času", "Problematika voľného času"),
        ("Matematika, fyzika", "Matematika, fyzika"),
        ("Chémia, potravinárstvo", "Chémia, potravinárstvo"),
        ("Biológia", "Biológia"),
        ("Životné prostredie, geografia, geológia", "Životné prostredie, geografia, geológia"),
        ("Zdravotníctvo a farmakológia", "Zdravotníctvo a farmakológia"),
        ("Pôdohospodárstvo (poľnohospodárstvo, lesné a vodné hospodárstvo)", "Pôdohospodárstvo (poľnohospodárstvo, lesné a vodné hospodárstvo)"),
        ("Cestovný ruch, hotelierstvo, gastronómia", "Cestovný ruch, hotelierstvo, gastronómia"),
        ("Strojárstvo, hutníctvo, doprava", "Strojárstvo, hutníctvo, doprava"),
        ("Stavebníctvo, geodézia, kartografia", "Stavebníctvo, geodézia, kartografia"),
        ("Informatika", "Informatika"),
        ("Elektrotechnika, hardware, mechatronika", "Elektrotechnika, hardware, mechatronika"),
        ("História, filozofia, právne vedy", "História, filozofia, právne vedy"),
        ("Tvorba učebných pomôcok, didaktické technológie", "Tvorba učebných pomôcok, didaktické technológie"),
        ("Ekonomika a riadenie", "Ekonomika a riadenie"),
        ("Teória kultúry, umenie, umelecká, odevná tvorba", "Teória kultúry, umenie, umelecká, odevná tvorba"),
        ("Pedagogika, psychológia,  sociológia", "Pedagogika, psychológia,  sociológia")
    )

    consultant = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=40)
    description = models.TextField()
    section = models.CharField(max_length=64, choices=SECTIONS)
    state = models.CharField(max_length=11, choices=STATES)
    consNum = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"