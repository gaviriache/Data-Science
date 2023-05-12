# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 16:27:02 2019

@author: Luis Miguel Gaviria
"""
class Adn(object):
    
    def __init__(self):  #constructor con un unico atributo para la clase, el cual
                                #contendrá la secuencia inicial de nucleotidos.
        self.__secuence = ''
        
    def showSecuence(self, chain):        
        self.__secuence = list(chain.upper()) 
        
        return self.__secuence  # retorna como dato, la lista de nucleotidos repre-
                                #sentados en letras mayusculas por convención.
                                              
    def validationChain(self, chain):  #método fundamental para validar que la secuencia de 
                                       #bases sea correcta respecto a la convención usada para bases 
        for k in chain:
            if k != 'a' and k != 't' and k != 'c' and k != 'g':
                
                print('La secuencia de datos no corresponde es su totalidad con los nucleótidos correctos' + '\n')
                print('---------------------------------------------------------------------------')
                data = input("Ingresa una secuencia aleatoria de bases nitrogenadas " + "|A - T - C - G|: ")
                self.validationChain(data)  #función recursiva que se invoca así misma para ejecutarse nueva/
            else:
                pass
        print('----------------------------------', '\n', 'La información genética ha sido validada', '\n-----------------------------------')
       
        return True
    #------------------------------------------------------------------
    
class Enzyme(object):
    
    def __init__(self):  #constructor con dos unicos atributos para la clase, los cuales 
                         #definirán los estados de las enzimas on/off, inicial/ estarán inactivas .
        self.arn_polymerase = False
        self.arn_transference = False
        
    def activateEnzymePol(self, obj, chain):  #Se activa la enzima ARN Polimerasa si existe una secuencia de adn(obj) y es valida.
                                  #También deberá estar activa para permitir la transcripción a ARNm  
        if len(obj.showSecuence(chain)) != 0:
            self.arn_polymerase = True
            
            return self.arn_polymerase  #La enzima cambia de estado y con ello es posible iniciar la transcripción a ARNm.
        
        else:
            return self.arn_polymerase  #se mantendrá el estado en caso de que la secuencia adn no sea valida.
    #-----------------------------------                
              
    def unactivateEnzymePol(self):  #fundamentaAl para activar la enzima de ARNt e iniciar la traducción.
        
        if self.arn_polymerase == True:
            
            self.arn_polymerase = False
            
        return True  #Fundamental no tener return booleano dentro de bucles o condicionales.        
        
#        else:
#            return None
    #---------------------------------
    def activateEnzymeTrans(self):  #La asociación de aminoácidos con los respectivos codones tiene lugar solo si la enzima trans
                                    #se activa
                                    
        if self.unactivateEnzymePol() == True:  
            self.arn_transference = True
            
        return self.arn_transference 
        
#        else:
#            return None
    #-----------------------------------    
    def unactivateEnzymeTrans(self):  #Desactiva enzyma cuando todo proceso halla concluido, 
        
        self.arn_transference = False
        print('..............................................................\n',
              'El proceso de traducción génica ha sido completado exitosamente.')
        
        #return self.activateEnzymeTrans()
#--------------------------------------
    
class Arn(object):
    
    def __init__(self):
        
        self.secuence_arn = []
        self.id_secuence = 0
    #---------------------------    
    def transcription(self, chain, obj):  #método ejecuta proceso de transcripción adn -> arn 
        #retorna el método publico de la clase Adn al atributo de la clase Arn para iniciar proceso.
        self.secuence_arn = obj.showSecuence(chain)
        for k in self.secuence_arn:
            
            if k == 'T':
                self.secuence_arn[self.secuence_arn.index(k)] = 'U'
            
            else:
                pass
            
        return self.secuence_arn 
    #---------------------------------------------------------------------

    def assignMetionine(self, met = 'AUG'):  #Codon de inicio del proceso de traducción a aminoácidos, debe agregarse al Arn
        
        i = 0
        for k in met:
            self.secuence_arn.insert(i, k)
            i+= 1
            
        return self.secuence_arn
    #---------------------------------------------------------------------    
            
    def assignId(self, num):  #asigna un número de id a la secuencia de ARN
        
        self.id_secuence = num
        
    def showId(self):   #método que será invocado para retornar id de la cadena arn
        
        return self.id_secuence
    
    def validationType(self, num, obj):  #método para validar tipo númerico del id de arn
        
        try: #control de excepciones o errores de ejecución para tipo de dato, validación                
            
            if type(num) == str:
                num = int(num)
        
        except ValueError:
                
            print('Debes identificar la secuencia de Arn con una secuencia numérica' + '\n')
            print('--------------------------------------------------------------------------')
            n = int(input("Ingresa nuevamente un número de identificación para la secuencia de ARN: "))
            self.validationType(n, obj)  #función recursiva que se invoca así misma para ejecutarse nueva/
        
        if str(num) in obj.secuence_aa.keys():
            
            print('El número de identificación ingresado ya existe en nuestra base de datos' + '\n')
            print('--------------------------------------------------------------------------')
            n = int(input("Ingresa nuevamente un número de identificación diferente al anterior para continuar: "))
            self.validationType(n, obj)  #función recursiva que se invoca así misma para ejecutarse nueva/
            
            
        return True
  
#---------------------------------------------------------------------------------------------
               
class ProteinBank(Arn): # Clase que contine diccionario de codones asociados con aminoacidos
                        #Clase con métodos para secuenciar la cadena arn en tripletas y ligar con aa.
    def __init__(self):
        
        Arn.__init__(self)  #Herencia de atributos de la clase Arn - Concepto de Herencia 
        self.peptide = ''
        self.secuence_aa = {} 
        self.triples = []
        self.codons = ({"GCU":"Ala","GCC":"Ala","GCA":"Ala","GCG":"Ala","GAU":"Asp","GAC":"Asp","UGU":"Cys","UGC":"Cys",
                          "CGU":"Arg","CGC":"Arg","CGA":"Arg","GGU":"Gly","GGC":"Gly","GGA":"Gly","GGG":"Gly","CAU":"His",
                          "CAC":"His","AAA":"Lys","AAG":"Lys","UUU":"Phe","UUC":"Phe","CCU":"Pro","CCA":"Pro","CCC":"Pro",
                          "CCG":"Pro","UCU":"Ser","UCC":"Ser","UCA":"Ser","GUU":"Val","GUC":"Val","GUA":"Val","GUG":"Val",
                          "ACU":"Thy","ACC":"Thy","ACA":"Thy","ACG":"Thy","UAU":"Tyr","UAC":"Tyr","AUG":"Met"})
        
    def showCodons(self, obj): #método para depurar la cadena de ARN y agrupar las tripletas de bases, obj de tipo Arn
        
        self.id_secuence = obj.id_secuence  #esta función solo se ejecuta si la enzima self.__arn_transference se encuentra activa.  
        self.triples = obj.secuence_arn[:] #copia por slicing de la cadena de transcripción luego de ser agregado el codon Metionina       
        if len(self.triples) % 3 == 2:  #instrucciones de decisión para verificar longitud con multiplicidad 
            del self.triples[-2:]       # exacta de 3 y eliminar nucleótidos finales.  
            
        elif len(self.triples) % 3 == 1:
            del self.triples[-1]
            
        string = ''
        while len(self.triples[0]) == 1:  #Bucle para cortar el arn y transformarlo en codones o tripletas
                                            #se redefine la lista contenedora de las bases por los codones derivados
            for k in range(3):              #de la secuencia de arn. Una vez la longitud del primer elemento es != 1
                string = string + self.triples[k] #se termina el ciclo de cortes y la lista es redefinida a vector de codones
        
            del self.triples[:3]  #    
            self.triples.append(string)
            string = ''
        
        return self.triples
    #-------------------------------------------------------------------------------------
    
    def assignAminoacid(self, obj): #parametro de tipo Enzyme para asignar aa si enzima transferasa se encuentra activa
        
        array = self.triples[:]  #variable local que hace un slicing del retorno de la función anterior
        
        if obj.activateEnzymeTrans() == True:
            
            for w in array:
                if w in self.codons.keys(): #recorre el vector de claves del diccionario para verificar existencia
                    
                    self.peptide = self.peptide + self.codons[w] + '--'
                    
                else:
                    continue
                
            return self.peptide
        #--------------------------------------------------------------------
    def assignInfoProtein(self, arn, adn, data):  #-objetos por parametros.
        
        self.secuence_aa[arn.showId()] = [adn.showSecuence(data), arn.secuence_arn, self.triples, self.peptide]
        #diccionario que almacenará los pares id_proteína : datosobj.secuence_ar
 #--------------------------------------------------------------------------------------------------------------------------
    
class System(object):
    
   
    def showInformation(self, num, obj):    
        
        num = str(num)                
        if num in obj.secuence_aa.keys():
            
            print ('Código de secuencia genética -', str(obj.showId())) #muestra en pantalla el código luego la información completa.           
            for k in obj.secuence_aa[num]:                            
                print('--------------------------------------------------------' + '\n' + str(k))
        
        elif type(num) != int:
                            
            print('La identificación debe corresponder con un dato unicamente númerico' + '\n')
            print('--------------------------------------------------------------------------')
            n = input("Ingresa el código de identificación para la proteína : ")
            self.showInformation(n, obj)
            
        else:
            print('------------------------------------------------------------------------------------')
            print('El número que ingresaste para identificar la proteína no está asociado en nuestro banco de datos')
            print('--------------------------------------------------------------------------'  + '\n')
            m = int(input("Ingresa de nuevo el número identificador de la proteína para consultar los datos: "))
            self.showInformation(m, obj)  #función recursiva que se invoca así misma para ejecutarse nuevamente 
            #---------------------------------------------
    
    def searchChain(self, num, obj):
        
        num = str(num)
        if num in obj.secuence_aa.keys():
            
            k = obj.secuence_aa[num]  #accede a los datos asociados con el código 
            return k[3]  #retorna el elemento 4 de la lista de datos obtenidos al buscar por la clave de proteína
        
        else:
            print('------------------------------------------------------------------------------------')
            print('El número que ingresaste para identificar la proteína no está asociado en nuestro banco de datos')
            print('--------------------------------------------------------------------------'  + '\n')
            z = int(input("Ingresa de nuevo el identificador de la proteína para consultar la secuencia peptídica: "))
            self.searchChain(z, obj)  #función recursiva que se invoca así misma para ejecutarse nuevamente 
            #---------------------------------------------
    
    def quantityProtein(self, obj):
        
        print ('---------------------------------------------------' + '\n',
               'El banco de datos actualmente contiene ' + str(len(obj.secuence_aa.keys())) + ' proteínas codificadas.')      
   
    def deleteData(self, num, obj):
        
        num = str(num)
        if num in obj.secuence_aa.keys():
            del obj.secuence_aa[num]
            
            return ('..............................................................\n',
                    'Los datos de la proteína han sido eliminados del sistema.')
        else:
            return 'El código de identificación no existe en la base de datos'
        
        
#---------------------------------------------------------------------------------------------         
        
def main():
            
    var, adn, enzyme, arn, protein, sys = True, Adn(), Enzyme(), Arn(), ProteinBank(), System() # Se instancian todos los objetos.
    print('----------------------------------', '\n', 'Simulador de sintesis de aminoácidos', '\n-----------------------------------')
    while var == True:
        
        data = input('Ingresa una secuencia de nucleotidos de Adn para transcribir y traducir la información genética: ')#         
        if adn.validationChain(data) == True:
                      
            if enzyme.activateEnzymePol(adn, data) == True:
                                                                
                arn.transcription(data, adn)  #adn.showSecuence(data)
                arn.assignMetionine()
                num = input('-----------------------------------------\nAsigna a la secuencia de Arn un código numérico: ')
                arn.validationType(num, protein)
                enzyme.unactivateEnzymePol()  #Inactiva la enzima de arn polimerasa para activar transferasa
                
                if arn.validationType(num, protein) == True:
                    
                    arn.assignId(num)
                    enzyme.activateEnzymeTrans()  #Enzima que permite asociar los aa con los codones.
                    protein.showCodons(arn)          #se genera el vector de codones.
                    protein.assignAminoacid(enzyme)     #se asocian los codones con aminoácidos
                    protein.assignInfoProtein(arn, adn, data)  #Se almacenan todos los datos en diccionario.
                    enzyme.unactivateEnzymeTrans()  #Inactiva enzima transferasa.
                else:
                    
                    pass
                
            else:
                continue
              
        print ('----------------------------\n' + 'Opciones de Consulta de datos' +'\n----------------------------------\n',
               '0 - Iniciar una nueva síntesis peptídica \n 1 - Consultar secuencias Adn, Arn y péptidos \n',
               '2 - Consultar secuencia de aminoácidos sintetizados\n',
               '3 - Verificar la cantidad de registros en el banco de datos\n 4 - Eliminar bloque de datos de una proteína\n',
               '5 - Finalizar consulta de datos\n----------------------------------------------')
        
        main = int(input('Ingresa una opción numerica de acuerdo al menú presentado anteriormente: '))
        if main == 0:
               
            continue 
        while True:
            
            if main == 1:
                
                num = int(input("Ingresa el número identificador de la proteína para consultar los datos: "))
                sys.showInformation(num, protein)
                
            elif main == 2:
                
                num = int(input("Ingresa el número identificador de la proteína para consultar la síntesis de péptidos: "))
                print ('--------------------------------------------------------------')
                print (sys.searchChain(num, protein))
                
            elif main == 3:
    
                print(sys.quantityProtein(protein)) 
                 
            elif main == 4:
                                        
                num = int(input("Ingresa el número identificador de la proteína para descartar los datos del sistema :")) 
                print (sys.deleteData(num, protein))
                
            elif main == 5:
               
                var = False
                break     
            
            main = int(input('Si deseas ejecutar una nueva consulta escoge una opción de nuevo: '))                              
                            
        var = False                                                
# print('----------------------------------', '\n', , '\n-----------------------------------')
if __name__ == '__main__':
    main()
    