// Node structure
class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// Function to perform inorder traversal using stack
function inorderTraversal(root) {
  let stack = [];
  let current = root;
  let result = []; // To store the inorder traversal result

  while (current !== null || stack.length > 0) {
    // Reach the leftmost node of the current node
    while (current !== null) {
      stack.push(current);  // Push the current node to the stack
      current = current.left;  // Move to the left child
    }

    // Current must be null at this point, so pop the top of the stack
    current = stack.pop();
    result.push(current.value);  // Process the current node

    // Now visit the right subtree
    current = current.right;
  }

  return result;  // Return the inorder traversal result
}

// Example usage
const root = new TreeNode(1);
root.right = new TreeNode(2);
root.right.left = new TreeNode(3);

console.log("Inorder Traversal:", inorderTraversal(root));
