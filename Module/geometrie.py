import math

def surfaceCercle () :
    r = float(input('Entrer le rayon du Cercle pour avoir sa surface :'))
    area = math.pi * r * r
    print("la surface du Cercle est : %.2f" %area)
    return;
   
def perimetreCercle () :
    r = float(input('Entrer la rayon du Cercle pour avoir son perimetre :'))
    resultat = 2 * math.pi * r
    print("la surface du Cercle est : ", resultat, "cm")
    return;
    
def surfaceCarre () :
    r = float(input('Entrer la longueur du Carre pour avoir sa surface :'))
    area = r * r
    print("la surface du Carre est : ", area, "cm²")
    return;

def perimetreCarre () :
    r = float(input('Entrer la longueur du Carre pour avoir son perimetre :'))
    perimetre = r * 4
    print("la surface du Carre est : ", perimetre, "cm")
    return;
    
def surfaceRectangle () :
    r = float(input('Entrer la longueur du Rectangle pour avoir sa surface :'))
    r2 = float(input('Entrer la largeur du Rectangle pour avoir sa surface :'))
    area = r + r2
    print("la surface du Rectangle est : ", area, "cm²")
    return;

def perimetreRectangle () :
    r = float(input('Entrer la longueur du Rectangle pour avoir son perimetre :'))
    r2 = float(input('Entrer la largeur du Rectangle pour avoir son perimetre :'))
    perimetre = (r + r2)*2
    print("la surface du Rectangle est : ", perimetre, "cm")
    return;

perimetreRectangle ()
perimetreCarre ()
perimetreCercle ()
surfaceCercle ()
surfaceCarre ()
surfaceRectangle ()
