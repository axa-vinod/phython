"""
Aksa Vinod
3-12-2024
"""
def fibonacci_number(n):
    sequence=[]
    first_number,second_number=0,1
    for _ in range(n):
        sequence.append(first_number)
        first_number,second_number=second_number,second_number+first_number
    return sequence
