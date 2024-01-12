# Program to solve quadratic equation using function
import cmath

# Function to solve quadratic equation
def quad_function(a,b,c):
  discriminant = cmath.sqrt(b**2 - 4*a*c)
  if discriminant.real > 0:
    root1 = -b + discriminant / (2*a)
    root2 = -b - discriminant / (2*a)
    return root1,root2
  elif discriminant.real == 0:
    root = -b / (2*a)
    return root
  else:
    print("The roots are imaginary")

def main():
  a = float(input("Enter the value of a: "))
  b = float(input("Enter the value of b: "))
  c = float(input("Enter the value of c: "))
  print(quad_function(a,b,c))

if __name__ == '__main__':
  main()