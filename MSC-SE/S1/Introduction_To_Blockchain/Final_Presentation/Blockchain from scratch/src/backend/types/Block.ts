interface Block {
  index: number;
  data: string;
  hash: string;
  nonce: number;
  previousHash: string;
  timestamp: string;
}

export { Block };
