def printOut():
    print("Hey");


#Arrays
groceryList = ['Juice', 'Salsa', 'Pinapeals', "Apples"];
print("First item", groceryList[0]);
groceryList.append("Bannans")
print(groceryList);
groceryList.sort();
print(groceryList);
groceryList.reverse();
print(groceryList);
del groceryList[4];
print(groceryList);
print(len(groceryList));
print(max(groceryList))

#Objects
DBStructure = {
    "ORDERBY" : ["ALPHABET", "FIFO", "NUMBER"],
    "Technique" : {
        "File" : "Save",
        "File" : "Delete"
    }
}
print(DBStructure["ORDERBY"]);
DBStructure["Hello"] = "World";

#if,elif,el
age = 30;

if age>16:
    print("Allowed To Drive");
elif age<=16:
    print("Not Allowed To Drive(By Self)");
else:
    print("Invalid Age");

#for

for y in groceryList:
    print(y);#Key:Val

class Animal:
    _name =None
    _age = None
    _load =__loader__
    _type = NotImplemented

    def __init__(self,name,age,type):
        self._name = name
        self._age = age
        self._type = type

    def  getName(self):
        return self._name
    def setName(self,name):
        self._name = name;

    def getType(self):
        return self._type

    def setType(self, type):
        self._type = type;
    def getAge(self):
        return self._age
    def setAge(self,age):
        self._age = age;
    def printInfo(self):
        return "I am {} and i am a {} years old {}. ".format(
                                                             self._name,
                                                             self._age,
                                                             self._type
                                                             )

cat = Animal("Whiskers",12,"cat");
print(cat.getAge(), cat.getName(), cat.getType());
print(cat.printInfo())

#Inheriting
class Dog(Animal):
    __owner = NotImplemented

    def __init__(self,name,age,type,owner):
        self._owner = owner;
        super(Dog,self).__init__(name,age,type);

    def setOwner(self,owner):
        self._owner = owner;
    def getOwner(self):
        return self._owner
    def getType(self):
        Animal.getType();
    def printInfo(self):
        Animal.printInfo(self) + "My Owner Is {}".format(self._owner)


buchie = Dog("Buchie", 12, "dog", "Amanuel");
print(buchie.printInfo())
