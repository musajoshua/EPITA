import { sha256 } from "@noble/hashes/sha2.js";
import { bytesToHex } from "@noble/hashes/utils.js";
import type { Block, BlockChain } from "./types";

export class Blockchain implements BlockChain {
  chain: Block[];
  difficulty: number;

  constructor(difficulty = 4) {
    this.chain = [];
    this.difficulty = difficulty;

    this.createNewBlock({
      data: "I am Genesis Block",
    });
  }

  private getNextIndex() {
    return this.chain.length + 1;
  }

  private sha256Hex(input: string) {
    return bytesToHex(sha256(new TextEncoder().encode(input)));
  }

  private getLastBlock() {
    return this.chain[this.chain.length - 1];
  }

  private mine(
    index: Block["index"],
    data: Block["data"],
    previousHash: Block["previousHash"],
    timestamp: Block["timestamp"],
  ) {
    let nonce = 0;
    let hash = "";

    const target = this.getTargetHash();

    while (!hash.startsWith(target)) {
      nonce++;
      const newHash = this.calculateHash({
        index,
        previousHash,
        data,
        nonce,
        timestamp,
      });
      hash = newHash;
    }

    return { nonce, hash };
  }

  private getTargetHash(numberOfZeros = this.difficulty) {
    return "0".repeat(numberOfZeros);
  }

  private calculateHash(
    block: Pick<
      Block,
      "index" | "previousHash" | "data" | "nonce" | "timestamp"
    >,
  ) {
    return this.sha256Hex(
      JSON.stringify({
        index: block.index,
        previousHash: block.previousHash,
        data: block.data,
        nonce: block.nonce,
        timestamp: block.timestamp,
      }),
    );
  }

  private getBlockByNumber(blockNumber: number) {
    const block = this.chain.find((blk) => blk.index === blockNumber);
    if (!block) throw new Error("Invalid block number");
    return block;
  }

  private getBlockPosition(blockNumber: number) {
    const i = this.chain.findIndex((b) => b.index === blockNumber);
    if (i === -1) throw new Error("Invalid block number");
    return i;
  }

  private recomputeBlockHash(blockNumber: number) {
    const i = this.getBlockPosition(blockNumber);
    const block = this.chain[i];
    block.hash = this.calculateHash(block);
  }

  private tamperWithBlock(blockNumber: number, newData: Block["data"]) {
    const block = this.getBlockByNumber(blockNumber);
    block.data = newData;
  }

  private cascadeFromBlockNumber(blockNumber: number) {
    if (blockNumber > this.chain.length) return;

    const startPos = this.getBlockPosition(blockNumber);

    for (let pos = startPos; pos < this.chain.length; pos++) {
      if (pos === 0) continue;

      this.chain[pos].previousHash = this.chain[pos - 1].hash;
      this.chain[pos].hash = this.calculateHash(this.chain[pos]);
    }
  }

  createNewBlock({ data }: { data: Block["data"] }) {
    const index = this.getNextIndex();
    const previousBlock = this.getLastBlock();
    const timestamp = new Date().toISOString();
    const previousHash = previousBlock
      ? previousBlock.hash
      : this.getTargetHash(64);

    const { nonce, hash } = this.mine(index, data, previousHash, timestamp);
    const newBlock: Block = {
      data,
      index,
      nonce,
      hash,
      timestamp,
      previousHash,
    };

    this.chain.push(newBlock);
  }

  isBlockChainValid() {
    const target = this.getTargetHash();
    for (let pos = 0; pos < this.chain.length; pos++) {
      const currentBlock = this.chain[pos];
      const previousBlock = this.chain[pos - 1];

      // First check if the previousHash matches, and is not genesis block
      if (pos !== 0 && currentBlock.previousHash !== previousBlock.hash) {
        return false;
      }

      // Now check if the hash is valid
      const recalculatedHash = this.calculateHash(currentBlock);

      if (currentBlock.hash !== recalculatedHash) {
        return false;
      }

      // Finally check the proof of work
      if (!currentBlock.hash.startsWith(target)) {
        return false;
      }
    }
    return true;
  }

  mineBlockAt(blockNumber: number) {
    const block = this.getBlockByNumber(blockNumber);

    const { nonce, hash } = this.mine(
      block.index,
      block.data,
      block.previousHash,
      block.timestamp,
    );

    block.nonce = nonce;
    block.hash = hash;

    if (blockNumber < this.chain.length) {
      this.cascadeFromBlockNumber(blockNumber + 1);
    }
    return block;
  }

  updateBlockData(blockNumber: number, newData: Block["data"]) {
    this.tamperWithBlock(blockNumber, newData);

    this.recomputeBlockHash(blockNumber);

    if (blockNumber < this.chain.length) {
      this.cascadeFromBlockNumber(blockNumber + 1);
    }
    return this.getBlockByNumber(blockNumber);
  }

  getValidityPerBlock() {
    const target = this.getTargetHash();

    return this.chain.map((block, pos) => {
      const prev = pos === 0 ? null : this.chain[pos - 1];

      const linkOk = pos === 0 ? true : block.previousHash === prev!.hash;
      const hashOk = block.hash === this.calculateHash(block);
      const powOk = block.hash.startsWith(target);

      return { blockNumber: block.index, valid: linkOk && hashOk && powOk };
    });
  }
}

const blockchain = new Blockchain(4);
// blockchain.createNewBlock({
//   data: "Test Block",
// });
// console.log(blockchain.chain);
// blockchain.createNewBlock({
//   data: "Test Block 2",
// });
// console.log(blockchain.chain);
// console.log(blockchain.isBlockChainValid());
// blockchain.updateBlockData(2, "Tampered Data");
// console.log(blockchain.chain);
// console.log(blockchain.chain);
// console.log(blockchain.isBlockChainValid());
// blockchain.updateBlockData(1, "Tampered Data");
// console.log(blockchain.chain);
// console.log(blockchain.isBlockChainValid());
