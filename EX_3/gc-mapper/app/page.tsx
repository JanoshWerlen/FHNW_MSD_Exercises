"use client";

import { FormEvent, useMemo, useState } from "react";

type GcResult = {
  id: string;
  gc: number;
};

function parseFasta(input: string): GcResult[] {
  const records: GcResult[] = [];
  const trimmed = input.trim();

  if (!trimmed) return records;

  const lines = trimmed.split(/\r?\n/);
  let currentId = "sequence";
  let currentSeq = "";

  for (const line of lines) {
    if (line.startsWith(">")) {
      if (currentSeq) {
        records.push({ id: currentId, gc: computeGc(currentSeq) });
      }
      currentId = line.slice(1).trim() || "sequence";
      currentSeq = "";
      continue;
    }

    currentSeq += line.trim();
  }

  if (currentSeq) {
    records.push({ id: currentId, gc: computeGc(currentSeq) });
  }

  return records;
}

function computeGc(sequence: string) {
  const upper = sequence.toUpperCase();
  const gcCount = (upper.match(/[GC]/g) ?? []).length;
  return upper.length === 0 ? 0 : (100 * gcCount) / upper.length;
}

export default function Home() {
  const [input, setInput] = useState(
    ">example\nACGTACGTGGCC"
  );
  const [results, setResults] = useState<GcResult[]>(() => parseFasta(">example\nACGTACGTGGCC"));
  const [error, setError] = useState("");

  const resultText = useMemo(() => {
    if (!results.length) return "No FASTA records found.";
    return results.map((r) => `${r.id}: ${r.gc.toFixed(6)} %`).join("\n");
  }, [results]);

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    try {
      const parsed = parseFasta(input);
      if (!parsed.length) {
        setResults([]);
        setError("Please enter a FASTA record starting with '>' and at least one sequence line.");
        return;
      }

      setResults(parsed);
      setError("");
    } catch {
      setResults([]);
      setError("Unable to process input.");
    }
  }

  return (
    <div className="min-h-screen bg-zinc-50 px-6 py-10 font-sans dark:bg-black">
      <main className="mx-auto flex w-full max-w-3xl flex-col gap-6 rounded-2xl bg-white p-8 shadow-sm ring-1 ring-zinc-200 dark:bg-zinc-950 dark:ring-zinc-800">
        <div>
          <h1 className="text-3xl font-semibold tracking-tight text-zinc-900 dark:text-zinc-50">
            GC mapper
          </h1>
          <p className="mt-2 text-sm text-zinc-600 dark:text-zinc-400">
            Paste a FASTA record and submit it to run the GC computation.
          </p>
        </div>

        <form className="space-y-4" onSubmit={handleSubmit}>
          <label className="block text-sm font-medium text-zinc-700 dark:text-zinc-300" htmlFor="fasta">
            FASTA input
          </label>
          <textarea
            id="fasta"
            name="fasta"
            className="min-h-44 w-full rounded-xl border border-zinc-300 bg-white px-4 py-3 font-mono text-sm text-zinc-900 outline-none transition focus:border-zinc-500 dark:border-zinc-700 dark:bg-zinc-900 dark:text-zinc-100"
            value={input}
            onChange={(event) => setInput(event.target.value)}
            placeholder={">seq1\nACGTACGT"}
          />

          <button
            type="submit"
            className="inline-flex items-center rounded-full bg-zinc-900 px-5 py-2.5 text-sm font-medium text-white transition hover:bg-zinc-700 dark:bg-zinc-100 dark:text-zinc-950 dark:hover:bg-white"
          >
            Submit
          </button>
        </form>

        <section className="space-y-2">
          <h2 className="text-sm font-semibold uppercase tracking-wide text-zinc-500 dark:text-zinc-400">
            Result
          </h2>
          {error ? (
            <p className="rounded-xl bg-red-50 px-4 py-3 text-sm text-red-700 dark:bg-red-950 dark:text-red-200">
              {error}
            </p>
          ) : (
            <pre className="whitespace-pre-wrap rounded-xl bg-zinc-100 px-4 py-3 font-mono text-sm text-zinc-900 dark:bg-zinc-900 dark:text-zinc-100">
              {resultText}
            </pre>
          )}
        </section>
      </main>
    </div>
  );
}


