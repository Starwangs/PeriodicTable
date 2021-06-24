import datetime
print("")
date = datetime.datetime.now()
print(date)


def mass(a, b):
    print(num, a, "mass", (b))


def mm(no):
    num = int(input("Please type the amount of your element. "))
    r = num*no
    print("mass", r)


def mc(no):
    num = int(input("Please type the amount of your element. "))
    r = num*no
    print("", r)


re = 0
while re == 0:
    lp = 1
    sm = 0
    print("Welcome to Element Mass Volume Amount Calculator Program.")
    mode = 0
    while mode != 1 and mode != 2:
        mode = int(input(
            "Type the mode of program that you want, 1 for elements data, 2 for the calculator ,3 for credit and program log "))
        if mode == 1:
            num = int(
                input(("Enter the element number for its mass or type 0 to get all data. ")))
            if num == 0:
                print(1, "H Hydrogen", 1)
                print(2, "He Helium", 2)
                print(3, "Li Lithium", 7)
                print(4, "Be Beryllium", 9)
                print(5, "B Boron", 11)
                print(6, "C Carbon", 12)
                print(7, "N Nitrogen", 14)
                print(8, "O Oxygen", 16)
                print(9, "F Fluorine", 19)
                print(10, "Ne Neon", 20)
                print(11, "Na Sodium", 23)
                print(12, "Mg Magnesium", 24)
                print(13, "Al Aluminium", 27)
                print(14, "Si Silicon", 28)
                print(15, "P Phosphorus", 31)
                print(16, "S Sulfur", 32)
                print(17, "Cl Chlorine", 35.5)
                print(18, "Ar Argon", 40)
                print(19, "K Potassium", 39)
                print(20, "Ca Calcium", 40)
                print(21, "Sc Scandium", 45)
                print(22, "Ti Titanium", 48)
                print(23, "V Vanadium", 51)
                print(24, "Cr Chromium", 52)
                print(25, "Mn Manganese", 55)
                print(26, "Fe Iron", 55.8)
                print(27, "Co Cobalt", 59)
                print(28, "Ni Nickel", 58.7)
                print(29, "Cu Copper", 63.5)
                print(30, "Zinc", 65.4)
                print(31, "Ga Gallium", 69.7)
                print(32, "Ge Germanium", 72.6)
                print(33, "As Arsenic", 75)
                print(34, "Se Selenium", 79)
                print(35, "Br Bromine", 80)
                print(36, "Kr Krypton", 84)
                print(37, "Rb Rubidium", 85.5)
                print(38, "Sr Strontium", 87.6)
                print(39, "Y Yttrium", 89)
                print(40, "Zr Zirconium", 91)
                print(41, "Zr Niobium", 93)
                print(42, "Mo Molybdenum", 96)
                print(43, "Tc Technetium", 98)
                print(44, "Ru Ruthenium", 101)
                print(45, "Rh Rhodium", 103)
                print(46, "Pd Palladium", 106.4)
                print(47, "Ag Silver", 108)
                print(48, "Cd Cadmium", 112.4)
            elif num == 1:
                mass("Hydrogen", 1)
                print("Hydrogen is the first element that appears in periodic table. In Hydrogen there are 1 proton and 1 electron. It's the most found element in universe.")
            elif num == 2:
                mass("Helium", 4)
                print("Helium is the VIIIA group element. It's noble gas.In Helium there are 2 protons, 2 electrons and 2 neutrons.Helium is used for add in balloons because it has very low density. It can be found from the oil drilling ")
            elif num == 3:
                mass("Lithium", 7)
                print("Lithium is IA group element. It can be used for mixing to the battery. Lithium has soft texture.In Lithium there are 3 protons 3 electrons and 4 neutrons.")
            elif num == 4:
                mass("Beryllium", 9)
                print("Beryllium Is IIA group element. It's called Alkaline earth metals. Beryllium is used for mixing with copper to make BeCu compound which make it stronger.In Beryllium there are 4 protons, 4 electrons and 5 neutrons.")
            elif num == 5:
                mass("Boron", 11)
                print("Boron is IIIA group element. It's one of metalloid elements. Boron can't conduct electricity in room temperature but it can in high temperature.In Boron there are 5 protons, 5 electrons and 6 neutrons.")
            elif num == 6:
                mass("Carbon", 12)
                print("Carbon is IV group element. It's non-metallic element that can be found a lot in universes. Carbon is appear in all organisms. In carbon there are 6 protons, 6 electrons and 6 neutrons.")
            elif num == 7:
                mass("Nitrogen", 14)
                print("Nitrogen is VA group element. Gas Nitrogen is assembled in the air that we use for breathing about 78%. Liquid Nitrogen has very low temperature so it's used for freezing things about the industry. In Nitrogen there are 7 protons, 7 electrons and 7 neutrons.")
            elif num == 8:
                mass("Oxygen", 16)
                print("Oxygen is VI group element. It's the one of most important element in the world. Almost all organisms use gas oxygen for breathing.Plants use it for photosynthesis. In Oxygen there are  8 protons, 8 electrons and 8 neutrons.")
            elif num == 9:
                mass("Fluorine", 19)
                print("Fluorine is VII group element. It's the lightest Halogen group element. Fluorine has the highest EN value and it's used for adding to toothpaste for making the teeth white and strong. In Fluorine there are 9 protons, 9 electrons and 10 neutrons.")
            elif num == 10:
                mass("Neon", 20)
                print("Neon is VIIIA group element. It is the ones of the noble gas. Neon is colorless and odorless. It is can be used for adding to fluorescent light to make more gleam. In Neon there are 10 protons,10 electrons and 10 neutrons.")
            elif num == 11:
                mass("Sodium", 23)
                print("Sodium is IA groupe element. It is the one alkali metal group. Pure sodium couldn't be found in nature. When sodium meet the water it will explode. Usually we found sodium in molecule form, for example NaCl. We normally call it , salt. In sodium there are 11 protons, 11 electrons and 12 neutrons.")
            elif num == 12:
                mass("Magnesium", 24)
                print("Magnesium is IIA  group element. It is the one of alkaline earth metal. Magnesium is used for mixing with aluminum to make stronger metal. It is one of the important nutrients for human. In magnesium there are 12 protons 12 electrons and 12 neutrons.")
            elif num == 13:
                mass("Aluminium", 27)
                print("Aluminum is IIIA group element. It's light, strong and can be found easily in bauxite mineral form. Aluminum is the very important elements in metallic industry. In aluminum there are 13 protons, 13 electrons and 14 neutrons.")
            elif num == 14:
                mass("Silicon", 28)
                print("Silicon is IVA group element. It is semi metallic element. It can be found in silica forms. Silica is used for glass,  cement and ceramic industry. In silicon there are 14 protons 14 electrons and 14 neutrons.")
            elif num == 15:
                mass("Phosphorus", 31)
                print("Phosphorus is VA group element. It can't be found in nature. Phosphorus can be found in every organism. It is the one of the important nutrients for plants. In phosphorus there are 15 protons, 15 electrons and 16 neutrons.")
            elif num == 16:
                mass("Sulfur", 32)
                print("Sulfur is VIA group element. It's non metal. Sulfur has no test or smell. It can be found in nature in mineral form called sulfide. It can be used for make batteries, firework and a lot of stuff .So Sulfur is important to the world economy. In Sulfur there are 16 protons 16 electrons and 16 neutrons.")
            elif num == 17:
                mass("Chlorine", 35.5)
                print("Chlorine is VIIA group element. It is the one of halogen group. Chlorine can be found in gas form. It is poisonous and has a pungent smell. Chlorine can be used for virus or bacteria. In Chlorine there are 17 protons 17 electrons and 18 neutron.")
            elif num == 18:
                mass("Argon", 40)
                print("Argon is VIIIA group element. It is the one of noble gas group. It can be used for checking radiation. In argon there are 18 protons 18 electrons and and 22 neutrons.")
            elif num == 19:
                mass("Potassium", 39)
                print("Argon is VIIIA group element. It is one of noble gas group. It can be used for checking radiation. In argon there are 18 protons 18 electrons and and 22 neutrons.")
            elif num == 20:
                mass("Calcium", 40)
                print("Calcium is IIA group element. It is important to every organism especially in  cell physioology and  Stretching of the muscles. It can be found in milk. In calcium there are 20 protons 20 electrons and 20 neutrons.")
            elif num == 21:
                mass("Scandium", 45)
                print("Scandium is IB group element. It is one of a transitions element. Scandium is white and soft. It can be found in Scandinavia countries. In scandium there are 21 protons 21 electrons and 24 neutrons.")
            elif num == 22:
                mass("Titanium", 48)
                print("Titanium is IIB group element. It is the one of a transition element. Titanium is very durable. It can be used to make things that need to be very strong such as starship or any vehicles. In titanium there are 22 protons 22 electrons and 26 neutrons.")
            elif num == 23:
                mass("Vanadium", 51)
                print("Vanadium is IIIB group element. It is the one of a transition element. Vanadium can be used for mixing with other metal to make them easier to be flatten. In vanadium there are 23 protons 23 electrons 28 neutrons.")
            elif num == 24:
                mass("Chromium", 52)
                print("Chromium is IVB group element. It is the one of a transitions element. Chromium can be used for make stainless steel and protect things from erosion. In chromium there are 24 protons 24 electrons and 28 neutrons.")
            elif num == 25:
                mass("Manganese", 55)
                print("Manganese is VB group elements. This is one of a transition element. Manganese is very important for our body. It is used for creating red cell blood and bones, synthesizing fat and cholesterol. In manganese there are 25 protons 25 electrons and 30 neutrons.")
            elif num == 26:
                mass("Iron", 56)
                print("Iron is VIB group element. It is the one of transitions elements. Iron is well known for its strength and hardness. It can be used for make vehicles, pots, and anything that needs to be strong and durable. In iron there are 26 protons 26 electrons and 30 neutrons.")
            elif num == 27:
                mass("Cobalt", 59)
                print("Cobalt is VIB group elements. It is the one of transition elements. Cobalt salt it's very important to all of mammals and it can be used for cure the cancer. In Cobalt there are 27 protons 27 electrons and 32 neutrons.")
            elif num == 28:
                mass("Nickel", 58.7)
                print("Nickel is VIIB group elements. It is the one of transition group elements. Nickel is shiny and durable so It can be used for mixing with ink and color to make  them shiny. Nickel is also used for making coins. In nickel there are 28 protons 28 electrons and 31 neutrons.")
            elif num == 29:
                mass("Copper", 63.5)
                print("")
            elif num == 30:
                mass("Zinc", 65.4)
                print("")
            elif num == 31:
                mass("Gallium", 69.7)
                print("Gallium is IIIA group element. It is the one of menal element but gallium's melting point is very low. It can be melted by room temperature. So from its low melting point. We use it to make diode in LED light. In gallium there are 31 protons 31 neutrons and 39 neutrons.")
            elif num == 32:
                mass("Germanium", 72.6)
                print("-")
            elif num == 33:
                mass("Arsenic", 75)
                print("-")
            elif num == 34:
                mass("Selenium", 79)
                print("-")
            elif num == 35:
                mass("Bromine", 80)
                print("-")
            elif num == 36:
                mass("Krypton", 84)
                print("-")
            elif num == 37:
                mass("Rubidium", 85.5)
                print("-")
            elif num == 38:
                mass("Strontium", 87.6)
                print("-")
            elif num == 39:
                mass("Yttrium", 89)
                print("-")
            elif num == 40:
                mass("Zirconium", 91)
                print("-")
            elif num == 41:
                mass("Niobium", 93)
                print("-")
            elif num == 42:
                mass("Molybdenum", 96)
                print("-")
            elif num == 43:
                mass("Technitium", 98)
                print("-")
            elif num == 44:
                mass("Ruthenium", 101)
                print("-")
            elif num == 45:
                mass("Rhodium", 103)
                print("-")
            elif num == 46:
                mass("Palladium", 106.4)
                print("-")
            elif num == 47:
                mass("Silver", 108)
                print("-")
            elif num == 47:
                mass("Cadmium", 112.4)
                print("-")
            else:
                print(
                    "We are working on adding new elments and features ,wait for us in soon.")
        elif mode == 2:
            lp = 1
            sm = 0
            cal = int(input("Please select the mode that you want to use, 1 for amount to mass, 2 for mass to amount, 3 for amount to volume, 4 for volume to amount, 5 for volume to mass, 6 for mass to volume, 7 for mols to amount, 8 for amount to mols "))
            print("The unit for amount is mol which 1 mol equals to 6.02*10^23 atoms, volume is liters and mass is grams")
            if cal == 1:
                print("Amount to mass calculator")
                no = int(
                    input(("Type the number of element you want to calculate. ")))
                if no == 1:
                    print("You are selecting Hydrogen.")
                    no = 1
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 2:
                    print("You are selecting Helium.")
                    no = 4
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 3:
                    print("You are selecting Lithium.")
                    no = 7
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 4:
                    print("You are selecting Beryllium.")
                    no = 9
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 5:
                    print("You are selecting Boron.")
                    no = 11
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 6:
                    print("You are selecting Carbon.")
                    no = 12
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 7:
                    print("You are selecting Nitrogen.")
                    no = 14
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 8:
                    print("You are selecting Oxygen.")
                    no = 16
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 9:
                    print("You are selecting Fluorine.")
                    no = 19
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 10:
                    print("You are selecting Neon.")
                    no = 20
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 11:
                    print("You are selecting Sodium.")
                    no = 23
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 12:
                    print("You are selecting Magnesium.")
                    no = 24
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 13:
                    print("You are selecting Aluminium.")
                    no = 27
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 14:
                    print("You are selecting Silicon.")
                    no = 28
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 15:
                    print("You are selecting Phosphorus.")
                    no = 31
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 16:
                    print("You are selecting Sulfur.")
                    no = 32
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 17:
                    print("You are selecting Chlorine.")
                    no = 35.5
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 18:
                    print("You are selecting Argon.")
                    no = 40
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 19:
                    print("You are selecting Potassium.")
                    no = 39
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 20:
                    print("You are selecting Calcium.")
                    no = 40
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 21:
                    print("You are selecting Scandium.")
                    no = 45
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 22:
                    print("You are selecting Titanium.")
                    no = 48
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 23:
                    print("You are selecting Vanadium.")
                    no = 51
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 24:
                    print("You are selecting Chromium.")
                    no = 52
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 25:
                    print("You are selecting Manganese.")
                    no = 55
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 26:
                    print("You are selecting Iron.")
                    no = 55.8
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 27:
                    print("You are selecting Cobalt.")
                    no = 59
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 28:
                    print("You are selecting Nickel.")
                    no = 58.7
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 29:
                    print("You are selecting Copper.")
                    no = 63.5
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 30:
                    print("You are selecting Zinc.")
                    no = 65.4
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 31:
                    print("You are selecting Gallium.")
                    no = 69.7
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 32:
                    print("You are selecting Germanium.")
                    no = 72.6
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 33:
                    print("You are selecting Arsenic.")
                    no = 75
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 34:
                    print("You are selecting Selenium.")
                    no = 79
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 35:
                    print("You are selecting Bromine.")
                    no = 80
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 36:
                    print("You are selecting Krypton.")
                    no = 84
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 37:
                    print("You are selecting Rubidium.")
                    no = 85.5
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 38:
                    print("You are selecting Strontium.")
                    no = 87.6
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 39:
                    print("You are selecting Yttrium.")
                    no = 89
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 40:
                    print("You are selecting Zirconium.")
                    no = 91
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 41:
                    print("You are selecting Niobium.")
                    no = 93
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 42:
                    print("You are selecting Molybdenum.")
                    no = 96
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 43:
                    print("You are selecting Technitium.")
                    no = 98
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 44:
                    print("You are selecting Ruthenium.")
                    no = 101
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 45:
                    print("You are selecting Rhodium.")
                    no = 103
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 46:
                    print("You are selecting Palladium.")
                    no = 106.4
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 47:
                    print("You are selecting Silver.")
                    no = 108
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 48:
                    print("You are selecting Cadmium.")
                    no = 112.4
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                else:
                    print(
                        "We are working on adding new elments and features ,wait for us in soon")
                if lp == 0:
                    print("Total mass is", sm, "grams.")
                while lp == 1:
                    no = int(
                        input(("Type the number of element you want to calculate. ")))
                    if no == 1:
                        print("You are selecting Hydrogen.")
                        no = 1
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 2:
                        print("You are selecting Helium.")
                        no = 4
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 3:
                        print("You are selecting Lithium.")
                        no = 7
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 4:
                        print("You are selecting Beryllium.")
                        no = 9
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 5:
                        print("You are selecting Boron.")
                        no = 11
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 6:
                        print("You are selecting Carbon.")
                        no = 12
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 7:
                        print("You are selecting Nitrogen.")
                        no = 14
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 8:
                        print("You are selecting Oxygen.")
                        no = 16
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 9:
                        print("You are selecting Fluorine.")
                        no = 19
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 10:
                        print("You are selecting Neon.")
                        no = 20
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 11:
                        print("You are selecting Sodium.")
                        no = 23
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 12:
                        print("You are selecting Magnesium.")
                        no = 24
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 13:
                        print("You are selecting Aluminium.")
                        no = 27
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 14:
                        print("You are selecting Silicon.")
                        no = 28
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 15:
                        print("You are selecting Phosphorus.")
                        no = 31
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 16:
                        print("You are selecting Sulfur.")
                        no = 32
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 17:
                        print("You are selecting Chlorine.")
                        no = 35.5
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 18:
                        print("You are selecting Argon.")
                        no = 40
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 19:
                        print("You are selecting Potassium.")
                        no = 39
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 20:
                        print("You are selecting Calcium.")
                        no = 40
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 21:
                        print("You are selecting Scandium.")
                        no = 45
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 22:
                        print("You are selecting Titanium.")
                        no = 48
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 23:
                        print("You are selecting Vanadium.")
                        no = 51
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 24:
                        print("You are selecting Chromium.")
                        no = 52
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 25:
                        print("You are selecting Manganese.")
                        no = 55
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 26:
                        print("You are selecting Iron.")
                        no = 55.8
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 27:
                        print("You are selecting Cobalt.")
                        no = 59
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 28:
                        print("You are selecting Nickel.")
                        no = 58.7
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 29:
                        print("You are selecting Copper.")
                        no = 63.5
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 30:
                        print("You are selecting Zinc.")
                        no = 65.4
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 31:
                        print("You are selecting Gallium.")
                        no = 69.7
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 32:
                        print("You are selecting Germanium.")
                        no = 72.6
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 33:
                        print("You are selecting Arsenic.")
                        no = 75
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 34:
                        print("You are selecting Selenium.")
                        no = 79
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 35:
                        print("You are selecting Bromine.")
                        no = 80
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 36:
                        print("You are selecting Krypton.")
                        no = 84
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 37:
                        print("You are selecting Rubidium.")
                        no = 85.5
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 38:
                        print("You are selecting Strontium.")
                        no = 87.6
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 39:
                        print("You are selecting Yttrium.")
                        no = 89
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 40:
                        print("You are selecting Zirconium.")
                        no = 91
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 41:
                        print("You are selecting Niobium.")
                        no = 93
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 42:
                        print("You are selecting Molybdenum.")
                        no = 96
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 43:
                        print("You are selecting Technitium.")
                        no = 98
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 44:
                        print("You are selecting Ruthenium.")
                        no = 101
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 45:
                        print("You are selecting Rhodium.")
                        no = 103
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 46:
                        print("You are selecting Palladium.")
                        no = 106.4
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 47:
                        print("You are selecting Silver.")
                        no = 108
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 48:
                        print("You are selecting Cadmium.")
                        no = 112.4
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    else:
                        print(
                            "We are working on adding new elments and features ,wait for us in soon")
                    if lp == 0:
                        print("Total mass is", sm, "grams.")
            elif cal == 2:
                print("Mass to amount calculator")
                no = int(
                    input(("Type the number of element you want to calculate. ")))
                if no == 1:
                    print("You are selecting Hydrogen.")
                    no = 1
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 2:
                    print("You are selecting Helium.")
                    no = 1/4
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 3:
                    print("You are selecting Lithium.")
                    no = 1/7
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 4:
                    print("You are selecting Beryllium.")
                    no = 1/9
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 5:
                    print("You are selecting Boron.")
                    no = 1/11
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 6:
                    print("You are selecting Carbon.")
                    no = 1/12
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 7:
                    print("You are selecting Nitrogen.")
                    no = 1/14
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 8:
                    print("You are selecting Oxygen.")
                    no = 1/16
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 9:
                    print("You are selecting Fluorine.")
                    no = 1/19
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 10:
                    print("You are selecting Neon.")
                    no = 1/20
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 11:
                    print("You are selecting Sodium.")
                    no = 1/23
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 12:
                    print("You are selecting Magnesium.")
                    no = 1/24
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 13:
                    print("You are selecting Aluminium.")
                    no = 1/27
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 14:
                    print("You are selecting Silicon.")
                    no = 1/28
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 15:
                    print("You are selecting Phosphorus.")
                    no = 1/31
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 16:
                    print("You are selecting Sulfur.")
                    no = 1/32
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 17:
                    print("You are selecting Chlorine.")
                    no = 1/35.5
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 18:
                    print("You are selecting Argon.")
                    no = 1/40
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 19:
                    print("You are selecting Potassium.")
                    no = 1/39
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 20:
                    print("You are selecting Calcium.")
                    no = 1/40
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 21:
                    print("You are selecting Scandium.")
                    no = 1/45
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 22:
                    print("You are selecting Titanium.")
                    no = 1/48
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 23:
                    print("You are selecting Vanadium.")
                    no = 1/51
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 24:
                    print("You are selecting Chromium.")
                    no = 1/52
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 25:
                    print("You are selecting Manganese.")
                    no = 1/55
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 26:
                    print("You are selecting Iron.")
                    no = 1/55.8
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 27:
                    print("You are selecting Cobalt.")
                    no = 1/59
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = num*no
                    sm = sm+r
                    print("Current amount is", sm, "mols.")
                    lp = float(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 28:
                    print("You are selecting Nickel.")
                    no = 58.7
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 29:
                    print("You are selecting Copper.")
                    no = 63.5
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 30:
                    print("You are selecting Zinc.")
                    no = 65.4
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 31:
                    print("You are selecting Gallium.")
                    no = 69.7
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 32:
                    print("You are selecting Germanium.")
                    no = 72.6
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 33:
                    print("You are selecting Arsenic.")
                    no = 75
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 34:
                    print("You are selecting Selenium.")
                    no = 79
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 35:
                    print("You are selecting Bromine.")
                    no = 80
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 36:
                    print("You are selecting Krypton.")
                    no = 84
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 37:
                    print("You are selecting Rubidium.")
                    no = 85.5
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 38:
                    print("You are selecting Strontium.")
                    no = 87.6
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 39:
                    print("You are selecting Yttrium.")
                    no = 89
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 40:
                    print("You are selecting Zirconium.")
                    no = 91
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 41:
                    print("You are selecting Niobium.")
                    no = 93
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 42:
                    print("You are selecting Molybdenum.")
                    no = 96
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 43:
                    print("You are selecting Technitium.")
                    no = 98
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 44:
                    print("You are selecting Ruthenium.")
                    no = 101
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 45:
                    print("You are selecting Rhodium.")
                    no = 103
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 46:
                    print("You are selecting Palladium.")
                    no = 106.4
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 47:
                    print("You are selecting Silver.")
                    no = 108
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 48:
                    print("You are selecting Cadmium.")
                    no = 112.4
                    num = float(
                        input("Please type the amount of your element in mols. "))
                    r = num*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                else:
                    print(
                        "We are working on adding new elments and features ,wait for us in soon.")
                if lp == 0:
                    print("Total amount is", sm, "mols or",
                          sm*(6.02*(10 ^ 23)), "atoms")
                while lp == 1:
                    no = int(
                        input(("Type the number of element you want to calculate. ")))
                    if no == 1:
                        print("You are selecting Hydrogen.")
                        no = 1
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 2:
                        print("You are selecting Helium.")
                        no = 1/4
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 3:
                        print("You are selecting Lithium.")
                        no = 1/7
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 4:
                        print("You are selecting Beryllium.")
                        no = 1/9
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 5:
                        print("You are selecting Boron.")
                        no = 1/11
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 6:
                        print("You are selecting Carbon.")
                        no = 1/12
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 7:
                        print("You are selecting Nitrogen.")
                        no = 1/14
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 8:
                        print("You are selecting Oxygen.")
                        no = 1/16
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 9:
                        print("You are selecting Fluorine.")
                        no = 1/19
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 10:
                        print("You are selecting Neon.")
                        no = 1/20
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 11:
                        print("You are selecting Sodium.")
                        no = 1/23
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 12:
                        print("You are selecting Magnesium.")
                        no = 1/24
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 13:
                        print("You are selecting Aluminium.")
                        no = 1/27
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 14:
                        print("You are selecting Silicon.")
                        no = 1/28
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 15:
                        print("You are selecting Phosphorus.")
                        no = 1/31
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 16:
                        print("You are selecting Sulfur.")
                        no = 1/32
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 17:
                        print("You are selecting Chlorine.")
                        no = 1/35.5
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 18:
                        print("You are selecting Argon.")
                        no = 1/40
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 19:
                        print("You are selecting Potassium.")
                        no = 1/39
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 20:
                        print("You are selecting Calcium.")
                        no = 1/40
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 21:
                        print("You are selecting Scandium.")
                        no = 1/45
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 22:
                        print("You are selecting Titanium.")
                        no = 1/48
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 23:
                        print("You are selecting Vanadium.")
                        no = 1/51
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 24:
                        print("You are selecting Chromium.")
                        no = 1/52
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 25:
                        print("You are selecting Manganese.")
                        no = 1/55
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 26:
                        print("You are selecting Iron.")
                        no = 1/55.8
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 27:
                        print("You are selecting Cobalt.")
                        no = 1/59
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 28:
                        print("You are selecting Nickel.")
                        no = 1/58.7
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = num*no
                        sm = sm+r
                        print("Current amount is", sm, "mols.")
                        lp = float(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 29:
                        print("You are selecting Copper.")
                        no = 63.5
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 30:
                        print("You are selecting Zinc.")
                        no = 65.4
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 31:
                        print("You are selecting Gallium.")
                        no = 69.7
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 32:
                        print("You are selecting Germanium.")
                        no = 72.6
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 33:
                        print("You are selecting Arsenic.")
                        no = 75
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 34:
                        print("You are selecting Selenium.")
                        no = 79
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 35:
                        print("You are selecting Bromine.")
                        no = 80
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 36:
                        print("You are selecting Krypton.")
                        no = 84
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 37:
                        print("You are selecting Rubidium.")
                        no = 85.5
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 38:
                        print("You are selecting Strontium.")
                        no = 87.6
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 39:
                        print("You are selecting Yttrium.")
                        no = 89
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 40:
                        print("You are selecting Zirconium.")
                        no = 91
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 41:
                        print("You are selecting Niobium.")
                        no = 93
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 42:
                        print("You are selecting Molybdenum.")
                        no = 96
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 43:
                        print("You are selecting Technitium.")
                        no = 98
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 44:
                        print("You are selecting Ruthenium.")
                        no = 101
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 45:
                        print("You are selecting Rhodium.")
                        no = 103
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 46:
                        print("You are selecting Palladium.")
                        no = 106.4
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 47:
                        print("You are selecting Silver.")
                        no = 108
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 48:
                        print("You are selecting Cadmium.")
                        no = 112.4
                        num = float(
                            input("Please type the amount of your element in mols. "))
                        r = num*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    else:
                        print(
                            "We are working on adding new elments and features ,wait for us in soon.")
                    if lp == 0:
                        print("Total amount is", sm, "mols. or",
                              sm*(6.02*(10 ^ 23)), "atoms")
            elif cal == 3:
                print("Volume to amount calculator")
                lp = 1
                sh = 0
                while lp == 1:
                    s = float(input(
                        ("Please fill the amount of your gas in liters, 22.4 liters equals to 1 mol of any gas at STP state. ")))
                    res = s/22.4
                    sh = res+sh
                    print("Now you have gas", sh, "mols.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                if lp == 0:
                    print("Total amount of your gas is", sh,
                          "mols or", sm*(6.02*(10 ^ 23)), "atoms")
            elif cal == 4:
                print("Amount to volume calculator")
                lp = 1
                sh = 0
                while lp == 1:
                    s = float(input(
                        ("Please fill the amount of your gas in mols, 22.4 liters equals to 1 mol of any gas at STP state. ")))
                    res = s*22.4
                    sh = res+sh
                    print("Now you have gas", sh, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                if lp == 0:
                    print("Your gas volume is", sh, "liters.")
            elif cal == 5:
                print("Volume to mass calculator")
                no = int(
                    input(("Type the number of element you want to calculate. ")))
                if no == 1:
                    print("You are selecting Hydrogen.")
                    no = 1
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 2:
                    print("You are selecting Helium.")
                    no = 4
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 3:
                    print("You are selecting Lithium.")
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 4:
                    print("You are selecting Beryllium.")
                    no = 9
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 5:
                    print("You are selecting Boron.")
                    no = 11
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 6:
                    print("You are selecting Carbon.")
                    no = 12
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 7:
                    print("You are selecting Nitrogen.")
                    no = 14
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 8:
                    print("You are selecting Oxygen.")
                    no = 16
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 9:
                    print("You are selecting Fluorine.")
                    no = 19
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 10:
                    print("You are selecting Neon.")
                    no = 20
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 11:
                    print("You are selecting Sodium.")
                    no = 23
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 12:
                    print("You are selecting Magnesium.")
                    no = 24
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 13:
                    print("You are selecting Aluminium.")
                    no = 27
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 14:
                    print("You are selecting Silicon.")
                    no = 28
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 15:
                    print("You are selecting Phosphorus.")
                    no = 31
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 16:
                    print("You are selecting Sulfur.")
                    no = 32
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 17:
                    print("You are selecting Chlorine.")
                    no = 35.5
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 18:
                    print("You are selecting Argon.")
                    no = 40
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 19:
                    print("You are selecting Potassium.")
                    no = 39
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 20:
                    print("You are selecting Calcium.")
                    no = 40
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 21:
                    print("You are selecting Scandium.")
                    no = 45
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 22:
                    print("You are selecting Titanium.")
                    no = 48
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 23:
                    print("You are selecting Vanadium.")
                    no = 51
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 24:
                    print("You are selecting Chromium.")
                    no = 52
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 25:
                    print("You are selecting Manganese.")
                    no = 55
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 26:
                    print("You are selecting Iron.")
                    no = 55.8
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 27:
                    print("You are selecting Cobalt.")
                    no = 59
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 28:
                    print("You are selecting Nickel.")
                    no = 58.7
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 29:
                    print("You are selecting Copper.")
                    no = 63.5
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 30:
                    print("You are selecting Zinc.")
                    no = 65.4
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 31:
                    print("You are selecting Gallium.")
                    no = 69.7
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 32:
                    print("You are selecting Germanium.")
                    no = 72.6
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 33:
                    print("You are selecting Arsenic.")
                    no = 75
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 34:
                    print("You are selecting Selenium.")
                    no = 79
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 35:
                    print("You are selecting Bromine.")
                    no = 80
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 36:
                    print("You are selecting Krypton.")
                    no = 84
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 37:
                    print("You are selecting Rubidium.")
                    no = 85.5
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 38:
                    print("You are selecting Strontium.")
                    no = 87.6
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 39:
                    print("You are selecting Yttrium.")
                    no = 89
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 40:
                    print("You are selecting Zirconium.")
                    no = 91
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 41:
                    print("You are selecting Niobium.")
                    no = 93
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 42:
                    print("You are selecting Molybdenum.")
                    no = 96
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 43:
                    print("You are selecting Technitium.")
                    no = 98
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 44:
                    print("You are selecting Ruthenium.")
                    no = 101
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 45:
                    print("You are selecting Rhodium.")
                    no = 103
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 46:
                    print("You are selecting Palladium.")
                    no = 106.4
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 47:
                    print("You are selecting Silver.")
                    no = 108
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 48:
                    print("You are selecting Cadmium.")
                    no = 112.4
                    num = float(
                        input("Please type the volume of your element in liters. "))
                    r = (num/22.4)*no
                    sm = sm+r
                    print("Current mass is", sm, "grams.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                else:
                    print(
                        "We are working on adding new elments and features ,wait for us in soon.")
                if lp == 0:
                    print("Total mass is", sm, "grams.")
                while lp == 1:
                    no = int(
                        input(("Type the number of element you want to calculate. ")))
                    if no == 1:
                        print("You are selecting Hydrogen.")
                        no = 1
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 2:
                        print("You are selecting Helium.")
                        no = 4
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 3:
                        print("You are selecting Lithium.")
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 4:
                        print("You are selecting Beryllium.")
                        no = 9
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 5:
                        print("You are selecting Boron.")
                        no = 11
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 6:
                        print("You are selecting Carbon.")
                        no = 12
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 7:
                        print("You are selecting Nitrogen.")
                        no = 14
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 8:
                        print("You are selecting Oxygen.")
                        no = 16
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 9:
                        print("You are selecting Fluorine.")
                        no = 19
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 10:
                        print("You are selecting Neon.")
                        no = 20
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 11:
                        print("You are selecting Sodium.")
                        no = 23
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 12:
                        print("You are selecting Magnesium.")
                        no = 24
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 13:
                        print("You are selecting Aluminium.")
                        no = 27
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 14:
                        print("You are selecting Silicon.")
                        no = 28
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 15:
                        print("You are selecting Phosphorus.")
                        no = 31
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 16:
                        print("You are selecting Sulfur.")
                        no = 32
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 17:
                        print("You are selecting Chlorine.")
                        no = 35.5
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 18:
                        print("You are selecting Argon.")
                        no = 40
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 19:
                        print("You are selecting Potassium.")
                        no = 39
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 20:
                        print("You are selecting Calcium.")
                        no = 40
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 21:
                        print("You are selecting Scandium.")
                        no = 45
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 22:
                        print("You are selecting Titanium.")
                        no = 48
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 23:
                        print("You are selecting Vanadium.")
                        no = 51
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 24:
                        print("You are selecting Chromium.")
                        no = 52
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 25:
                        print("You are selecting Manganese.")
                        no = 55
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 26:
                        print("You are selecting Iron.")
                        no = 55.8
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 27:
                        print("You are selecting Cobalt.")
                        no = 59
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 28:
                        print("You are selecting Nickel.")
                        no = 58.7
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 29:
                        print("You are selecting Copper.")
                        no = 63.5
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 30:
                        print("You are selecting Zinc.")
                        no = 65.4
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 31:
                        print("You are selecting Gallium.")
                        no = 69.7
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 32:
                        print("You are selecting Germanium.")
                        no = 72.6
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 33:
                        print("You are selecting Arsenic.")
                        no = 75
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 34:
                        print("You are selecting Selenium.")
                        no = 79
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 35:
                        print("You are selecting Bromine.")
                        no = 80
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 36:
                        print("You are selecting Krypton.")
                        no = 84
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 37:
                        print("You are selecting Rubidium.")
                        no = 85.5
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 38:
                        print("You are selecting Strontium.")
                        no = 87.6
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 39:
                        print("You are selecting Yttrium.")
                        no = 89
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 40:
                        print("You are selecting Zirconium.")
                        no = 91
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 41:
                        print("You are selecting Niobium.")
                        no = 93
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 42:
                        print("You are selecting Molybdenum.")
                        no = 96
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 43:
                        print("You are selecting Technitium.")
                        no = 98
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 44:
                        print("You are selecting Ruthenium.")
                        no = 101
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 45:
                        print("You are selecting Rhodium.")
                        no = 103
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 46:
                        print("You are selecting Palladium.")
                        no = 106.4
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 47:
                        print("You are selecting Silver.")
                        no = 108
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 48:
                        print("You are selecting Cadmium.")
                        no = 112.4
                        num = float(
                            input("Please type the volume of your element in liters. "))
                        r = (num/22.4)*no
                        sm = sm+r
                        print("Current mass is", sm, "grams.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    else:
                        print(
                            "We are working on adding new elments and features ,wait for us in soon.")
                    if lp == 0:
                        print("Total mass is", sm, "grams.")
            elif cal == 6:
                print("Mass to volume calculator")
                no = int(
                    input(("Type the number of element you want to calculate. ")))
                if no == 1:
                    print("You are selecting Hydrogen.")
                    no = 1
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 2:
                    print("You are selecting Helium.")
                    no = 4
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 3:
                    print("You are selecting Lithium.")
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 4:
                    print("You are selecting Beryllium.")
                    no = 9
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 5:
                    print("You are selecting Boron.")
                    no = 11
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 6:
                    print("You are selecting Carbon.")
                    no = 12
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 7:
                    print("You are selecting Nitrogen.")
                    no = 14
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 8:
                    print("You are selecting Oxygen.")
                    no = 16
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 9:
                    print("You are selecting Fluorine.")
                    no = 19
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 10:
                    print("You are selecting Neon.")
                    no = 20
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 11:
                    print("You are selecting Sodium.")
                    no = 23
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 12:
                    print("You are selecting Magnesium.")
                    no = 24
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 13:
                    print("You are selecting Aluminium.")
                    no = 27
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 14:
                    print("You are selecting Silicon.")
                    no = 28
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 15:
                    print("You are selecting Phosphorus.")
                    no = 31
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 16:
                    print("You are selecting Sulfur.")
                    no = 32
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 17:
                    print("You are selecting Chlorine.")
                    no = 35.5
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 18:
                    print("You are selecting Argon.")
                    no = 40
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 19:
                    print("You are selecting Potassium.")
                    no = 39
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 20:
                    print("You are selecting Calcium.")
                    no = 40
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 21:
                    print("You are selecting Scandium.")
                    no = 45
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 22:
                    print("You are selecting Titanium.")
                    no = 48
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 23:
                    print("You are selecting Vanadium.")
                    no = 51
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 24:
                    print("You are selecting Chromium.")
                    no = 52
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 25:
                    print("You are selecting Manganese.")
                    no = 55
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 26:
                    print("You are selecting Iron.")
                    no = 55.8
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 27:
                    print("You are selecting Cobalt.")
                    no = 59
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 28:
                    print("You are selecting Nickel.")
                    no = 58.7
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 29:
                    print("You are selecting Copper.")
                    no = 63.5
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 30:
                    print("You are selecting Zinc.")
                    no = 65.4
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 31:
                    print("You are selecting Gallium.")
                    no = 69.7
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 32:
                    print("You are selecting Germanium.")
                    no = 72.6
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 33:
                    print("You are selecting Arsenic.")
                    no = 75
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 34:
                    print("You are selecting Selenium.")
                    no = 79
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 35:
                    print("You are selecting Bromine.")
                    no = 80
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 36:
                    print("You are selecting Krypton.")
                    no = 84
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 37:
                    print("You are selecting Rubidium.")
                    no = 85.5
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 38:
                    print("You are selecting Strontium.")
                    no = 87.6
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 39:
                    print("You are selecting Yttrium.")
                    no = 89
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 40:
                    print("You are selecting Zirconium.")
                    no = 91
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 41:
                    print("You are selecting Niobium.")
                    no = 93
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 42:
                    print("You are selecting Molybdenum.")
                    no = 96
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 43:
                    print("You are selecting Technetium.")
                    no = 98
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 44:
                    print("You are selecting Ruthenium.")
                    no = 101
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 45:
                    print("You are selecting Rhodium.")
                    no = 103
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 46:
                    print("You are selecting Paladium.")
                    no = 106.4
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 47:
                    print("You are selecting Silver.")
                    no = 108
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                elif no == 48:
                    print("You are selecting Cadmium.")
                    no = 112.4
                    num = float(
                        input("Please type the mass of your element in grams. "))
                    r = (num*22.4)/no
                    sm = sm+r
                    print("Current volume is", sm, "liters.")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                else:
                    print(
                        "We are working on adding new elments and features ,wait for us in soon.")
                if lp == 0:
                    print("Total mass is", sm, "grams.")
                while lp == 1:
                    no = int(
                        input(("Type the number of element you want to calculate. ")))
                    if no == 1:
                        print("You are selecting Hydrogen.")
                        no = 1
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 2:
                        print("You are selecting Helium.")
                        no = 4
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 3:
                        print("You are selecting Lithium.")
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 4:
                        print("You are selecting Beryllium.")
                        no = 9
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 5:
                        print("You are selecting Boron.")
                        no = 11
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 6:
                        print("You are selecting Carbon.")
                        no = 12
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 7:
                        print("You are selecting Nitrogen.")
                        no = 14
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 8:
                        print("You are selecting Oxygen.")
                        no = 16
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 9:
                        print("You are selecting Fluorine.")
                        no = 19
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 10:
                        print("You are selecting Neon.")
                        no = 20
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 11:
                        print("You are selecting Sodium.")
                        no = 23
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 12:
                        print("You are selecting Magnesium.")
                        no = 24
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 13:
                        print("You are selecting Aluminium.")
                        no = 27
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 14:
                        print("You are selecting Silicon.")
                        no = 28
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 15:
                        print("You are selecting Phosphorus.")
                        no = 31
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 16:
                        print("You are selecting Sulfur.")
                        no = 32
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 17:
                        print("You are selecting Chlorine.")
                        no = 35.5
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 18:
                        print("You are selecting Argon.")
                        no = 40
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 19:
                        print("You are selecting Potassium.")
                        no = 39
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 20:
                        print("You are selecting Calcium.")
                        no = 40
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 21:
                        print("You are selecting Scandium.")
                        no = 45
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 22:
                        print("You are selecting Titanium.")
                        no = 48
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 23:
                        print("You are selecting Vanadium.")
                        no = 51
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 24:
                        print("You are selecting Chromium.")
                        no = 52
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 25:
                        print("You are selecting Manganese.")
                        no = 55
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 26:
                        print("You are selecting Iron.")
                        no = 55.8
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 27:
                        print("You are selecting Cobalt.")
                        no = 59
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 28:
                        print("You are selecting Nickel.")
                        no = 58.7
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 29:
                        print("You are selecting Copper.")
                        no = 63.5
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 30:
                        print("You are selecting Zinc.")
                        no = 65.4
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 31:
                        print("You are selecting Gallium.")
                        no = 69.7
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 32:
                        print("You are selecting Germanium.")
                        no = 72.6
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 33:
                        print("You are selecting Arsenic.")
                        no = 75
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 34:
                        print("You are selecting Selenium.")
                        no = 79
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 35:
                        print("You are selecting Bromine.")
                        no = 80
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 36:
                        print("You are selecting Krypton.")
                        no = 84
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 37:
                        print("You are selecting Rubidium.")
                        no = 85.5
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 38:
                        print("You are selecting Strontium.")
                        no = 87.6
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 39:
                        print("You are selecting Yttrium.")
                        no = 89
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 40:
                        print("You are selecting Zirconium.")
                        no = 91
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 41:
                        print("You are selecting Niobium.")
                        no = 93
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 42:
                        print("You are selecting Molybdenum.")
                        no = 96
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 43:
                        print("You are selecting Technetium.")
                        no = 98
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 44:
                        print("You are selecting Ruthenium.")
                        no = 101
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 45:
                        print("You are selecting Rhodium.")
                        no = 103
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 46:
                        print("You are selecting Paladium.")
                        no = 106.4
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 47:
                        print("You are selecting Silver.")
                        no = 108
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    elif no == 48:
                        print("You are selecting Cadmium.")
                        no = 112.4
                        num = float(
                            input("Please type the mass of your element in grams. "))
                        r = (num*22.4)/no
                        sm = sm+r
                        print("Current volume is", sm, "liters.")
                        lp = int(
                            input("Do you want to calculate more?, 1 for yes 0 for no "))
                    else:
                        print(
                            "We are working on adding new elments and features ,wait for us in soon.")
                    if lp == 0:
                        print("Total volume is", sm, "liters.")
            elif cal == 7:
                while lp == 1:
                    print("Mols to amount calculator")
                    ic = float(input("Please enter your amount in mols. "))
                    rs = ic*(6.02*(10**23))
                    print("You have", rs, "atoms")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                    if lp == 0:
                        print("Total atoms", rs, "atoms")
            elif cal == 8:
                while lp == 1:
                    print("Amount to mols calculator")
                    ic = float(input("Please enter your atom amount. "))
                    rs = ic/(6.02*(10**23))
                    print("You have atom", rs, "mols")
                    lp = int(
                        input("Do you want to calculate more?, 1 for yes 0 for no "))
                    if lp == 0:
                        print("Total atoms", rs, "mols")
            else:
                print(
                    "We are working on adding new elments and features ,wait for us in soon.")
        elif mode == 3:
            print("Current Version: B8")
            print("Version log")
            print("BETA")
            print("30/1/2021 Version B8 12A: We have included more elements from number 44 to 48. Some grammar errors have been corrected")
            print(
                "29/1/2021 Version B7 12: We have included more elements from number 34 to 43.")
            print("11/1/2021 Version B6 11: ANNOUNCEMENT: Our program data has lost. Good news! We have recovered the information until Version B3 form repl. We have rewriten the information about the element from number 26 to 33. ")
            print(
                "10/1/2021 Version B5 10: We have included more elements from number 31 to 33.")
            print(
                "9/1/2021 Version B4 9: We have included more elements from number 26 to 30.")
            print(
                "8/1/2021 Version B3 8: We have included more elements from number 21 to 25.")
            print(
                "7/1/2021 Version B2 7: We have included more elements form number 16 to 20'.")
            print("6/1/2021 Version B1 6: Happy New Year 2021! We've opened the 1st version of the program. We have included more elements form number 7 to 15.")
            print("Prototype")
            print("27/12/2020 Version P5 5: We've added more information about elements.")
            print("26/12/2020 Version P4 4: REVISED VERSION ,this version has added 4 more modes in the calculator which are mass to volume ,volume to mass, mols to amount and amount to mols.")
            print("We've checked grammar and edited some of the sentences also we change the word from mol to amount the mass of elements from atu to grams")
            print("These make the program more revalant and easier to use. In amount summary we have added quantity to display more than mols.")
            print("24/12/2020 Version P3 3: Gas mole calculation (Mode 2/2) and deleted old mode 2/1 because of its overlap feature with old mode 2/2, add more display output for clearer describtion")
            print("We also have redesigned the mode 2 describtion and change some instruction to be easier to use ,we are working on mode 2/2 and 2/3. Some misspelled has reedited.")
            print("23/12/2020 Version P2 2: Multiple elements calculation")
            print("22/12/2020 Version P1 1: Program structure ,mode 1-3 basic Element 1-6 calculator mode 1: single element calculation mass")
            print(
                "This program is made for TU project by Pankwan,Aussadanisaorn,Chayanon and Sorrawit.")
