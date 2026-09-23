# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Exam-prep workspace for a CSE undergrad (SUST). One folder per course. There is no build, no test suite, no app. The "code" is small Python drills and generated study notes. The user is a self-described beginner in Python who learns best by writing the code themselves and getting checked.

- `CE/` — Communication Engineering (Forouzan, *Data Communications and Networking* 5e, chapters 1–4). Theory midterm and a Python lab exam are both done.
- `ML/` — CSE 475 Machine Learning. Notes, worked numericals, past papers under `ML/Questions/`.
- A DSP course (a separate repo at `C:\Users\adib\Desktop\DSP-tales`) shares the same study style; the user references its `study/00-battle-plan.md` as the model for how these sessions should run.

## How study sessions work here (the part that matters)

The user calls it "the DataCamp experience". The pattern that worked:

1. **One file per step, each with a skeleton, a `# TODO`, and a checker at the bottom that prints `PASS` or `FAIL` with the expected value.** See `CE/practice/step1_nrz_l.py` through `step6_plot.py`, `lab1_step*.py`, `pcm_drill.py`.
2. The user edits the file and runs it. Claude reads the file, runs it, and gives **hints, not the answer** ("help without touching code" is a standing request). Only rewrite a file if the user asks.
3. When the user solves something a different way than the skeleton intended, check whether it's actually correct before "fixing" it. Their differential Manchester (`level` = end-of-bit level, flip on 1, `extend([-level, level])`) is correct and cleaner than the textbook version.
4. After the drills, produce a cheat sheet in `<course>/study/` (markdown) and, for anything visual, a claude.ai artifact they can open on a phone.
5. Always give a "doomsday" fallback: the fewest lines that still earn marks (e.g. `CE/practice/step6_plot_doomsday.py`).

Mark everything against the actual mark scheme from the lab sheet or past paper when one exists; the user asks "how fkd am I" and wants a per-item table.

## Running things

```
python CE/practice/<file>.py            # every drill runs standalone from repo root
python CE/practice/lab1_q1_mp3.py       # expects CE/saint.mp3 relative to repo root
```

- Python 3.13, matplotlib 3.10, numpy available. The exam environment is Google Colab, so prefer code that also works there (`plt.show()`, no `__file__` tricks in exam-facing snippets).
- To run a plotting script headless for checking, swap `plt.show()` for `savefig` via `exec` rather than editing the file:
  `python -c "import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt; exec(open('CE/practice/x.py').read().replace('plt.show()','plt.savefig(\"out.png\")'))"`
- Scripts that call `input()` can be driven with `echo 10110010 | python ...`.
- `ax.stairs()` needs matplotlib ≥ 3.4. The hand-built `steps()` t/y version is the fallback for old installs.

## Environment quirks

- **Bash heredocs (`<<'EOF'`) with long bodies fail on this machine** ("unexpected EOF while looking for matching `''`"). Use the Write tool for any multi-line file, then run it with Bash.
- The PDF/txt extractions in `CE/` (`ch*.txt`, `soln_extracted.txt`) are page-tagged text dumps of the textbook and a past paper; `CE/study/figs/` holds rendered figure crops referenced from the notes.
- The repo lives in OneDrive; file-changed notices mid-session are normal.

## Layout worth knowing

- `CE/study/00-battle-plan.md` — the schedule/weighting doc for the theory exam; the past-paper-to-textbook-example mapping there is the key finding.
- `CE/study/05-lab2-linecoding-python.md`, `06-lab1-delays-encapsulation-python.md` — the lab cheat sheets.
- `CE/Lab 1.ipynb`, `CE/Lab 2.ipynb` — the instructor's lab notebooks (Colab). Lab 1 = delays/encapsulation/bit stuffing; Lab 2 = NRZ-L, NRZ-I, Manchester, differential Manchester with plots. Conventions in the notebooks match Forouzan Fig 4.6/4.8 exactly.
- `CE/practice/fee-amanillah.py` — the user's from-memory Lab 2 solution; the reference for what they can reproduce unaided.
- Artifact for Lab 2 (waveform ↔ code map): https://claude.ai/artifact/5t2wLjhCZXN7n8RoQVMdu5
