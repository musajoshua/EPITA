type Props = {
  overallValid: boolean;
  onAddBlock: () => void;
};

export function ChainHeader({ overallValid, onAddBlock }: Props) {
  return (
    <header className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
      <div>
        <h1 className="text-2xl font-semibold">Blockchain Demo</h1>
        <p className="text-sm text-slate-400">
          Edit data to break the chain. Mine to restore Proof of Work.
        </p>
      </div>

      <div className="flex items-center gap-3">
        <div
          className={[
            "rounded-full px-3 py-1 text-sm font-medium",
            overallValid
              ? "bg-emerald-500/15 text-emerald-300"
              : "bg-rose-500/15 text-rose-300",
          ].join(" ")}
        >
          {overallValid ? "Chain valid" : "Chain invalid"}
        </div>

        <button
          onClick={onAddBlock}
          className="rounded-lg bg-slate-100 px-4 py-2 text-sm font-semibold text-slate-900 hover:bg-white"
        >
          + Add block
        </button>
      </div>
    </header>
  );
}
