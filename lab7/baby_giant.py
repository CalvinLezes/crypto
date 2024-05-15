def baby_step_giant_step(a, y, p):

    global multiplication_counter_BSGS
    multiplication_counter_BSGS = 0

    # Step 1: Compute the value of m.
    m = int(p ** 0.5) + 1
    
    # Step 2: Compute the list of baby steps.
    baby_steps = {}
    print('Baby steps: ')
    for j in range(m):
        baby_steps[y*pow(a, j, p)] = j
        print(y*pow(a, j, p))
        multiplication_counter_BSGS += 1

    # Step 3: Compute the giant step.
    print('Giant steps: ')
    for i in range(1, m):
        giant_step = pow(a, i*m, p)
        multiplication_counter_BSGS += 1
        print(giant_step)
        if giant_step in baby_steps:
            print('i:',i,' m ',m, ' j ', baby_steps[giant_step])
            return (i) * m - baby_steps[giant_step]
        else:
            giant_step = pow(a, i*m, p)
    return None    

def brute_force(a, h, p):
    global multiplication_counter_BF
    multiplication_counter_BF = 0
    for i in range(p-1):
        multiplication_counter_BF += 1
        if(pow(a,i,p)==h):
            return i, multiplication_counter_BF

# Example usage:
a = 2
y = 178261486
p = 987654321
x = baby_step_giant_step(a, y, p)
print("BSGS Solution:", x)
print("BSGS number of multiplications:", multiplication_counter_BSGS)
x2 = brute_force(a, y, p)
print("BF Solution:", x)
print("BF number of multiplications:", multiplication_counter_BF)