# You need to figure out which sets of panels in any given array you can take offline to repair while still maintaining the maximum amount of power output per array, and to do THAT, you'll first need to figure out what the maximum output of each array actually is. Write a function solution(xs) that takes a list of integers representing the power output levels of each panel in an array, and returns the maximum product of some non-empty subset of those numbers. So for example, if an array contained panels with power output levels of [2, -3, 1, 0, -5], then the maximum product would be found by taking the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30.  So solution([2,-3,1,0,-5]) will be "30".

# Each array of solar panels contains at least 1 and no more than 50 panels, and each panel will have a power output level whose absolute value is no greater than 1000 (some panels are malfunctioning so badly that they're draining energy, but you know a trick with the panels' wave stabilizer that lets you combine two negative-output panels to produce the positive output of the multiple of their power values). The final products may be very large, so give the solution as a string representation of the number.
def solution(xs):
    positiveOutput = []
    negativeOutput = []
    zero = 0
    for painel in xs:
        if painel > 0:
            positiveOutput.append(painel)
        elif painel < 0:
            negativeOutput.append(painel)
        else: zero += 1
    if len(negativeOutput) > 1 and (len(negativeOutput)%2) == 1:
        negativeOutput.sort(reverse=True)
        negativeOutput.pop(0)
    totalOutputArray = positiveOutput + negativeOutput
    if len(totalOutputArray) > 1:
        totalOutput = 1
        for po in totalOutputArray:
            totalOutput *= po
        return str(totalOutput)
    elif zero == 0: return str(totalOutputArray[0])
    else:
        return "0"

print(solution([-1,-5,-7]))