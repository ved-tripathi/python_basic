import sklearn
from sklearn import tree
features = [[2,300],[2,450],[8,200],[9,150]]
label = ["sports_car","sports_car","minivan","minivan"]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,label)
seats = str(input("enter the no. of seats of the vehicle:"))
horse_power = str(input("enter the horse power:"))
print(clf.predict([[1,140]]))
