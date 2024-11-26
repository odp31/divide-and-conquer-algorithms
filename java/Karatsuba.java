public class Karatsuba
  {
    public static long karatsuba(long x, long y)
    {
      // base case; for small numbers, use simple multiplication
      if(x < 10 || y < 10)
      {
        return x * y;
      }
      // determine length of larger number
      int n = Math.max(String.valueOf(x).length(), String.valueOf(y).length());

      // divide numbers into two havles
      int nHalf = n / 2;
      long a = x / (long) Math.pow(10, nHalf);
      long b = x % (long) Math.pow(10, nHalf);
      long c = y / (long) Math.pow(10, nHalf);
      long d = y % (long) Math.pow(10, nHalf);

      // recursively calculate the products
      long ac = karatsuba(a, c);
      long bd = karatsuba(b, d);
      long ad_bc = karatsuba(a + b, c + d) - ac - bd;

      // combine results 
      return ac * (long) Math.pow(10, 2 * nHalf) + ad_bc * (long) Math.pow(10, nHalf) + bd;
    }
  }
