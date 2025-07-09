printers = [
        "Brother DCP-L2540DW",
        "HP Laserjet Pro M404dn",
        "Brother HL-L6200DW",
        "TOSHIBA e-STUDIO3018A",
        "HP LaserJet Pro 4003dn",
        "HP LaserJet M402dn",
        "Brother HL-L5210DW",
        "Brother HL-5210DW",
        "Brother ADS-4300N",
        "HP Smart Tank 750",
        "Brother MFC-J2330DW (Color)",
        "Brother HL-L5200DW",
        "Brother T820DW (Color)",
        "HP LaserJet 400 M401dn",
        "Brother HL-5200DW",
        "Brother MFC-J2330DW",
        "TOSHIBA e-STUDIO3018A"
]

#Empty list for each brand
brothers_printer = []
hp_printer = []
toshiba_printer = []

#Loop for each printer and classify by brand
for printer in printers:
    if printer.lower().startswith("brother"):
        brothers_printer.append(printer)
    elif printer.lower().startswith("hp"):
        hp_printer.append(printer)
    elif printer.lower().startswith("toshiba"):
        toshiba_printer.append(printer)

print("Brothers Printers:")
print(brothers_printer)
print("HP Printers:")
print(hp_printer)
print("Toshiba Printers:")
print(toshiba_printer)