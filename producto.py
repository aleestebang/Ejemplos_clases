class producto:
    Codigo=''
    Tipo=''
    Nombe=''
    Marca=''
    Precio=0
    Stock=0
    Procedencia=''

    def __int__(self):
        self.Codigo='AA001'
        self.Tipo='Electronica'
        self.Nombre='TV'
        self.Marca='S/M'
        self.Precio=500
        self.Stock=1
        self.Procedencia='AMERICA'

        def setProcedencia(self , Procedencia):
            if Procedencia.upper() == 'AMERICA' or Procedencia.upper() == 'EUROPA' or Procedencia.upper() == 'ASIA':
                self.Procedencia = Procedencia
                return True
            else:
                print("Procedencia debe ser AMERICA, EUROPA, ASIA")
                return False
