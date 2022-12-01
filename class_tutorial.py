class Kotatko:
    def zamnoukej(self):
        print(f"{self.jmeno}: Mňau!")

mourek = Kotatko()
mourek.jmeno = 'Mourek'

micka = Kotatko()
micka.jmeno = 'Micka'

mourek.zamnoukej()
micka.zamnoukej()