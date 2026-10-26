# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Exam-prep workspace for a CSE undergrad (SUST). One folder per course. There is no build, no test suite, no app. The "code" is small Python drills and generated study notes. The user is a self-described beginner in Python who learns best by writing the code themselves and getting checked.

- `CE/` — Communication Engineering (Forouzan, *Data Communications and Networking* **5e**). Mid-term 1 (ch 1–4) and the Python lab exam are done. Mid-term 2 + quiz covers ch **5, 6, 7, 8, 10, 11** and was set for 2026-10-05; its material is `CE/study/10-*` to `15-*`.
- `ML/` — CSE 475 Machine Learning. Notes, worked numericals, past papers under `ML/Questions/`.
- `DSP/` — CSE 0714 3276 DSP. `DSP/practice/` holds the lab-exam drills `step1` to `step9` in the same skeleton-plus-checker style. `DSP/study/` holds the Mid-2 set (exam Sun 2026-10-11 10:00; updated syllabus = Mitra 4.8–4.8.7 as Quiz Q1, Proakis ch 3 and ch 4 as TT2; ch 5 and ch 7 DFT/FFT were dropped): `00-mid2-battle-plan.md` and `20-*` to `24-*`, in LaTeX. They are typeset for the phone as the artifact "DSP Mid-2 Notes", https://claude.ai/artifact/NR1NcgWMjgyLmYUKjiWVvD, built by `_build_mid2_notes.js` (run instructions in its header) into `mid2-notes.html`. Figures live in `DSP/study/figs/*.svg`, drawn by `_make_pz_figs.py`; the build inlines them, and a `<!-- widget:pole-explorer -->` comment in the markdown becomes the interactive pole explorer. `lab-doomsday.md` is the lab-exam sheet. The pre-update files (`00-tt2-battle-plan.md`, tutorials `10-*` to `13-*` on DTFT/z/DFT/FIR, `midterm-2-tutorial.md`) were deleted on 2026-10-10 at the user's request; they are in git history before that date. Syllabus notices are `DSP/midterm-2.txt.txt` (mid 2) and `DSP/DSP.md` (everything after mid 1). The older theory notes live in a separate repo, `C:\Users\adib\Desktop\DSP-tales`, whose `study/00-battle-plan.md` is the model for how sessions run. On 2026-10-04 the user asked for a reorganisation of `DSP/` and then cancelled it, so don't restructure it unless asked again.
- `CA/` — CSE 329 Computer Architecture (Patterson & Hennessy 4e, `CA/Resources/MK...pdf`; book page = PDF page − 27). The syllabus is the professor's 10 lecture decks in `CA/Resources/` (L1 Ch1, L2 Ch2, L3–5 Ch5, L6 numbers/IEEE, L7–8 Ch4 pipelining + ILP, L9 Ch7 §7.1–7.6, L10 Ch6 I/O). Past papers are in `CA/Final question/` (the two 2024 finals, sessions 2020-21 and 2021-22, share questions word for word with the 2025–26 term tests; older 2018–20 papers are a different examiner) plus `CA/Tt/` and `CA/Term Test/`. For the final (Oct 2026): `CA/study/10-ch7-final.md` is the 4–6 h Ch 7 file, and the artifact "CSE 329 Final Kit" (all lectures, every past question solved, calculators) is https://claude.ai/artifact/3fPxbeH5mKLstj9aPRjyd1 with source copy `CA/study/11-final-kit.html`. Its calculation logic was tested in Node against every past-paper answer. On 2026-10-27 the user had the Ch 7 quiz notes deleted (`03-ch7-quiz.md`, `03a-ch7-from-zero.md`, `drill8`, trick-bank Part C; in git history). `CA/study/00`–`04` and `CA/practice/drill1–7` are the older TT2 midterm material; the TT2 artifact is https://claude.ai/artifact/1t9uxu7wGe6GBRCoHhmwAq.
- `comp-architecture/` — a separate older git repo (Ch 1–2 cram notes for TT1); the live CA work is in `CA/`.

## How study sessions work here (the part that matters)

The user calls it "the DataCamp experience". The pattern that worked:

1. **One file per step, each with a skeleton, a `# TODO`, and a checker at the bottom that prints `PASS` or `FAIL` with the expected value.** See `CE/practice/step1_nrz_l.py` through `step6_plot.py`, `lab1_step*.py`, `pcm_drill.py`, and `DSP/practice/step*.py`.
2. The user edits the file and runs it. Claude reads the file, runs it, and gives **hints, not the answer** ("help without touching code" is a standing request). Only rewrite a file if the user asks.
3. When the user solves something a different way than the skeleton intended, check whether it's actually correct before "fixing" it. Their differential Manchester (`level` = end-of-bit level, flip on 1, `extend([-level, level])`) is correct and cleaner than the textbook version.
4. After the drills, produce a cheat sheet in `<course>/study/` (markdown) and, for anything visual, a claude.ai artifact they can open on a phone.
   **Write all maths in study markdown as LaTeX** (`$...$` inline, `$$` on their own lines for display), never Unicode pseudo-maths like `e^{jωn}` or `|z| > |a|` in plain text. In tables use `\lvert ... \rvert`, because a bare `|` splits the cell. Write the prose as full, plain sentences that explain the idea, not clipped fragments with arrows and ticks. On 2026-10-10 the user said the old style was hard to follow and "oddly machinery". The VS Code preview (`Ctrl+Shift+V`) typesets it with KaTeX; `DSP/study/.vscode/markdown.css` sets the fonts and the three `.vscode/settings.json` files (repo root, `DSP/`, `DSP/study/`) point the preview at it.
