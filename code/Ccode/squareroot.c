// save file squareroot.c
// compile gxx squareroot.c -o aquareroot.exe
// run ./squareroot.exe
#include <stdio.h>
#include <math.h>
// define functions
float squareroot(float a);

float main(){
  float a,s;
  printf("Input a number : ");
  scanf("%f",&a);
  printf("The number you types was %f\n",a);
  s = squareroot(a);
  printf("The square root of %f is %f\n",a,s);
  return 0;
}
float squareroot (float a){
  float s = sqrt(a);
  return s;
}
