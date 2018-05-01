data = """
program compilador; 
    var float G1, G2, G3;
    int uno(int b, int a, float c){
        var int z;
        z = b;
        b = a + a - z;
        a = z;
        return z;
    }
    string tres(int z, float a, bool T){
        var string hola;
        return hola;
    }
    float dos(int que, int pedo){
        var float a;
        a = que - pedo;
        return a;
    }
    float cuatro( int a){
        var float h;
        h = 1;
        G1 = h + 1;
        return h;
    }
    void cinco(){

    }
    int fib(int n){
        var int ret;
        ret = n;
        if(ret <= 1){
            ret = 1;
        }
        else {
            ret = fib(ret-1) + fib(ret-2);
        }
        return ret;
    }
main{
    var string alpha;
    alpha = "WHAT iS GOINF ON";
    var int x,y;
    var bool z;
    var float h, l;
    h = 8.8;
    x = uno(1+1, 5,4.5);
    z = true;
    x = h;
    y =2;
    l=100.5 * 5.4 +1/3;
    h=cuatro(1000*1000/3);
    cwrite((h + h) * 5);
    z = x>y;
    cwrite(z);
}
          """

data = """
program compilador; 
    int funcionTest(int x, int y, int z){
        list int lista[12];
        var int a;
        list int lista2[5], lista3[4];
        var int b, c, d;
        return z;
    }

    int fib(int n){
        var int ret;
        ret = n;
        if(ret <= 1){
            ret = ret;
        }
        else {
            ret = fib(ret-1) + fib(ret-2);
        }
        return ret;
    }
main{
    list int a[2];
    a[1] = 2;

}
          """


data = """
program compilador; 


main{
    list int a[2];
    var int aa;
    a[1] = 3;
    a[0] = 4;
    aa = a[1] + a[0];


}
          """

    print('ok\n')
    print("Tabla de funciones: ")
    for a in dicFunciones:
        print('Funcion %s : ' % a)
        print("\t id : %s" % dicFunciones[a]['id'])
        print("\t tipo : %s" % dicFunciones[a]['tipo'])
        print("\t inicio : %s" % dicFunciones[a]['inicio'])
        print("\t dirRet : %s" % dicFunciones[a]['dirRet'])
        print('\t pars : %s' % dicFunciones[a]['pars'])

        print("\t vars :")
        for b in dicFunciones[a]['vars']:
            print("\t\t %s" % dicFunciones[a]['vars'][b])
        print('\t Temps: %s' % dicFunciones[a]['temps'])
        print('\t cantVar: %s' % dicFunciones[a]['cantVar'])
            
    print(" \n\n")
    print("Tabla de variables globales: ")
    for a in dicVarGlobales:
        print("%s : %s" % (a, dicVarGlobales[a]))
    print(" \n\n")
    print("Tabla de variables en main: ")
    for a in dicVarLocales:
        print("%s : %s" % (a, dicVarLocales[a]))
    print(" \n\n")
    print("Temporales en el main: ")
    for a in dicTemporales:
        print(a, dicTemporales[a])
    print(" \n\n")
    print("Tabla de Constantes Usados")
    for a in dicConstantes:
        print(a, dicConstantes[a])
    print(" \n\n")
    print("Cantidad Vars usadas en main")
    abcd = calcularTam(dicVarLocales, dicTemporales)
    print(abcd)
    print("\n\n")
    print("Cuadruplos:")
    for a in dicQuadruplos:
        print("%s: %s" % (a, dicQuadruplos[a]))