# Python Mini Project – Core Programs

**Name:** Parepalli Satya Yuva Krishna  
**Branch:** AIML  
**Year:** 2nd Year, Semester 4  
**Tool Used:** IntelliJ IDEA (Python Code)

---

## 1. Sum of Two Numbers

**Approach:**  
Created a function that accepts two integers and returns their sum.

**Challenges:**  
None – basic arithmetic.

**Solution:**  
Used `a + b` and returned the result from a function.

---

## 2. Odd or Even

**Approach:**  
Checked whether the input number is divisible by 2.

**Challenges:**  
Simple logic, no issues.

**Solution:**  
Used modulus operator `%` to determine parity.

---

## 3. Factorial Calculation

**Approach:**  
Used both a manual loop and Python's `math.factorial()` function.

**Challenges:**  
Understanding and managing loop logic correctly.

**Solution:**  
Looped from 1 to `n` and multiplied incrementally; also used built-in function.

---

## 4. Fibonacci Sequence

**Approach:**  
Generated Fibonacci numbers iteratively using two variables `a` and `b`.

**Challenges:**  
Maintaining the current and next terms correctly during iteration.

**Solution:**  
Used a for-loop with `a, b = 0, 1` and `a, b = b, a + b`.

---

## 5. Reverse a String

**Approach:**  
Used Python slicing to reverse the string.

**Challenges:**  
None – straightforward with Python’s features.

**Solution:**  
Returned `s[::-1]`.

---

## 6. Palindrome Check

**Approach:**  
Checked whether a string is equal to its reversed version.

**Challenges:**  
No major challenge, but could consider ignoring cases and spaces in future improvements.

**Solution:**  
Used `s == s[::-1]`.

---

## 7. Leap Year Check

**Approach:**  
Used standard rules for leap year checking.

**Challenges:**  
Understanding the edge case (divisible by 100 but not by 400).

**Solution:**  
Used condition: `(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)`.

---

## 8. Armstrong Number

**Approach:**  
Raised each digit of the number to the power equal to the number of digits and summed them.

**Challenges:**  
Managing conversions between string and integer.

**Solution:**  
Used: `sum(int(d)**power for d in str(n)) == n`.

---

## Caesar Cipher – Custom Encryption & Decryption

**Approach:**  
The Caesar Cipher is one of the simplest and oldest encryption techniques. It works by shifting each letter in the message by a fixed number of positions in the alphabet. For example, if the shift is 3, then A becomes D, B becomes E, and so on. I implemented this manually without using any encryption libraries, which helped me understand how encryption works at a basic level.

The program accepts a plain text message and a key (the number of positions to shift), then outputs the encrypted text. It also supports decryption by applying the opposite shift.

**Challenges:**  
- I had to make sure the encryption worked for both **uppercase and lowercase** letters.
- I needed to **ignore special characters and spaces** without affecting the format.
- Handling the **wrap-around logic** when shifting letters beyond 'Z' or 'z' required some careful math.

**Solution:**  
- Used `ord()` to get the ASCII value of the letter.
- Subtracted the base ASCII value (`'A'` or `'a'`) to shift letters within a 0–25 range.
- Used `(position + shift) % 26` to handle wrap-around.
- Converted the result back to a character using `chr()`.
- For decryption, the same function is reused by passing a **negative shift**.

**What I Learned:**  
This helped me understand how simple encryption algorithms work and gave me practical experience with string manipulation, loops, and conditionals. It also deepened my appreciation for the complexity behind even basic security methods.

---

## 📘 Conclusion

This mini project helped me reinforce important core Python programming skills like loops, conditionals, functions, and string operations. The Caesar Cipher task, especially, gave me hands-on exposure to encryption logic and how data can be secured using basic principles.

Creating the documentation helped me organize and reflect on my thought process, which improved both my problem-solving clarity and my ability to communicate technical solutions effectively — a vital skill for any future developer.

---

