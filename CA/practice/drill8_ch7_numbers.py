# DRILL 8: Chapter 7 quiz, numbers + one-word concepts
#
#   Amdahl:  speed-up = 1 / ((1 - F) + F / P)
#   exec time after = parallel_time / P + serial_time
#   Ring: total = P, bisection = 2.   Fully connected: total = P(P-1)/2, bisection = (P/2)^2
#   Crossbar = n^2 switches, Omega = 2 n log2(n)
#   Roofline: attainable = min(BW x AI, peak)   ridge point AI = peak / BW
from cachelib import check, score

# --- Amdahl & scaling ---
q1_max_sequential_percent_for_90x_on_100 = None   # in percent, e.g. 5 for 5%
q2_speedup_10x10_on_10 = None
q2_speedup_10x10_on_100 = None
q2_speedup_100x100_on_10 = None
q2_speedup_100x100_on_100 = None
q3_speedup_one_proc_2_percent = None             # 100x100 on 100 procs, one proc has 2% of the load
q3_speedup_one_proc_5_percent = None
q4_procs_for_4x_if_80_percent_parallel = None     # (old final)
q5_memory_advantage_ratio = None                  # 20 GB SMP vs 5 x 4 GB cluster, OS = 1 GB

# --- Networks ---
q6_ring16_total = None
q6_ring16_bisection = None
q6_fc16_total = None
q6_fc16_bisection = None
q7_crossbar8_switches = None
q7_omega8_switches = None
q8_ncube_n3_nodes = None

# --- Roofline ---
q9_ai_0_5 = None        # peak 16 GFLOP/s, BW 16 GB/s, arithmetic intensity 0.5 -> attainable GFLOP/s
q9_ai_4 = None          # same machine, AI 4
q9_ridge = None         # ridge point AI of that machine
q10_ai_2_on_74_peak_16_bw = None   # (new) peak 74, BW 16, AI 2

# --- GPU / vector numbers ---
q11_8800gtx_peak_gflops = None   # 16 MPs x 8 SPs x 2 FLOPs x 1.35 GHz
q12_warp_size = None
q12_max_threads_per_block = None
q13_daxpy_mips_instructions = None   # roughly
q13_daxpy_vector_instructions = None

# --- One-word concepts (lowercase) ---
q14_switches_every_cycle = None        # "fine", "coarse" or "smt"
q14_switches_on_l2_miss = None
q14_issues_from_many_threads_same_cycle = None
q15_misd_examples = None               # "none" or a chip name
q16_flynn_class_of_x86_sse = None      # "sisd" "simd" "misd" "mimd"
q16_flynn_class_of_multicore = None
q17_strong_scaling_problem_size = None # "fixed" or "grows"
q18_gpu_dram_optimized_for = None      # "latency" or "bandwidth"
q19_only_strong_scaling_benchmark = None   # "linpack" "specrate" "splash" "nas" "parsec"


# ---------------- checker ----------------
check("Q1 sequential %", q1_max_sequential_percent_for_90x_on_100, 0.1, tol=0.15)
check("Q2 10x10 on 10", q2_speedup_10x10_on_10, 5.5)
check("Q2 10x10 on 100", q2_speedup_10x10_on_100, 10.0)
check("Q2 100x100 on 10", q2_speedup_100x100_on_10, 9.9)
check("Q2 100x100 on 100", q2_speedup_100x100_on_100, 91.0)
check("Q3 2% load", q3_speedup_one_proc_2_percent, 48.0, tol=0.02)
check("Q3 5% load", q3_speedup_one_proc_5_percent, 20.0, tol=0.03)
check("Q4 procs", q4_procs_for_4x_if_80_percent_parallel, 16)
check("Q5 ratio", q5_memory_advantage_ratio, 1.25, tol=0.02)
check("Q6 ring total", q6_ring16_total, 16)
check("Q6 ring bisection", q6_ring16_bisection, 2)
check("Q6 FC total", q6_fc16_total, 120)
check("Q6 FC bisection", q6_fc16_bisection, 64)
check("Q7 crossbar", q7_crossbar8_switches, 64)
check("Q7 omega", q7_omega8_switches, 48)
check("Q8 n-cube nodes", q8_ncube_n3_nodes, 8)
check("Q9 AI 0.5", q9_ai_0_5, 8.0)
check("Q9 AI 4", q9_ai_4, 16.0)
check("Q9 ridge", q9_ridge, 1.0)
check("Q10", q10_ai_2_on_74_peak_16_bw, 32.0)
check("Q11 GTX peak", q11_8800gtx_peak_gflops, 345.6)
check("Q12 warp", q12_warp_size, 32)
check("Q12 block", q12_max_threads_per_block, 512)
check("Q13 MIPS ~", q13_daxpy_mips_instructions, 600.0, tol=0.05)
check("Q13 vector", q13_daxpy_vector_instructions, 6)
check("Q14 every cycle", q14_switches_every_cycle, "fine")
check("Q14 on L2 miss", q14_switches_on_l2_miss, "coarse")
check("Q14 same cycle", q14_issues_from_many_threads_same_cycle, "smt")
check("Q15 MISD", q15_misd_examples, "none")
check("Q16 SSE", q16_flynn_class_of_x86_sse, "simd")
check("Q16 multicore", q16_flynn_class_of_multicore, "mimd")
check("Q17 strong", q17_strong_scaling_problem_size, "fixed")
check("Q18 GPU DRAM", q18_gpu_dram_optimized_for, "bandwidth")
check("Q19 strong benchmark", q19_only_strong_scaling_benchmark, "splash")
score()
