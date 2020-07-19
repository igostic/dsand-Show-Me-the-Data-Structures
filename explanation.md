## Explanation to Problems

## 1. Explanation LRU caching exercise
Is basically a Linked List backed by a Hash table -> why?
* we needed fast look up (that is what a hash table was needed)
* we needed order and fast insertion (The necessity of a linked list)
Then Each node was being saved with the reference to the next and previous one into
the hash table, in that way we are able to look at a node without going through all
the linked list
Time and space complexity 
 * get --->  Time O(1), Space O(1) -> Our dictionary can access easily
 * set --->  Time O(1), Space O(1) -> We can add a new entry in O(1) thanks to self.head
 

## 2. Explanation File recursion exercise

Was easy, just iterate among each directory and each sub directory with a list filtering
files with the extension required

Time and Space complexity:
* Time O(n * m) -> Because per each initial folder we need to iterate among all the things inside(other variable thats m)
* Space O(n * m) -> We need an array of size m for each folder (n)


## 3. Explanation Huffman Coding exercise
```Note: This fucking exercise was amazing, took me like 2 or 3 days of thinking and a lot of research and keyboards, but finally I made it work :) Feels great```


### How I did it?
I made a lot of visualization, also hand crafted ones, and then I found a pattern, not sure if that
is how is in the books or is the pro way (I found one on my own).

* Frequencies array created and sorted and Nodes(Frequency, Char)
* on the lower frequencies making pairs of nodes and creating  a bunch of trees
* if n_of_frequencies % 2 != 0 -> take already created trees and append it to the tree
* with the rest of the frequencies
    - each (frequency, char) is added to a one of each of the trees created previously
    - if len of this frequencies > len trees -> new trees are created in pairs and appended to trees

* at the end with a bunch of trees and all chars in right position
    - sort trees based on root node value reversed
    - append trees 1 .. n to tree 0
    - ENCODING TREE BUILT
    
    
Time and Space complexity:
* Encoding
```
def huffman_encoding(data):
    trees = []

    # sort -> logn -> Counter ( Space O(n), Time O(n)) ---> build frequencies arr costs O(nlogn)
    frequencies = [Pair(freq, char) for char, freq in Counter(sorted(data)).items()]

    # O(f) -> f set of different amounts of frequencies
    # Worst case all different so forget O(f) exists ---> Just O(n)
    while len(frequencies) > 0:

        # O(2n) -> O(n) n = chars in data
        lowest_freq_pairs, frequencies = lowest_frequencies(frequencies)

        if len(trees) == 0:
            # All different frequencies, so here there is only 1 frequency O(1)
            create_subtrees_in_pairs(trees, lowest_freq_pairs)
        else:
            # only 1 frequency  in lowest_freq_pairs, and trees always len 1 --> O(1)
            add_one_freq_to_each_tree(trees, lowest_freq_pairs)

    # trees here len = 1 so cost is O(1)
    final_tree = build_final_tree_from_trees(trees)  
    # O(n) iterate over each char -> and get char encoded recursively takes O(n) --> O(n^2)
    data_encoded = get_encoded_data(final_tree.root, data)  

    return data_encoded, final_tree
```

This give us --> O(nlogn) + O(n * n) + O(n ^ 2) --> O(nlogn + 2*n^2) --> O(n^2)




* Decoding

```
def find_char_from_path(path, node):
    # This recursive function also takes O(n)
    if node:
        if node.get_pair().char is not None:
            return node.get_pair().char

        if len(path) > 0:
            direction = path[0]
            char = None
            if direction == "0":
                char = find_char_from_path(path[1:], node.left)
            elif direction == "1":
                char = find_char_from_path(path[1:], node.right)

            return char


def huffman_decoding(data, codified_tree):
    # Iterate over each "char" in data O(n)
    return ''.join([find_char_from_path(path, codified_tree.root) for path in data.split()])

```
  Decoding give us -> O(n * n) -> O(n^2)


## 4. Explanation Active directory exercise

Almost the same as File recursion, the difference here is that we had to check 
if a list contains something and return true or false

Time and Space Complexity:
* O (n * m) -> iterating among m times per each n initial group
* Space -> O(n) -> being n the max recursion depth in the initial group


## 5. Explanation Blockchain exercise
"A Blockchain is a sequential chain of records, similar to a linked list." ->
That made me think about off course a linked list off course, but taking into account that is not required
to make fast deletions and insertions, only appends, an array works perfectly

Time and Space Complexity
* Append operation in arrays takes O(n) being n the number of blocks ```chain = [Block(0, datetime.now(), "First Block", "0")]```


## 6. Explanation BlockChain exercise
* Union -> just iterate over both list, and add each node to a new LinkedList
* Intersection -> Iterate Over List2 1 time per item in list1, check whether or 
not an item of list 1 exists in list 2, if True -> append to a new linked list

Time and Space complexity:
* Union -> O(n + m) being n list1, m list2
* Intersection -> O (n + m + p) being n list1, m list2, p (append to intersected list)
