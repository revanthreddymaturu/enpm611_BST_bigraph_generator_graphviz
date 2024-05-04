# Binary Search Tree Generator

This Python script generates a Binary Search Tree (Bigraph) in Graphviz syntax using a list of requirements priorities as input. The script takes the priority list, where the first element is considered the highest priority, and constructs a complete Bigraph representing the priorities.

## Usage

1. Clone the repository or download the script.
2. Open the Python script in a text editor or an IDE.
3. Modify the `requirements` list variable with your own priorities in comma-separated values.
4. Run the script.
5. Copy the output and go to https://dreampuf.github.io/GraphvizOnline/ and paste it there to generate the bigraph or BST.

The script will generate a complete Binary Search Tree representing the priorities in Graphviz syntax. 

## Example

```python
requirements = [6,8,10,9,3,5,4,7,2,1] #(6 being the highest priority and 1 being the lowest)
```
 ![image](https://github.com/revanthreddymaturu/enpm611_BST_bigraph_generator_graphviz/assets/49469625/5be805e5-0076-4a1a-8b06-5fefc8e22aa9)

## Customization
You can customize the script to make any user story as the root node by changing the index of the root variable.
Ensure the input list is sorted in ascending order for the Binary Search Tree to be constructed correctly.

## Contribution
Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## Acknowledgments
Inspired by the need to automatically generate Binary Search Trees from priority lists.
Built with Python