5. Always give a "doomsday" fallback: the fewest lines that still earn marks (e.g. `CE/practice/step6_plot_doomsday.py`).

Mark everything against the actual mark scheme from the lab sheet or past paper when one exists; the user asks "how fkd am I" and wants a per-item table.

### Theory exam tomorrow, nothing studied (what worked for CE mid-term 2)

- **Map the past papers to the textbook first.** This CE teacher copies Forouzan's end-of-chapter Questions/Problems and worked Examples almost word for word and reuses them across years. The past papers effectively are the syllabus.
- **Split chapters across parallel agents**, one study file per chapter pair, all with the same structure: what the papers ask (with years), concepts in plain English, formula box, every past question solved step by step, traps, a practice set with answers at the bottom, and a 15-minute doomsday box. Add one battle-plan file (topic frequency ranking, 12h/3h/1h schedules) and one mock paper built only from real past questions.
- **Recompute every numerical in Python** before it goes into a file, and spot-check agent output independently. Textbook and publisher answers contain errors (see Layout).
- **Explain for intuition first.** When the user says they can't picture something, give a physical picture before the formula (I/Q landed as "where a Ferris-wheel seat starts"), then the formula, then the exam answer. When ASCII diagrams stop helping, build an artifact with drawn figures and small calculators.
- Keep replies short and plain during a crunch. The user is stressed and reading on a phone.

## Running things

```
python CE/practice/<file>.py            # every drill runs standalone from repo root
python CE/practice/lab1_q1_mp3.py       # expects CE/saint.mp3 relative to repo root
python DSP/practice/<file>.py           # step4b writes and reads DSP/practice/test_tone.wav
```

- `python` here is Python 3.11, with numpy 2.4, matplotlib 3.11 and pypdf 6.14. Node 22 is available, which is handy for `node --check` on an artifact's script. The exam environment is Google Colab, so prefer code that also works there (`plt.show()`, no `__file__` tricks in exam-facing snippets). The DSP lab exam allows only numpy, matplotlib and SymPy.
- To run a plotting script headless for checking, swap `plt.show()` for `savefig` via `exec` rather than editing the file:
  `python -c "import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt; exec(open('CE/practice/x.py').read().replace('plt.show()','plt.savefig(\"out.png\")'))"`
- Scripts that call `input()` can be driven with `echo 10110010 | python ...`.
- `ax.stairs()` needs matplotlib ≥ 3.4. The hand-built `steps()` t/y version is the fallback for old installs.

## Environment quirks

- **Long Bash heredocs (`<<'EOF'`) have failed on this machine** ("unexpected EOF while looking for matching `''`"). Short `python - <<'EOF'` blocks of about 50 lines work. Use the Write tool for anything longer, then run it with Bash.
- Set `PYTHONIOENCODING=utf-8` before printing PDF text. The console is cp1252 and crashes on characters like π.
- The PDF/txt extractions in `CE/` (`ch*.txt`, `soln_extracted.txt`, `ch7_media.txt`, `ch8_switching.txt`) are text dumps of the textbook and a past paper; `CE/study/figs/` holds rendered figure crops referenced from the notes.
- A full artifact page (about 80 KB) is too big for one Write call. Write it in parts of about 15 KB and concatenate. Artifact sources live in the session scratchpad and disappear afterwards, so update an existing artifact from its URL.
- **Look at artifacts before publishing.** Chrome is at `/c/Program Files/Google/Chrome/Application/chrome.exe`; `--headless=new --screenshot=... --window-size=500,H file:///...page.html#tab` renders a page (wrap the artifact body in a doctype skeleton first). The headless window is at least ~500 px wide, so for phone checks inject `document.body.style.width="360px"`; `--dump-dom` with an injected script can report elements wider than the viewport. Node/jsdom tests do not catch layout bugs: on 2026-10-27 the CA kit shipped with superscripts split onto separate lines (inline tags inside CSS grid/flex rows) and phone overflow (grid children without `min-width:0`), and the user found both.
- The repo lives in OneDrive; file-changed notices mid-session are normal. `CE/questions` and `CE/Questions` are the same folder.

## Layout worth knowing

