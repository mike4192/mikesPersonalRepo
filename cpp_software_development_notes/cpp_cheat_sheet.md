# C++ Cheat Sheet


* [Initialization](#Initialization)
* [Keywords](#keywords)
* [Constructors and Destructors](#Constructors-and-Destructors)
* [Loops](#loops)
* [Vector](#vector)
* [List](#list)
* [Deque](#deque)
* [Stack](#stack)
* [Queue](#queue)
* [Priority Queue](#priority-queue)
* [Set and Multiset](#set-and-multiset)
* [Map and Multimap](#map-and-multimap)
* [Unordered Set or Hash Set](#unordered-set-or-hash-set)
* [Unordered Map or Hash Table](#unordered-map-or-hash-table)
* [STL Algorithms](#stl-algorithms)
* [Lambda Functions](#lambda-functions)
* [Smart Pointers](#smart-pointers)
* [Major Additions of C++11](#major-additions-of-c++11)


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

Map initialization example:
```c++
map<string, string> singers = 
  { {"Lady Gaga", "+1 (212) 555-7890"},
  {"Beyonce Knowles", "+1 (212) 555-0987"}};
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
for (auto elem : some_vector) {
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





## Vector
Tables from https://users.cs.northwestern.edu/~riesbeck/programming/c++/stl-summary.html
#### Required Header
```c++
#include <vector>
```

#### Constructors
| Code                     | Operation                         | Time Complexity |
|--------------------------|--------------------------------------------------------|------|
| `vector<T> v;`             | Make an empty vector.                                  | O(1) |
| `vector<T> v(n);`          | Make a vector with N elements.                         | O(n) |
| `vector<T> v(n, value);`   | Make a vector with N elements, initialized to value.   | O(n) |
| `vector<T> v(begin, end);` | Make a vector and copy the elements from begin to end. | O(n) |

#### Accessors
| Code                     | Operation                         | Time Complexity |
|---------------|---------------------------------------------------------|------|
| `v[i];`         | Return (or set) the I'th element.                       | O(1) |
| `v.at(i);`      | Return (or set) the I'th element, with bounds checking. | O(1) |
| `v.size();`     | Return current number of elements.                      | O(1) |
| `v.empty();`    | Return true if vector is empty.                         | O(1) |
| `v.begin();`    | Return random access iterator to start.                 | O(1) |
| `v.end();`      | Return random access iterator to end.                   | O(1) |
| `v.front();`    | Return the first element.                               | O(1) |
| `v.back();`     | Return the last element.                                | O(1) |
| `v.capacity();` | Return maximum number of elements.                      | O(1) |

#### Modifiers 
| Code                     | Operation                         | Time Complexity |
|----------------------------|---------------------------------------------------|------------------|
| `v.push_back(value);`        | Add value to end.                                 | O(1) (amortized) |
| `v.insert(iterator, value);` | Insert value at the position indexed by iterator. | O(n)             |
| `v.pop_back();`              | Remove value from end (does not return value)     | O(1)             |
| `v.erase(iterator);`         | Erase value indexed by iterator.                  | O(n)             |
| `v.erase(begin, end);`       | Erase the elements from begin to end.             | O(n)             |

#### Other Useful Operations
* Concatenate two vectors:
```c++
vector1.insert( vector1.end(), vector2.begin(), vector2.end() );
```

* Get a sub vector (aka, slicing). Example, slicing v1 from index 2 to end:
```c++
auto v2 = std::vector<int>(v1.begin() + 2, v1.end());
```



## List
Lists are sequence containers that allow constant time insert and erase operations anywhere within the sequence, and iteration in both directions. The main drawback of lists and forward_lists compared to these other sequence containers is that they lack direct access to the elements by their position;

#### Required Header
```c++
#include <list>
```

#### Constructors
| Code                   | Operation                                          | Time Complexity |
|------------------------|----------------------------------------------------|-----------------|
| `list<T> l;`             | Make an empty list.                                | O(1)            |
| `list<T> l(begin, end);` | Make a list and copy the values from begin to end. | O(n)            |

* Also possible, initializer list initialization:
```c++
std::list<int> listOfInts({1,2,3,4,5});
```

#### Accessors
| Code       | Operation                               | Time Complexity |
|------------|-----------------------------------------|-----------------|
| `l.size();`  | Return current number of elements.      | O(1)            |
| `l.empty();` | Return true if list is empty.           | O(1)            |
| `l.begin();` | Return bidirectional iterator to start. | O(1)            |
| `l.end();`   | Return bidirectional iterator to end.   | O(1)            |
| `l.front();` | Return the first element.               | O(1)            |
| `l.back();`  | Return the last element.                | O(1)            |

#### Modifiers
| Code                       | Operation                                        | Time Complexity |
|----------------------------|--------------------------------------------------|-----------------|
| `l.push_front(value);`       | Add value to front.                              | O(1)            |
| `l.push_back(value);`        | Add value to end.                                | O(1)            |
| `l.insert(iterator, value);` | Insert value after position indexed by iterator. | O(1)            |
| `l.pop_front();`             | Remove value from front.                         | O(1)            |
| `l.pop_back();`              | Remove value from end.                           | O(1)            |
| `l.erase(iterator);`         | Erase value indexed by iterator.                 | O(1)            |
| `l.erase(begin, end);`       | Erase the elements from begin to end.            | O(1)            |
| `l.remove(value);`           | Remove all occurrences of value.                 | O(n)            |
| `l.remove_if(test);`         | Remove all element that satisfy test.            | O(n)            |
| `l.reverse();`               | Reverse the list.                                | O(n)            |
| `l.sort();`                  | Sort the list, small to large.                   | O(n log n)      |
| `l.sort(comparison);`        | Sort with comparison function.                   | O(n log n)       |
| `l.merge(l2);`               | Merge sorted lists into a single sorted list.    | O(n)            |





## Deque
deque (usually pronounced like "deck") is an irregular acronym of double-ended queue. Double-ended queues are sequence containers with dynamic sizes that can be expanded or contracted on both ends (either its front or its back). Best for use cases where inserations/removals happen at start or end only

#### Required Header
```c++
#include <deque>
```

#### Constructors
| Code                    | Operation                                           | Time Complexity |
|-------------------------|-----------------------------------------------------|-----------------|
| `deque<T> d;`             | Make an empty deque.                                | O(1)            |
| `deque<T> d(n);`          | Make a deque with N elements.                       | O(n)            |
| `deque<T> d(n, value);`   | Make a deque with N elements, initialized to value. | O(n)            |
| `deque<T> d(begin, end);` | Make a deque and copy the values from begin to end. | O(n)            |

#### Accessors
| Code       | Operation                                               | Time Complexity |
|------------|---------------------------------------------------------|-----------------|
| `d[i];`      | Return (or set) the I'th element.                       | O(1)            |
| `d.at(i);`   | Return (or set) the I'th element, with bounds checking. | O(1)            |
| `d.size();`  | Return current number of elements.                      | O(1)            |
| `d.empty();` | Return true if deque is empty.                          | O(1)            |
| `d.begin();` | Return random access iterator to start.                 | O(1)            |
| `d.end();`   | Return random access iterator to end.                   | O(1)            |
| `d.front();` | Return the first element.                               | O(1)            |
| `d.back();`  | Return the last element.                                | O(1)            |

#### Modifiers
| Code                       | Operation                                         | Time Complexity  |
|----------------------------|---------------------------------------------------|------------------|
| `d.push_front(value);`       | Add value to front.                               | O(1) (amortized) |
| `d.push_back(value);`        | Add value to end.                                 | O(1) (amortized) |
| `d.insert(iterator, value);` | Insert value at the position indexed by iterator. | O(n)             |
| `d.pop_front();`             | Remove value from front.                          | O(1)             |
| `d.pop_back();`              | Remove value from end.                            | O(1)             |
| `d.erase(iterator);`         | Erase value indexed by iterator.                  | O(n)             |
| `d.erase(begin, end);`       | Erase the elements from begin to end.             | O(n)             |







## Stack


#### Required Header
```c++
#include <stack>
```

#### Constructors
| Code                    | Operation                                           | Time Complexity |
|-------------------------|-----------------------------------------------------|-----------------|
| `stack< container<T> > s;`             | Make an empty stack.                                | O(1)            |

#### Accessors
| Code       | Operation                                               | Time Complexity |
|------------|---------------------------------------------------------|-----------------|
| `s.top();`    | Return the top element.                       | O(1)            |
| `s.size()`    | Return current number of elements             | O(1)            |
| `d.empty();`  | Return true if stack is empty.                | O(1)            |


#### Modifiers
| Code                       | Operation                                         | Time Complexity  |
|----------------------------|---------------------------------------------------|------------------|
| `d.push(value);`       | Push value on top.                     | O(1) (amortized) |
| `d.pop();`             | Pop value from top.                    | O(1)  |



## Queue
#### Required Header
```c++
#include <queue>
```

#### Constructors
| Code                    | Operation                                           | Time Complexity |
|-------------------------|-----------------------------------------------------|-----------------|
| `queue< container<T> > s;`             | Make an empty queue.                                | O(1)            |

#### Accessors
| Code       | Operation                                               | Time Complexity |
|------------|---------------------------------------------------------|-----------------|
| `s.front();`    | Return the front element.                       | O(1)            |
| `s.back();`    | Return the rear element.                       | O(1)            |
| `s.size()`    | Return current number of elements             | O(1)            |
| `d.empty();`  | Return true if queue is empty.                | O(1)            |


#### Modifiers
| Code                       | Operation                                         | Time Complexity  |
|----------------------------|---------------------------------------------------|------------------|
| `d.push(value);`       | Push value to the end                     | O(1) (amortized) |
| `d.pop();`             | Remove value from front                    | O(1)  |


## Set and Multiset
Sets store objects and automatically keep them sorted in large to small order (descending) and quick to find. In a set, there is only one copy of each objects. multisets are declared and used the same as sets but allow duplicate elements.

Anything stored in a set has to have a comparison predicate. This will default to whatever operator<() has been defined for the item you're storing. Alternatively, you can specify a predicate to use when constructing the set.

Implemented as a balanced binary tree under the hood (a red black tree)

Best for the following cases:
* A very large collection such that the difference between O(N) and (O(log N) is important
* Number of lookups is the same order of magnitude as the number of insertions. 
* Elements are inserted in random order, rather than in order
* Insertions and lookups are interleaved, there are not distinct insertion and lookup phases

Set best used if all 4 of these conditions are true, otherwise a simple sorter vector may be better
#### Required Header
```c++
#include <set>
```

#### Constructors
| Code                                | Operation                                                                                                                                       | Time Complexity |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| `set< type, compare > s;`             | Make an empty set. compare should be a binary predicate for ordering the set. It's optional and will default to a function that uses operator<. | O(1)            |
| `set< type, compare > s(begin, end);` | Make a set and copy the values from begin to end.                                                                                               | O(n log n)      |

Multiset is initialized same way except with `multiset` keyword.
#### Accessors
| Code               | Operation                                                                                                                   | Time Complexity |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------|-----------------|
| `s.find(key)`        | Return an iterator pointing to an occurrence of key in s, or s.end() if key is not in s.                                    | O(log n)        |
| `s.lower_bound(key)` | Return an iterator pointing to the first occurrence of an item in s not less than key, or s.end() if no such item is found. | O(log n)        |
| `s.upper_bound(key)` | Return an iterator pointing to the first occurrence of an item greater than key in s, or s.end() if no such item is found.  | O(log n)        |
| `s.equal_range(key)` | Returns pair<lower_bound(key), upper_bound(key)>.                                                                           | O(log n)        |
| `s.count(key)`       | Returns the number of items equal to key in s. Useful to check if something in the set.                                                                              | O(log n)        |
| `s.size();`          | Return current number of elements.                                                                                          | O(1)            |
| `s.empty();`         | Return true if set is empty.                                                                                                | O(1)            |
| `s.begin()`          | Return an iterator pointing to the first element.                                                                           | O(1)            |
| `s.end() `           | Return an iterator pointing one past the last element.                                                                      | O(1)            |


#### Modifiers
| Code                    | Operation                                                                                                                                                                | Time Complexity |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| `s.insert(iterator, key)` | Inserts key into s. iterator is taken as a "hint" but key will go in the correct position no matter what. Returns an iterator pointing to where key went.                | O(log n)        |
| `s.insert(key)`          | Inserts key into s and returns a pair<iterator, bool>, where iterator is where key went and bool is true if key was actually inserted, i.e., was not already in the set. | O(log n)        |

#### Other notes
A set or multiset can be traversed similar to a vector, for example:
```c++
for (auto it = s.begin(); it != s.end(); it++) {
  // Dereference set item with *it
}
```
A range based for loop can also be used


## Map and Multimap
Maps can be thought of as generalized vectors. They allow map[key] = value for any kind of key, not just integers. Maps are often called associative tables in other languages, and are incredibly useful. They're even useful when the keys are integers, if you have very sparse arrays, i.e., arrays where almost all elements are one value, usually 0.

Maps are implemented with balanced binary search trees, typically red-black trees. Thus, they provide logarithmic storage and retrieval times. Because they use search trees, maps need a comparison predicate to sort the keys. operator<() will be used by default if none is specified a construction time.

Maps store <key, value> pair's. That's what map iterators will return when dereferenced. To get the value pointed to by an iterator, you need to say
```c++
(*mapIter).second
```
Usually though you can just use map[key] to get the value directly.

Warning: map[key] creates a dummy entry for key if one wasn't in the map before. Use map.find(key) if you don't want this to happen.

multimaps are like map except that they allow duplicate keys. map[key] is not defined for multimaps. Instead you use lower_bound() and upper_bound(), or equal_range(), to get the iterators for the beginning and end of the range of values stored for the key. To insert a new entry, use map.insert(pair<key_type, value_type>(key, value)).

#### Required Header
```c++
#include <map>
```

#### Constructors
| Code                                                    | Operation                                                                                                                                            | Time Complexity |
|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| `map< key_type, value_type, key_compare > m;`             | Make an empty map. key_compare should be a binary predicate for ordering the keys. It's optional and will default to a function that uses operator<. | O(1)            |
| `map< key_type, value_type, key_compare > m(begin, end);` | Make a map and copy the values from begin to end.                                                                                                    | O(n log n)      |
Multiset is initialized same way except with `multmap` keyword.

#### Accessors
| Code               | Operation                                                                                                                        | Time Complexity |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------|-----------------|
| `m[key]`             | Return the value stored for key. **WARNING** This adds a default value if key not in map.                                                    | O(log n)        |
| `m.find(key)`        | Return an iterator pointing to a key-value pair, or m.end() if key is not in map.                                                | O(log n)        |
| `m.lower_bound(key)` | Return an iterator pointing to the first pair containing key, or m.end() if key is not in map.                                   | O(log n)        |
| `m.upper_bound(key)` | Return an iterator pointing one past the last pair containing key, or m.end() if key is not in map.                              | O(log n)        |
| `m.equal_range(key)` | Return a pair containing the lower and upper bounds for key. This may be more efficient than calling those functions separately. | O(log n)        |
| `m.size();`          | Return current number of elements.                                                                                               | O(1)            |
| `m.empty();`         | Return true if map is empty.                                                                                                     | O(1)            |
| `m.begin()`          | Return an iterator pointing to the first pair.                                                                                   | O(1)            |
| `m.end()`            | Return an iterator pointing one past the last pair.                                                                              | O(1)            |


#### Modifiers
| Code            | Operation                                                                      | Time Complexity |
|-----------------|--------------------------------------------------------------------------------|-----------------|
| `m[key] = value;` | Store value under key in map.                                                  | O(log n)        |
|` m.insert(pair)`  | Inserts the <key, value> pair into the map. Equivalent to the above operation. | O(log n)        |

#### Other notes
A map or multimap can be traversed similar to a vector, for example:
```c++
for (auto it = m.begin(); it != m.end(); it++) {
  // Dereference map item with *it
}
```
A range based for loop can also be used

Syntax for creating a pair:
```c++
std::pair<int,char> my_pair;
my_pair.first = 100;
my_pair.second = 'G';
```



## Unordered Set or Hash Set
An unordered set is implemented using a hash table where keys are hashed into indices of a hash table. All operations are O(1) on average which can go to linear time O(n) in worst case.
#### Required Header
```c++
#include <unordered_set>
```

#### Construction
```c++
unordered_set<string> string_set; // Empty unordered set of strings
unordered_set<char> char_set = {'d', 'b', 'c', 'a'}; // Initializer list example
```

#### Accessors
```c++
my_set.find(key); // Returns iterator pointing to the value in the set, or returns my_set.end() if not in set
my_set.count(key); // Counts occurences of a item in the unordered set, useful for seeing if an item is in a set
my_set.size(); // Returns number of elements in the unordered set
my_set.empty(); //Returns true if the set is empty, false otherwise

```
#### Modifiers
```c++
my_set.insert(value); //inserts element into the set, emplace does the same thing
my_set.clear(); // Removes all elements from the set and empties it.
my_set.erase(iterator); // Removes the item pointed by the iterator in the set, 
my_set.erase(my_set.find(10)); //to erase a specific value in a set
```


## Unordered Map or Hash Table
unordered_map is an associated container that stores elements formed by combination of key value and a mapped value. The key value is used to uniquely identify the element and mapped value is the content associated with the key. Both key and value can be of any type predefined or user-defined.
Internally unordered_map is implemented using Hash Table, the key provided to map are hashed into indices of hash table that is why performance of data structure depends on hash function a lot but on an average the cost of search, insert and delete from hash table is O(1).
#### Required Header
```c++
#include <unordered_map>
```

#### Construction
```c++
unordered_map<string, int> m; // Empty unordered set of string mapping to ints
m["a String"] = 10;
m["another_string"] = 20;
m.insert(make_pair("a_third_string",30));
```

#### Accessors
```c++
my_map.at(key); // Returns reference to the value with the element as key
my_map.count(key); // Counts occurences of a item in the unordered set, useful for seeing if an item is in a set
my_map.size(); // Returns number of elements in the unordered map
my_map.empty(); //Returns true if the map is empty, false otherwise
my_map.find(key); // Returns iterator pointing to that element in the map if it exists, or my_map.end() if it does not

```
#### Modifiers
```c++
my_map["something"] = 10; // Insertion of a key value pair
my_map.insert(key_value_pair); //inserts element into the map, emplace does the same thing
my_map.clear(); // Removes all elements from the map and empties it.
my_map.erase(key); //Erases an item by key
my_map.erase(iterator); // Removes the item pointed by the iterator in the map 

```


#### Other notes
Key and values (first and second, respectively) are retrieved from a iterator pointing to a single pair as
```c++
m.first;
m.second;
```

Maps can be traversed using for loop, and range based for loops
```c++
for (itr = umap.begin(); itr != umap.end(); itr++) 
    { 
        // itr works as a pointer to pair<string, double> 
        // type itr->first stores the key part  and 
        // itr->second stroes the value part 
        cout << itr->first << "  " << itr->second << endl; 
     } 
```

## STL Algorithms
Info primarily taken from here: https://users.cs.northwestern.edu/~riesbeck/programming/c++/stl-algorithms.html
#### find
find is for simple searching. Looks for a `value` in a container, starting at `begin` and stopping with `end`. Note `end` is one past the last item to checked, and is not checked itself.

Example:
```c++
resultIter = find(v.begin(), v.end(), value);
if (resultIter ~= v.end()) {
  cout << "Found it!" << endl;
}
```
#### find_if
Same as find but searches with a defined search condition. Example:
```c++
class IsEven {
  public:
    bool operator() (int x) const
    { return ((x % 2) == 0); }
} evenPred;
 
resultIter = find_if(v.begin(), v.end(), evenPred);
if (resultIter != v.end())
   cout << "Found the even number " << (*resultIter) << endl;
```

#### count
Count is for counting occurences of a value in a container.
```c++
int num = count(v.begin(), v.end(), 10);
cout << "Found " << num << " occurrences of 10." << endl;
```

`count_if` is similar to find_if.

#### max_element and min_element
Used to find max and minimum element of a range of elements in a container.
```c++
vector<int> stats;
vector<int>::iterator result;
...
cout << "Looking for max number" << endl;
result = max_element(stats.begin(), stats.end());
 
if (result != stats.end())
  cout << "Found " <<  (*result) << endl;
```

#### accumulate
Adds up a rnage of elements in a container, like a `sum` function. Example:
```c++
cout << "Sum of all the numbers is " 
     << accumulate(stats.begin(), stats.end(), 0)
     << endl;
```
The third argument, 0 in this case, is the initial value for the sum.

#### sort
Sorts a container. 
```c++
sort(v.begin(), v.end());
```
Instead of `operator<` a specific comparison function can be used.
```c++
void sort(RandomAccessIterator begin,
          RandomAccessIterator end,
          Compare comp)
```

Time complexity: n log n


## Lambda Functions
A lambda function or expression is a compact function defined in place. Generally return type is evaluated by the compiler and is not necessary to specify it explicitly. Useful to use with `for_each`

Basic format:
```
[ capture clause ] (parameters) -> return-type  
{   
   definition of method   
} 
```


Basic example of a lambda function assigned to a handle, and used.
```c++
auto sum = [](int x, int y) { return x + y; };
auto sum = [](int x, int y) -> int { return x + y; }; // equivalent definition but specifying return type
cout << sum(5,2) << endl;
```

Example of a lambda expression defined in place in a function argument. Function to print out an argument.
```c++ 
// Function to print vector 
void printVector(vector<int> v) 
{ 
    // lambda expression to print vector 
    for_each(v.begin(), v.end(), [](int i) 
    { 
        std::cout << i << " "; 
    }); 
    cout << endl; 
} 
```

The capture clause specifies which outside variables are available for the lambda function, and whether they should be captured by value or by reference. An empty capture clause means no external variables are captured.

A capture clause can be the name of a variable in the same scope as the lambda function. That variable is captured by copy.
Specifying `[=]` captures any referenced variables within the lambda by value (making a copy).

A variable can be captured by reference, for example `[first_var, &some_other_var]`. `first_var` is captured by value, while `some_other_var` is captured by reference.

`[&]` will capture any referenced variable by reference, but `[&, some_var]` will capture any referenced variable by reference except `some_var`.

Example of capturing a single variable:
```c++
// The user would introduce different values for divisor    
    int divisor = 3;
    vector<int> numbers { 1, 2, 3, 4, 5, 10, 15, 20, 25, 35, 45, 50 };
    for_each(numbers.begin(), numbers.end(), [divisor] (int y)
    {
        if (y % divisor == 0)
        {
            cout << y << endl;
        }
    });
```

Example achieving the same with `[=]`:
```c++
for_each(numbers.begin(), numbers.end(), [=] (int y)
{
    if (y % divisor == 0)
    {
        cout << y << endl;
    }
});
```
An arbitrary lambda expression can be passed to a function specified as a std::function type. For example:
```c++
void run_within_for_each(std::function<void (int)> func)
{
    vector<int> numbers{ 1, 2, 3, 4, 5, 10, 15, 20, 25, 35, 45, 50 };
 
    for_each(numbers.begin(), numbers.end(), func);
}
```

## Smart Pointers
Required header:
```c++
#include <memory>
```
Basic comparison between a raw and smart pointer. A smart pointer automatically unallocates memory of the pointed to data when the pointer goes out of scope.
```c++ 
void UseRawPointer()
{
    // Using a raw pointer -- not recommended.
    Song* pSong = new Song(L"Nothing on You", L"Bruno Mars"); 

    // Use pSong...

    // Don't forget to delete!
    delete pSong;   
}


void UseSmartPointer()
{
    // Declare a smart pointer on stack and pass it the raw pointer.
    unique_ptr<Song> song2(new Song(L"Nothing on You", L"Bruno Mars"));

    // Use song2...
    wstring s = song2->duration_;
    //...

} // song2 is deleted automatically here.
```

Alternative way to create an object instead of using the `new` keyword. Better to use make_unique except if a custom deleter is needed, or adapting a raw pointer. **make_unique** is a c++14 feature.
```c++
auto p1 = std::make_unique<double>(3.14);
std::unique_ptr<SomeObject> a = std::make_unique(SomeObject(...)) // more explicit, general
```

Smart pointers must be moved to change ownership. However, it can be "lended" to a function by passing the pointer by reference.
```c++
std::unique_ptr<double> a = std::make_unique<double>(3.14)
borrower(&a); //borrower function can use the pointer by reference
taker(std::move(a)); //taker function needs pointer to be moved to it
```

a shared_ptr is similar to a unique pointer, but it can be copied, and keeps an internal count of ownership of the pointer. When the counter reaches zero (all shared pointers go out of scope), the underlying resource is destroyed.

## Major Additions of C++11
* lambda expressions
* range based for loop
* `nullptr` keyword
* List initialization
* `auto` keyword
* deleted and defaulted functions 
  * e.g.: `A()=default;`
* Constructor can call another constructor of the same class (delegating)
* Smart pointers (shared_ptr, unique_ptr, move)
* Multithreading libraries (std::thread)
* Variadic template (arbitrary number of template arguments)
* unordered_map, unordered_set

## Major additions of C++14
* use of auto type-specifier in parameter list of lambda expression'
* Return type deduction
* Initializing stuff in lambda captures
* std::make_unique

## Major Additions of C++17
* Folding expressions
* Structured bindings (where a function returns a tuple like object that can be directly assigned to variables in a bracketed list `[x,y,z] = expr`)


See this page for more comprehensive summary of features in C++11/14/17/20:
https://github.com/AnthonyCalandra/modern-cpp-features


## Callable Object
```c++
// A callable object
class thread_obj {
public:
    void operator()(int x)
    {
        for (int i = 0; i < x; i++)
            cout << "Thread using function"
                  " object as  callable\n";
    }
};
```

## Multithreading
https://medium.com/swlh/c-multithreading-and-concurrency-introduction-f640ce986fa7


### Creating and starting threads
```c++
#include <thread>
#include <iostream>
#include <string>

void run(std::string threadName) {
  for (int i = 0; i < 10; i++) {
    std::string out = threadName + std::to_string(i) + "\n";
    std::cout << out;
  }
}

int main() {
  std::thread tA(run, "A");
  std::thread tB(run, "\tB");
  tA.join(); // Waits till thread a finishes
  tB.join(); // waits till thread b finishes
}
```

### Simple Mutexes
* Example of a thread safe queue
* Problem with simple mutex: have to remember to unlock!!!

```c++
#include <mutex>
#include <queue>

class threadSafe_queue {

    std::queue<int> rawQueue; // shared structure between all threads
    std::mutex m; // rawQueue's red door

public:

    int& retrieve_and_delete() {
        int front_value = 0; // if empty return 0
        m.lock();
        // From now on, the current thread is the only one that can access rawQueue
        if( !rawQueue.empty() ) {
            front_value = rawQueue.front();
            rawQueue.pop();
        }
        m.unlock();
        // other threads can lock the mutex now
        return front_value;
    };

    void push(int val) {
        m.lock();
        rawQueue.push(val);
        m.unlock();
    };

};
```

### Lock Guard
* Wrapper around mutex, but allows automatic unlocking when lock guard goes out of scope
* Example of thread safe queue with lock guard
```c++
#include <mutex>
#include <queue>

class threadSafe_queue {

    std::queue<int> rawQueue; // shared structure between all threads
    std::mutex m; // rawQueue's red door

public:

    int& retrieve_and_delete() {
        int front_value = 0; // if empty return 0
        std::lock_guard<std::mutex> lg(m);
        // From now on, the current thread is the only one that can access rawQueue
        if( !rawQueue.empty() ) {
            front_value = rawQueue.front();
            rawQueue.pop();
        }
        return front_value;
    };  // other threads can lock the mutex now

    void push(int val) {
        std::lock_guard<std::mutex> lg(m);
        // from now on, the current thread is the only one that can access rawQueue
        rawQueue.push(val);
    }; // other threads can lock the mutex now
};
```

### Unique Lock
* Combination of simpel mutex and lock guard
* Allows manual lock/unlock, but still unlock when going out of scope
```c++
#include <mutex>
#include <vector>
std::mutex door; //mutex declaration
std::vector<int> v;
{     
     std::unique_lock<std::mutex> ul(door); 
     // ul Constructor called. Equivalent to door.lock();
     // ul allocated on the stack
     // unique ownership of vector guaranteed  
    
     door.unlock();  
   
     // execution of operations that don't concern the vector
     // ....
     // now I need to access the vector again 
     
     door.lock();     
     // Unique ownership of vector guaranteed again
} /* unique_lock exits its scope. Destructor called. 
  Equivalent to door.unlock(); */
```



