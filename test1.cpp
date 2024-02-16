#include <iostream>
int
main ()
{
  std::cout << "Hello World";
  //int acc = 0;
  float xmin=-50.0;
  float xmax=50.0;
  int ms=201;
  float yc=0.0;
  float xc=xmin;
  float step=(xmax-xmin)/ms;
  for (int i = 0; i <=ms; i++)
	{
	  yc = 2 * (xc * xc) - 3 * xc - 5;
	  std::cout << "x= " << xc << ";  y= " << yc << std::endl;
	  xc=xc+step;
	}

  return 0;
}
