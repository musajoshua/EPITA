import { useEffect, useMemo, useReducer, useState } from "react";
import { Blockchain } from "./../../backend/blockchain";
import type { Block } from "./../../backend/types/Block";
import { useDebouncedValue } from "./hooks/useDebouncedValue";
import { ChainHeader } from "./components/ChainHeader";
import { BlockCard } from "./components/BlockCard";

export default function App() {
  const [bc] = useState(() => new Blockchain(4));
  const [tick, force] = useReducer((x) => x + 1, 0);

  const chain = bc.chain;

  const [draftByBlock, setDraftByBlock] = useState<Record<number, string>>({});
  const debouncedDraftByBlock = useDebouncedValue(draftByBlock, 1000);

  // Apply debounced edits into the blockchain (mutates chain) then rerender
  useEffect(() => {
    let changed = false;

    for (const [k, v] of Object.entries(debouncedDraftByBlock)) {
      const blockNumber = Number(k);
      const block = chain.find((b) => b.index === blockNumber);
      if (!block) continue;

      if (v !== block.data) {
        bc.updateBlockData(blockNumber, v);
        changed = true;
      }
    }

    if (changed) force();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [debouncedDraftByBlock]);

  const validity = useMemo(() => bc.getValidityPerBlock(), [tick]);
  const overallValid = bc.isBlockChainValid();
  const validMap = useMemo(
    () => new Map(validity.map((v) => [v.blockNumber, v.valid])),
    [validity],
  );

  function addBlock() {
    bc.createNewBlock({ data: "New block data..." });
    force();
  }

  function onChangeData(blockNumber: number, value: string) {
    setDraftByBlock((prev) => ({ ...prev, [blockNumber]: value }));
  }

  function onMine(blockNumber: number) {
    bc.mineBlockAt(blockNumber);

    // keep textarea aligned with chain after mining
    const mined = bc.chain.find((b) => b.index === blockNumber);
    if (mined) {
      setDraftByBlock((prev) => ({ ...prev, [blockNumber]: mined.data }));
    }

    force();
  }

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100">
      <div className="mx-auto max-w-6xl p-6">
        <ChainHeader overallValid={overallValid} onAddBlock={addBlock} />

        <div className="mt-6 grid gap-4">
          {chain.map((block: Block) => {
            const isValid = validMap.get(block.index) ?? false;
            const draftValue = draftByBlock[block.index] ?? block.data;

            return (
              <BlockCard
                key={block.index}
                block={block}
                isValid={isValid}
                difficulty={bc.difficulty}
                draftValue={draftValue}
                onChangeData={onChangeData}
                onMine={onMine}
              />
            );
          })}
        </div>
      </div>
    </div>
  );
}
