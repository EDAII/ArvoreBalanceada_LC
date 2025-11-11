// 124. Binary Tree Maximum Path Sum
// Abordagem: DFS pós-ordem com ganho por ramo, ignorando negativos

class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

export function maxPathSum(root: TreeNode | null): number {
  let best = -Infinity;

  function dfs(node: TreeNode | null): number {
    if (!node) return 0;

    // calcula o ganho da subárvore esquerda
    let leftGain = dfs(node.left);
    if (leftGain < 0) leftGain = 0;

    let rightGain = dfs(node.right);
    if (rightGain < 0) rightGain = 0;

    const throughNode = node.val + leftGain + rightGain;
    if (throughNode > best) best = throughNode;

    let pick = leftGain;
    if (rightGain > pick) pick = rightGain;

    // retorna o valor do nó + o melhor lado (para ser usado pelo pai)
    return node.val + pick;
  }

  dfs(root);
  return best;
}

// Exemplo rápido (comentado):
// const root = new TreeNode(-10,
//   new TreeNode(9),
//   new TreeNode(20, new TreeNode(15), new TreeNode(7))
// );
// console.log(maxPathSum(root)); // 42

