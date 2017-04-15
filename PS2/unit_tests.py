import ID3, parse, random
from matplotlib import pyplot as plt


def testID3AndEvaluate():
  data = [dict(a=1, b=0, Class=1), dict(a=1, b=1, Class=1)]
  tree = ID3.ID3(data, 0)
  if tree != None:
    ans = ID3.evaluate(tree, dict(a=1, b=0))
    if ans != 1:
      print "ID3 test failed."
    else:
      print "ID3 test succeeded."
  else:
    print "ID3 test failed -- no tree returned"

def testPruning():
  data = [dict(a=1, b=0, Class=1), dict(a=1, b=1, Class=1), dict(a=0, b=1, Class=0), dict(a=0, b=0, Class=1)]
  validationData = [dict(a=1, b=0, Class=1), dict(a=1, b=1, Class=1), dict(a=0, b=0, Class=0), dict(a=0, b=0, Class=0)]
  tree = ID3.ID3(data, 0)
  ID3.prune(tree, validationData)
  if tree != None:
    ans = ID3.evaluate(tree, dict(a=0, b=0))
    if ans != 0:
      print "pruning test failed."
    else:
      print "pruning test succeeded."
  else:
    print "pruning test failed -- no tree returned."

def testID3AndTest():
  trainData = [dict(a=1, b=0, c=0, Class=1), dict(a=1, b=1, c=0, Class=1), 
  dict(a=0, b=0, c=0, Class=0), dict(a=0, b=1, c=0, Class=1)]
  testData = [dict(a=1, b=0, c=1, Class=1), dict(a=1, b=1, c=1, Class=1), 
  dict(a=0, b=0, c=1, Class=0), dict(a=0, b=1, c=1, Class=0)]
  tree = ID3.ID3(trainData, 0)
  fails = 0
  if tree != None:
    acc = ID3.test(tree, trainData)
    print acc
    if acc == 1.0:
      print "testing on train data succeeded."
    else:
      print "testing on train data failed."
      fails = fails + 1
    acc = ID3.test(tree, testData)
    print acc
    if acc == 0.75:
      print "testing on test data succeeded."
    else:
      print "testing on test data failed."
      fails = fails + 1
    if fails > 0:
      print "Failures: ", fails
    else:
      print "testID3AndTest succeeded."
  else:
    print "testID3andTest failed -- no tree returned."

# inFile - string location of the house data file
def testPruningOnHouseData(inFile):
  withPruning = []
  withoutPruning = []
  data = parse.parse(inFile)
  for i in range(10):
    random.shuffle(data)
    train = data[:len(data)/2]
    valid = data[len(data)/2:3*len(data)/4]
    test = data[3*len(data)/4:]

    tree = ID3.ID3(train, 'democrat')
    acc = ID3.test(tree, train)
    print "training accuracy: ",acc
    acc = ID3.test(tree, valid)
    print "validation accuracy: ",acc
    acc = ID3.test(tree, test)
    print "test accuracy: ",acc
  
    ID3.prune(tree, valid)
    acc = ID3.test(tree, train)
    print "pruned tree train accuracy: ",acc
    acc = ID3.test(tree, valid)
    print "pruned tree validation accuracy: ",acc
    acc = ID3.test(tree, test)
    print "pruned tree test accuracy: ",acc
    withPruning.append(acc)
    tree = ID3.ID3(train+valid, 'democrat')
    acc = ID3.test(tree, test)
    print "no pruning test accuracy: ",acc
    withoutPruning.append(acc)
  print withPruning
  print withoutPruning
  print "average with pruning",sum(withPruning)/len(withPruning)," without: ",sum(withoutPruning)/len(withoutPruning)

#<<<<<<< HEAD
# inFile - string location of the house data file
def LearningCurvePlot(inFile):
  withPruning = []
  withoutPruning = []
  data = parse.parse(inFile)
  for size in range(10, 300, 5):
    acc = 0
    acc_prune = 0
    for i in range(100):
      random.shuffle(data)
      train = data[:size]
      test = data[size:]

      tree = ID3.ID3(train, 'democrat')
      acc += ID3.test(tree, test)  

      ID3.prune(tree, test)
      acc_prune += ID3.test(tree, test)

    withoutPruning.append(acc)
    withPruning.append(acc_prune)
    print 'size: ', size

  plt.plot(range(10,300,5), withPruning, 'bo-', label = 'with Pruning')
  plt.plot(range(10,300,5), withoutPruning, 'ro-', label = 'without Pruning')
  plt.title('Accruacy vs. training set size')
  plt.xlabel('training set size')
  plt.ylabel('Accuracy / %')
  plt.legend()
  plt.show()


def testTrainData(inFile):
	data = parse.parse(inFile)
	withoutPruning = []

	for size in range(10,300,5):
		acc = 0
		for i in range(100):
			random.shuffle(data)
			tree = ID3.ID3(data[:size], 'democrat')
			acc += ID3.test(tree, data[:size])
		withoutPruning.append(acc)
		print 'size: ', size

	plt.plot(range(10,300,5), withoutPruning, 'ro-', label = 'without Pruning')
	plt.title('Accruacy vs. training set size')
	plt.xlabel('training set size')
	plt.ylabel('Accuracy / %')
	plt.legend()
	plt.show()


#testID3AndEvaluate()
#testPruning()
#testID3AndTest()
#testPruningOnHouseData('house_votes_84.data')
#LearningCurvePlot('house_votes_84.data')
#testTrainData('house_votes_84.data')
#=======
def plottestdata(inFile):
  withPruning = []
  withoutPruning = []
  withaccuracy = []
  withoutaccuracy = []
  data = parse.parse(inFile)
  for j in range(10,300,10):
    for i in range(100):
      random.shuffle(data)
      train = data[:j]
      test = data[j:j+(len(data)-j)/2]
      valid = data[j+(len(data)-j)/2:]
      tree = ID3.ID3(train, 'democrat')
      ID3.prune(tree, valid)
      acc = ID3.test(tree, test)
      if isinstance(acc,float):
        withPruning.append(acc)
      tree = ID3.ID3(train+valid, 'democrat')
      acc = ID3.test(tree, test)
      if isinstance(acc,float):
        withoutPruning.append(acc)
    acc = sum(withPruning)/len(withPruning)
    withaccuracy.append(acc)
    acc = sum(withoutPruning)/len(withoutPruning)
    withoutaccuracy.append(acc)
  plt.plot(range(10,300,10),withoutaccuracy,'ro-', label = 'without Pruning')
  plt.plot(range(10,300,10),withaccuracy,'bo-', label = 'with Pruning')
  plt.xlabel('number of trianing example')
  plt.ylabel('accuracy on test data')

  plt.show()
#testID3AndEvaluate()
#testPruning()
#testID3AndTest()
#testPruningOnHouseData('house_votes_84.data')
plottestdata('house_votes_84.data')
#>>>>>>> origin/master
