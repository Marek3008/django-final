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
        ("dostupné", "Dostupné"),
        ("nedostupné", "Nedostupné"),
        ("čakajúce", "Čakajúce")
    )

    SECTIONS = (
        ("problematika voľného času", "Problematika voľného času"),
        ("matematika, fyzika", "Matematika, fyzika"),
        ("chémia, potravinárstvo", "Chémia, potravinárstvo"),
        ("biológia", "Biológia"),
        ("životné prostredie, geografia, geológia", "Životné prostredie, geografia, geológia"),
        ("zdravotníctvo a farmakológia", "Zdravotníctvo a farmakológia"),
        ("pôdohospodárstvo (poľnohospodárstvo, lesné a vodné hospodárstvo)", "Pôdohospodárstvo (poľnohospodárstvo, lesné a vodné hospodárstvo)"),
        ("cestovný ruch, hotelierstvo, gastronómia", "Cestovný ruch, hotelierstvo, gastronómia"),
        ("strojárstvo, hutníctvo, doprava", "Strojárstvo, hutníctvo, doprava"),
        ("stavebníctvo, geodézia, kartografia", "Stavebníctvo, geodézia, kartografia"),
        ("informatika", "Informatika"),
        ("elektrotechnika, hardware, mechatronika", "Elektrotechnika, hardware, mechatronika"),
        ("história, filozofia, právne vedy", "História, filozofia, právne vedy"),
        ("tvorba učebných pomôcok, didaktické technológie", "Tvorba učebných pomôcok, didaktické technológie"),
        ("ekonomika a riadenie", "Ekonomika a riadenie"),
        ("teória kultúry, umenie, umelecká, odevná tvorba", "Teória kultúry, umenie, umelecká, odevná tvorba"),
        ("pedagogika, psychológia,  sociológia", "Pedagogika, psychológia,  sociológia")
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