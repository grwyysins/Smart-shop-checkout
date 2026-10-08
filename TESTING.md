# Testing

The Smart Shop Checkout System was tested using different inputs
to make sure that valid inputs work correctly and invalid inputs
do not crash the program.

| Test | Input | Expected Result | Result |
|---|---|---|---|
| Valid product code | P001 | Product is added to basket | Pass |
| Another valid product | P003 | Product is added to basket | Pass |
| Invalid product code | P999 | Error message is displayed | Pass |
| Valid quantity | 3 | Product is added with quantity 3 | Pass |
| Zero quantity | 0 | Quantity is rejected | Pass |
| Negative quantity | -2 | Quantity is rejected | Pass |
| Invalid quantity | abc | Error message is displayed | Pass |
| View basket | Option 2 | Current basket is displayed | Pass |
| Remove existing item | P001 | Item is removed | Pass |
| Remove unavailable item | P999 | Error message is displayed | Pass |
| No discount | Total below KSh 5,000 | No discount applied | Pass |
| 5% discount | Total of KSh 5,000 or more | 5% discount applied | Pass |
| 10% discount | Total of KSh 10,000 or more | 10% discount applied | Pass |
| Insufficient payment | Payment below total | Payment is rejected | Pass |
| Invalid payment | abc | Error message is displayed | Pass |
| Successful payment | Payment greater than total | Change is calculated | Pass |
| Exit | Option 5 | Program closes | Pass |

## Conclusion

The program successfully handles normal shopping operations
and common input errors without requiring the user to restart
the program.