- `CE/study/00-battle-plan.md` — the schedule/weighting doc for the mid-term 1 theory exam; the past-paper-to-textbook-example mapping there is the key finding.
- `CE/study/05-lab2-linecoding-python.md`, `06-lab1-delays-encapsulation-python.md` — the lab cheat sheets.
- `CE/study/10-mid2-battle-plan.md` — mid-term 2 map: every ch 5–11 past question with its textbook source, topic ranking, schedules, night-before checklist.
- `CE/study/11-ch5-6-analog-and-multiplexing.md`, `12-ch7-8-media-and-switching.md`, `13-ch10-11-errors-and-dlc.md` — the chapter files. `14-mid2-mock-paper.md` is a mock from real past questions. `15-mid2-official-quizzes.md` holds the publisher's 109 MCQs with a corrected key.
- `CE/Questions/` — past papers: `Previous Year Questions/` (2014-15 to 2019-20 finals), `Term Test/` (TT-01, DataCom_TT2), `tt2/` (photos of the 28 Aug 2025 TT2, the latest paper by this teacher: 1 hour, 20 marks, answered on the question paper, mostly drawing and calculating), and `official-solutions/` (publisher solutions to odd-numbered ch 5–11 exercises).
- Publisher companion site for the 5e: https://highered.mheducation.com/sites/0073376221/sitemap.html. Each chapter has a quiz whose answer key is XOR-150 encoded in the page, and an odd-problem solutions PDF. **The quiz keys are often wrong** (7 of 109 for ch 5–11), so check every key against the book.
- Known textbook errors: Forouzan 5e Ex 8.4 prints 9500 crosspoints where the correct figure is 15,200, and Ex 6.11 and the official P6-9 solution write ms where µs is right.
- `CE/Lab 1.ipynb`, `CE/Lab 2.ipynb` — the instructor's lab notebooks (Colab). Lab 1 = delays/encapsulation/bit stuffing; Lab 2 = NRZ-L, NRZ-I, Manchester, differential Manchester with plots. Conventions in the notebooks match Forouzan Fig 4.6/4.8 exactly.
- `CE/practice/fee-amanillah.py` — the user's from-memory Lab 2 solution; the reference for what they can reproduce unaided.
- Artifact for Lab 2 (waveform ↔ code map): https://claude.ai/artifact/5t2wLjhCZXN7n8RoQVMdu5
- Artifact for CE ch 5–6, "Carriers and Channels" (drawn modulation and multiplexing figures, constellation explorer with the I/Q wheel, FDM and TDM calculators, past-paper answers): https://claude.ai/artifact/E6Puw6NPe2XbrGfx6vZTHp
- Artifact for CE ch 10–11, "Parity to PPP" (CRC long division in exam layout, checksum, Hamming distance and code, 2D parity, bit and byte stuffing, drawn Stop-and-Wait timelines, HDLC decoder, PPP phases): https://claude.ai/artifact/BtASg4eTKd8Ni1kHbbFTLB. Its calculation logic was tested in Node against every answer in `13-ch10-11-errors-and-dlc.md`.
- Artifact for the mid-term 2 quiz, "CE Mid-2 Quiz Drill" (108 tap-to-answer MCQs for ch 5, 6, 7, 8, 10 and 11 with a why line, past-paper tags, a starred fast lane, and primers for ch 7, 8 and 11): https://claude.ai/artifact/4Zb4aJuNnSjesuLZ7qUuNh. Source copy: `CE/study/16-mid2-quiz-drill.html`.
- ML artifact "Table to Network" (past-paper index for the NN-design questions, ML pipeline map, the 5-animal mammal table worked through every exam ask incl. the "simplest possible" one-neuron/step version, practice cards for the packet, weather and WeTube datasets, a network builder that draws layer sizes and counts params/data/updates, word decoder). The NN-design questions themselves are listed in `ML/fight.txt`. Data rule used: Baum–Haussler N ≈ W/ε from Haykin: https://claude.ai/artifact/1GALJB2TtduxMW7tVYvjJw. Source copy: `ML/table_to_network.html`. Rules tagged [Ranjan] come from Chitta Ranjan's "Rules-of-thumb for building a Neural Network" (Medium blocks fetching; rules confirmed from search snippets only).
- ML artifact "CNN by Hand" (the six CNN past questions from `ML/fight.txt` as think-first cards: CNN vs dense, patch counting, convolution + max pooling by hand, 8×8 CNN design with 86 parameters, plus a convolution/pooling calculator with per-patch working): https://claude.ai/artifact/XbmMKzpnTos45cAQ2fjfjM. Source copy: `ML/cnn_by_hand.html`. The F2021 Q2f convolution uses the unflipped kernel (CNN convention, answer 35 after max pooling); the flipped maths version gives 25.
- Artifact "CE Quiz Cram Sheet" (no questions, just "see this word → pick that" hooks, guess rules, publisher-key traps; unstudied ch 7, 8, 11 first): https://claude.ai/artifact/FZnV7MzLXXBLk6UTehNFaY. Source copy: `CE/study/17-mid2-quiz-cram-sheet.html`. Lesson from 2026-10-04: with under 2 hours left and chapters unstudied, the user wanted a cram list, not a quiz. A quiz assumes they already know the material.
