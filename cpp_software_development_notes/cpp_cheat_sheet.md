# C++ Cheat Sheet


* [Initialization](#Initialization)
* [Keywords](#keywords)
* [Constructors and Destructors](#Constructors-and-Destructors)
* [Loops](#loops)
* [Pointers](#pointers)


### Initilization
* Variable initialization, all are ok:
```c++
int x = 3;
int x(3);
int x{3};
std::string name = "Some Name";
std::string name("Some Name");
std::string name{"Some Name"};
```
* Vector initialization via initialization list.
``` c++
std::vector<int> v(100, 1);  // A vector containing 100 items: All 1s.
std::vector<int> v{100, 1};  // A vector containing 2 items: 100 and 1.
```

* Class member initialization. Note that Inherited class constructor may need to be called first. Example syntax for class initialization with a inherited class
```c++
class MyClass: public SomeBaseClass 
{
public:
  int var;
  int other_var;

  MyClass(int var, double other_var)
      : SomeBaseClass(var), // Optional call of base class constructor if needed
        some_var_(var),             
        some_other_var_(var + 1) {
  // Other work here
  } 
```

## Keywods
```c++
volatile // indicates to compiler the value of this may change at any time 
         // (so it doesn't optimize it to a constant for example)
static // When used for data members in classes, indicates all objects of 
       // that class share that same data member. Must be initializaed outside of the class
       // declaration. E.g.:
MyClass::static_data_member = 0;
       // When used for a variable in a function, means that variable will be initialized and 
       // allocated the first time that function is called and that variable is reached, and will
       // remain and exist after function ends/goes out of scope

       // When used for a class function, means that function can be called outside of an instance
       // of a class, e.g. called directly as:
ret_val = MyClass::some_static_method();

const // For a variable, indicates it is constant and can not be modified, usually
      // used to pass a const reference to a function or method to remove copy overhead while 
      // guranteeing user cant modify value, e.g.:
my_function(const BigData& some_really_big_data) {...

     // For a method, indicates it does not mutate/modify any aspect of its class (like a pure getter function), e.g.:
void MyClass::my_const_method() const {...

      
```


## Constructors and Destructors 
* If not default constructor and destructors specified, defaults are used
* Normal destructor and destructor syntax:

```c++
class MyClass
{
public:

  MyClass(); // Constructor
  ~MyClass(); // Destructor
  // Other work here
} 
```
* If a non-empty constructor is defined, default constructor wont be available unless explicitly defined
* In inheritanece, declaring a constructor = default means the base class default constructor will be invoked
```c++
class MyClass
{
public:

  MyClass(int a); // Non-default Constructor, if defined, default constructor unavailable
  MyClass() = default;
}
```

## Loops
* Basic for loop syntax:
```c++
for (int i = 0; i < some_num; i++) {
    // Loop work
}
```

* Range based for loop (similar to elementwise python loop), c++11
```c++
for (elem : some_vector) {
    // elem will be the element in the vectors
}
```

* For loops using iterators in a vector (explicit syntax for context)
```c++
vector<int> myIntVector;
vector<int>::iterator myIntVectorIterator;

// Add some elements to myIntVector
myIntVector.push_back(1);
myIntVector.push_back(4);

for(myIntVectorIterator = myIntVector.begin(); 
        myIntVectorIterator != myIntVector.end();
        myIntVectorIterator++) {
    cout<<*myIntVectorIterator<<" ";
    //Should output 1 4
}
```

More general syntax:
```c++
for (auto it = some_vec.begin(), it != some_vec.end(); it++) {
    *it; // Dereference of the iterator pointer yields that element in the vector
}
```
* For loop **reverse** iteration
```c++
for (auto it = my_vector.rbegin(); it != my_vector.rend(); ++it) {
    // loop stuff}
} 
```




## Map, unordered map, set, unordered set
* Range based for loop


## Unordered Map

## Vector Operations
* Insert (and concatenate)
* Erase
* Sub vector (splicing)
* Push back
* sort
* Different kind of finds
