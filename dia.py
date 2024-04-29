class Dia:
    def __init__(self, anyo = 1970, mes = 1, dia = 1):
        self.anyo = anyo
        self.mes = mes
        self.dia = dia
        self.comprobar_fecha()
        
    def es_bisiesto(self):
        return self.anyo % 4 == 0 and (self.anyo % 100 !=0 or self.anyo % 400 == 0)
    
    def comprobar_fecha(self):
        if self.anyo < 1:
            raise ValueError("Fecha incorrecta. Año fuera de rango")
        if self.mes < 1 or self.mes > 12:
            raise ValueError("Fecha incorrecta. Mes fuera de rango.")
        
        dias_del_mes = (31, 29 if self.es_bisiesto() else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,31)
       

        if self.dia < 1 or self.dia> dias_del_mes[self.mes - 1]:
            raise ValueError("Fecha incorrecta. Dia fuera de rango.")
        

        """ esto seria la linea 20 pero desglosada, la parte de arriba esta con un diccionario y una condición para todo
        if self.dia < 1 or self.dia >31:
            raise ValueError("Fecha incorrecta. Día fuera de rango.")
        if self.dia > 28 and self.mes == 2 and self.es_bisiesto() == False:
            raise ValueError("Fecha incorrecta. Día fuera de rango")
       
        if self.dia > 30 and (self.mes == 4 or self.mes == 6 or self.mes == 9 or self.mes == 11):
            raise ValueError("Fecha incorrecta. Día fuera de rango.")
        
            este sería para el mes de febrero es bisiesto
        if self.dia > 29 and self.mes == 2 and self.es_bisiesto() == True:
            raise ValueError("Fecha incorrecta. Día fuera de rango")
        """
        
       


        
        
