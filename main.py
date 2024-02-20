# This is a sample Python script.
# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#---------------------Aufgabe 1 ------------------------------------
def compute_r2d2_population(step_amount: int) -> tuple[int,int,int]:
    """
        Computes the r2d2 population for the given step amount
    :param step_amount: amount of steps to compute the population (e.g.: 5)
    :return: tuple of childs adults and old r2d2
    """
    young = 10
    adults = 10
    old = 10

    for step in range(step_amount):
        newYoung = adults * 4 + old * 2
        old = adults // 3
        adults = young // 2
        young = newYoung

    return (young,adults,old)

#---------------------Aufgabe 2 Streichholz------------------------------
#IMPLEMENT YOUR SOLUTION FOR THE STEICHHOLZSPIEL HERE


#---------------------Aufgabe 3 Heron ------------------------------------
def heron_verfahren(flaeche : float, abweichung_grenze:float) -> float:
    """
        computes the square root using the heron method
    :param flaeche: size of the area
    :param abweichung_grenze: threshold for the heron method
    :return:the square root of the given area according to the heron method
    """
    a=flaeche
    b=1.0
    abweichung_ok = True
    print(" %-20s | %-20s | %20s | %20s" % ("Länge a", "Länge b", "Mittelwert","Abweichung"))
    while(abweichung_ok):
        mittelwert = (a + b) / 2
        abweichung = abs(a-b)
        print(" %-20s | %-20s | %20s | %20s" % (a, b, mittelwert, abweichung))

        if(abweichung <= abweichung_grenze):
            abweichung_ok = False
        else:
            a = mittelwert
            b = flaeche / a
    return a


#---------------------Aufgabe 4 Quersumme------------------------------
#IMPLEMENT, IF NECESSARY, EXERCISE 4 HERE BUT USE A FUNCTION!


#---------------MANAGEMENT----------------------
#-------------COMMENT/UNCOMMENT lines to launch the different exercises
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("You need to adjust this code to run your implementation")

    # Aufgabe 1
    print(f"""
        # R2D2 Population after 5 steps is: 
        # Young: {compute_r2d2_population(5)[0]}
        # Adults: {compute_r2d2_population(5)[1]}
        # Old: {compute_r2d2_population(5)[2]}""")
    # print (compute_r2d2_population(5))

    # Aufgabe 2
    # TO BE IMPLEMENTED

    # Aufgabe 3
    print (f"Die Wurzel für die Fläche 25 und Grenze 0.01 nach Heron ist: {heron_verfahren(25, 0.01)}")

    # Aufgabe 4
    # TO BE IMPLEMENTED

    # Use a breakpoint in the code line below to debug your script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
