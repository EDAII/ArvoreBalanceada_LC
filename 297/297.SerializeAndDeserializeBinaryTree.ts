// 297. Serialize and Deserialize Binary Tree
// Abordagem: DFS pré-ordem com marcador 'N' para nulos

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

export function serialize(root: TreeNode | null): string {
  const out: string[] = [];

  function dfs(node: TreeNode | null): void {
    if (node === null) {
      out.push("N");
      return;
    }

    // adiciona o valor do nó atual
    out.push(String(node.val));

    dfs(node.left);
    dfs(node.right);
  }

  dfs(root);
  return out.join(",");
}

export function deserialize(data: string): TreeNode | null {
  if (!data) return null;
  const tokens = data.split(",");
  let i = 0;

  function build(): TreeNode | null {
    const tok = tokens[i++];
    if (tok === "N") return null;

    // cria o nó com o valor atual
    const node = new TreeNode(Number(tok));
    // constrói os filhos recursivamente em pré-ordem
    node.left = build();
    node.right = build();
    return node;
  }

  // inicia a reconstrução e retorna o nó raiz
  return build();
}
