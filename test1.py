def calculate_polynomial(coeffs, x):
  """
  Calculates the value of a polynomial.

  This function takes a list of coefficients and a value for x, 
  and calculates the result of the polynomial.

  For example:
    If coeffs = [2, 1] and x = 3, it calculates 2*3 + 1 = 7

  Args:
    coeffs: A list of numbers representing the coefficients.
    x: The value of x.

  Returns:
    The result of the polynomial.
  """
  answer = 0
  for i, coeff in enumerate(coeffs[::-1]):  # Go through coefficients in reverse
    answer += coeff * x**i  # Calculate each term and add it to the answer
  return answer

# Example:
coefficients = [2, 1]  # 2x + 1
x_value = 3
result = calculate_polynomial(coefficients, x_value)
print(result)  # Output: 7