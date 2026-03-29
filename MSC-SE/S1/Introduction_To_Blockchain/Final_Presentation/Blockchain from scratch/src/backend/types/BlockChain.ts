import { Block } from "./Block.ts";

interface BlockChain {
  chain: Block[];
  difficulty: number;
  createNewBlock(input: { data: string }): void;
  mineBlockAt(blockNumber: number): Block;
  updateBlockData(blockNumber: number, newData: string): Block;
  getValidityPerBlock(): Array<{ blockNumber: number; valid: boolean }>;
  isBlockChainValid(): boolean;
}

export { BlockChain };
