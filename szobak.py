from szoba import Szoba


class EgyagyasSzoba(Szoba):
    def get_tipus(self):
        return "Egyágyas"


class KetagyasSzoba(Szoba):
    def get_tipus(self):
        return "Kétágyas"
