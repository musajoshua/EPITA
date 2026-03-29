import type { Block } from "./../../../backend/types/Block";
import { shorten } from "./../utils/shorten";
import { InfoRow } from "./InfoRow";

type Props = {
  block: Block;
  isValid: boolean;
  difficulty: number;
  draftValue: string;
  onChangeData: (blockNumber: number, value: string) => void;
  onMine: (blockNumber: number) => void;
};

export function BlockCard({
  block,
  isValid,
  difficulty,
  draftValue,
  onChangeData,
  onMine,
}: Props) {
  return (
    <div
      className={[
        "rounded-xl border p-4",
        isValid
          ? "border-emerald-500/40 bg-emerald-500/5"
          : "border-rose-500/40 bg-rose-500/5",
      ].join(" ")}
    >
      <div className="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
        <div className="flex items-center gap-3">
          <div className="text-lg font-semibold">Block #{block.index}</div>
          <span
            className={[
              "rounded-full px-2 py-0.5 text-xs font-semibold",
              isValid
                ? "bg-emerald-500/15 text-emerald-300"
                : "bg-rose-500/15 text-rose-300",
            ].join(" ")}
          >
            {isValid ? "VALID" : "INVALID"}
          </span>
        </div>

        <button
          onClick={() => onMine(block.index)}
          className="rounded-lg bg-slate-800 px-4 py-2 text-sm font-semibold hover:bg-slate-700"
        >
          Mine block
        </button>
      </div>

      <div className="mt-4 grid gap-4 md:grid-cols-2">
        <div className="space-y-2">
          <div className="text-xs font-semibold text-slate-400">Data</div>
          <textarea
            value={draftValue}
            onChange={(e) => onChangeData(block.index, e.target.value)}
            rows={4}
            className="w-full rounded-lg border border-slate-800 bg-slate-900 p-3 text-sm text-slate-100 outline-none focus:border-slate-600"
          />
          <div className="text-xs text-slate-500">Debounced: 1000ms</div>
        </div>

        <div className="space-y-2">
          <div className="grid gap-3">
            <InfoRow label="Timestamp" value={block.timestamp} />
            <InfoRow label="Nonce" value={String(block.nonce)} mono />
            <InfoRow label="Previous hash" value={shorten(block.previousHash)} mono />
            <InfoRow label="Hash" value={shorten(block.hash)} mono />
          </div>

          <div className="mt-2 text-xs text-slate-500">
            Target: hash starts with{" "}
            <span className="font-mono">{`"${"0".repeat(difficulty)}"`}</span>
          </div>
        </div>
      </div>
    </div>
  );
}
