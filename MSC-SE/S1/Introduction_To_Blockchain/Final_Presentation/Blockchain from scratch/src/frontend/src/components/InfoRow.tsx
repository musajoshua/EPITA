type Props = {
  label: string;
  value: string;
  mono?: boolean;
};

export function InfoRow({ label, value, mono }: Props) {
  return (
    <div className="rounded-lg border border-slate-800 bg-slate-900 p-3">
      <div className="text-xs font-semibold text-slate-400">{label}</div>
      <div className={["mt-1 text-sm", mono ? "font-mono" : ""].join(" ")}>
        {value}
      </div>
    </div>
  );
}
