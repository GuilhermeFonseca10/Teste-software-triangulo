from src import triangulo
class TesteTriangulo:

    def teste1(self):
        assert triangulo.Triangulo(0,0,0) == False
    
    def teste2(self):
        assert triangulo.Triangulo(1,3,3) == True
    
    def teste3(self):
        assert triangulo.Triangulo(3,4,5) == True
    
    def teste4(self):
        assert triangulo.Triangulo(3,3,6) == False