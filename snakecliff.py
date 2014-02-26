import random
import math

def testSteps(steps, maxAllowableSteps):
	takeNextStep = True
	i = 0
	position = 0
	while takeNextStep and (i<len(steps)):

		position += steps[i]

		overMax = (position >= maxAllowableSteps)
		underMin = (position <= -1*maxAllowableSteps)
	
		if overMax or underMin:
			takeNextStep = False
		i += 1
	return takeNextStep

maxAllowableSteps = 2
steps = [1,-1]
assert(True == testSteps(steps,maxAllowableSteps))
steps = [1,1]
assert(False == testSteps(steps,maxAllowableSteps))

steps = [1,-1,-1]
assert(True == testSteps(steps,maxAllowableSteps))
steps = [1,-1,-1,-1]
assert(False == testSteps(steps,maxAllowableSteps))

maxAllowableSteps = 3
steps = [1,1]
assert(True == testSteps(steps,maxAllowableSteps))
steps = [1,-1,1,1]
assert(True == testSteps(steps,maxAllowableSteps))
steps = [1,1,1]
assert(False == testSteps(steps,maxAllowableSteps))
steps = [1,-1,1,-1,1,-1,1,-1,1,1,1]
assert(False == testSteps(steps,maxAllowableSteps))


def callTestStepWithSkipping(steps, maxAllowableSteps):
	win = True
	for j in range(len(steps)):

		start = j
		skip = j+1

		subset= steps[start::skip]



		i = 0
		position = 0
		while win and (i<len(subset)):



			position += subset[i]

			overMax = (position >= maxAllowableSteps)

			underMin = (position <= -1*maxAllowableSteps)

			if overMax or underMin:
				win = False
				break	
			i += 1
		if not win:
			break
	return win

maxAllowableSteps = 2

steps = [1,-1]
assert(True == callTestStepWithSkipping(steps,maxAllowableSteps))
steps = [1,1]
assert(False == callTestStepWithSkipping(steps,maxAllowableSteps))

steps = [1,-1,-1,-1,1,1,-1]
assert(False == callTestStepWithSkipping(steps,maxAllowableSteps))

steps = [1,-1,1,-1]
assert(False == callTestStepWithSkipping(steps,maxAllowableSteps))

steps = [1,-1,-1,1]
assert(True == callTestStepWithSkipping(steps,maxAllowableSteps))

steps = [-1,1,1,-1,1,-1,-1,1]
assert(True == callTestStepWithSkipping(steps,maxAllowableSteps))

steps = [-1,1,1,-1,1,-1,1,-1]
assert(False == callTestStepWithSkipping(steps,maxAllowableSteps))


maxAllowableSteps = 3
steps = [-1,1,1,-1,1,-1,1,-1]
assert(True == callTestStepWithSkipping(steps,maxAllowableSteps))

steps = [-1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,1,-1,1,-1,-1,1]
assert(False == callTestStepWithSkipping(steps,maxAllowableSteps))



print 'unit tests OK'




def getRandomSteps(stepsLength):
	steps = []
	for i in range(4):
		next = random.choice([1,-1])
		steps.append(next)
	for i in range(4,stepsLength):		
		prev1 = steps[i-1]
		prev2 = steps[i-2]
		prev3 = steps[i-3]
		prev4 = steps[i-4]
		if prev1 == prev2 == prev3 == prev4:
			next = prev1 * -1
		else:
			next = random.choice([1,-1])
		steps.append(next)
	return steps



MAX_ALLOWABLE_STEPS = 3

STEPS_LENGTH = 40

EXHAUSTED = int(math.pow(10,5.95))

for i in range(EXHAUSTED):
	steps = getRandomSteps(STEPS_LENGTH)

	win = callTestStepWithSkipping(steps,MAX_ALLOWABLE_STEPS)
	if win:
		break

print 'done'
if win:
	print steps
