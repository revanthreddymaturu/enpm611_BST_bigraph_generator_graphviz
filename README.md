# Binary Search Tree Generator

This Python script generates a Binary Search Tree (Bigraph) in Graphviz syntax using a list of requirements priorities as input. The script takes the priority list, where the first element is considered as the priority of Requirement 1, and constructs a complete Bigraph representing the priorities(A lower priority number means higher ranking).

## Usage

1. Clone the repository or download the script.
2. Open the Python script in a text editor or an IDE.
3. Modify the `requirements` list variable with your own priorities in comma-separated values.
4. Run the script.
5. Copy the output and go to https://dreampuf.github.io/GraphvizOnline/ and paste it there to generate the bigraph or BST.

The script will generate a complete Binary Search Tree representing the priorities in Graphviz syntax. 

## Example

```python
requirements = [6,8,10,9,3,5,4,7,2,1] #(Requirement #10 being the highest priority with priority value 1 and Requirement #3 being the lowest priority with priority value 10)
```
![image](https://github.com/revanthreddymaturu/enpm611_BST_bigraph_generator_graphviz/assets/49469625/ed0b87f5-cbf5-49e8-9b29-9a812bba962d)


## Customization
You can customize the script to make any user story as the root node by changing the index of the root variable.

## Contribution
Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## Acknowledgments
Inspired by the need to automatically generate Binary Search Trees from priority lists.
Built with Python
