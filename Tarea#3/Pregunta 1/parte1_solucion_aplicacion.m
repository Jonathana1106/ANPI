function parte1_solucion_aplicacion()
  warning('off');
  pkg load symbolic;
  pkg load NumInt;
  syms x;
  f = (200*(x/(5 + x))*(2.71828)^((-2*x)/30));
  display('Metodo del Trapecio')
  I = trapecio(f, 0, 30);
  display(I)
  display('Metodo del Simpson')
  I = simpson(f, 0, 30);
  display(I)
  display('Metodo del Trapecio Compuesto')
  I = trapecio_compuesto(f, 0, 20, 3);
  display(I) 
  display('Metodo de Simpson Compuesto')
  I = simpson_compuesto(f, 0, 30, 3);
  display(I) 
  display('Metodo de Cuadratura Gaussiana')
  I = gaussiana(f, 0, 30, 2);
  display(I) 
  display('Metodo de Cuadratura Gaussiana Compuesta')
  I = gaussiana_compuesta(f, 0, 30, 2, 3);
  display(I) 
  display('Metodo de Romberg')
  I = romberg(f, 0, 30, 3);
  display(I) 
endfunction