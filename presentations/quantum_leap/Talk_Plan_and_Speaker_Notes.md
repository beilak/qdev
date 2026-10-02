# Quantum Leap: Building Real Quantum Programs with Python

## Talk plan

Working assumption: 30 minutes plus 5 minutes for questions. The 18 main slides use 27 minutes 30 seconds, leaving 2 minutes 30 seconds for transitions and a slow demo. Slides 19–22 are backup material. All examples come from the five supplied notebooks and three previous presentations. External documentation only supports updates and corrections.

Audience: developers with intermediate Python. Introduce each quantum term when it first appears.

The central example is the two-qubit VQE problem, followed by its saved hardware result. Hello World establishes circuits and sampling first. Half-adder connects to familiar logic. Grover and the route model provide brief extensions.

| Time | Slide | Purpose |
|---|---|---|
| 00:00–00:30 | 1. Quantum Leap | 0.5 min |
| 00:30–01:30 | 2. A quantum program in Python | 1 min |
| 01:30–03:30 | 3. Qubits and measurement | 2 min |
| 03:30–05:00 | 4. The gates used in these notebooks | 1.5 min |
| 05:00–06:30 | 5. A half-adder | 1.5 min |
| 06:30–08:30 | 6. Hello World: three correlated qubits | 2 min |
| 08:30–10:30 | 7. Local simulation | 2 min |
| 10:30–12:00 | 8. Reading the counts | 1.5 min |
| 12:00–14:00 | 9. A two-bit optimization problem | 2 min |
| 14:00–16:00 | 10. The VQE feedback loop | 2 min |
| 16:00–17:30 | 11. VQE in the supplied notebook | 1.5 min |
| 17:30–19:00 | 12. The measured answer | 1.5 min |
| 19:00–21:30 | 13. Submitting a cloud job | 2.5 min |
| 21:30–23:00 | 14. The saved hardware result | 1.5 min |
| 23:00–24:30 | 15. Grover: increasing a target probability | 1.5 min |
| 24:30–26:00 | 16. Route optimization with QAOA | 1.5 min |
| 26:00–27:00 | 17. What these examples establish | 1 min |
| 27:00–27:30 | 18. Code and questions | 0.5 min |
| 27:30–30:00 | Buffer | Demo transitions and audience pauses |
| 30:00–35:00 | Q&A | Use backup slides as needed |

## Opening and closing

Opening: “I will build a small quantum circuit in Python, read its output, and show the same workflow on a real device. You only need Python to follow the examples.”

Closing: “You can build a circuit, sample it locally, and submit its compiled version to a quantum processor. The result is a distribution you need to interpret.”

## Demonstration plan

1. At slides 6–8, construct the three-qubit Hello World circuit and sample 1,024 shots. Explain why only `000` and `111` occur in the ideal model. Allow about one minute for the run and interpretation.
2. At slides 9–12, show the four objective values before VQE. Run only the small two-qubit section. Decode `01` aloud as `a=1, b=0`.
3. At slides 13–14, show the submission code, then the saved hardware output. The original VQE notebook defaults to retrieving its saved job. Keep a saved result available even if the account or network fails.
4. Use saved output for QAOA and the 14-qubit VQE example. Their long runs add little to a beginner talk.

Local rehearsal command from the repository root:

```bash
.venv/bin/python presentations/quantum_leap/output/rehearsal_demo.py
```

The script runs the supplied examples with current local APIs and never connects to a quantum processor. It checks the four half-adder inputs, the ideal GHZ outcomes, one Grover iteration, and the small VQE result. If you want an interactive walkthrough, copy the relevant short blocks into a fresh notebook or rehearse the original VQE cells in order. Do not run the legacy installation cells during the talk.

## Environment and saved results

Local rehearsal on 27 September 2026 used Python 3.14.2, Qiskit 2.5.2, qiskit-ibm-runtime 0.48.0, qiskit-algorithms 0.4.0 and qiskit-optimization 0.7.0. These describe this working environment, not a promise that any future latest versions will work. Preserve the project lock file and rehearse after changing packages.

| Example | Result used in the slides | Evidence |
|---|---|---|
| Hello World | `000`: 537, `111`: 487 | Saved original notebook output |
| Small VQE | `01`: 984 of 1,024 | Saved output, also reproduced locally |
| Hardware VQE circuit | `00`: 7, `01`: 986, `10`: 13, `11`: 18 | Saved notebook output only |
| Grover | P(`010`) = 12.5% before, 78.125% after one iteration | Exact calculation from the supplied circuit |
| QAOA route | Cost 11, 1.9% feasible samples | Saved notebook output |

The new Hello World rehearsal produced `000`: 515 and `111`: 509. The deck retains the original saved counts and labels them explicitly. The hardware counts were not retrieved again. No new QPU jobs were submitted. The route baseline was checked independently: the three allowed Moscow-to-Florianópolis paths have costs 11, 12 and 12.

## Shorter and longer versions

For 20 minutes plus questions, omit the half-adder, Grover and route slides (5, 15, 16). Explain the gate table in 45 seconds, use saved VQE output, and keep the cloud setup explanation brief. Preserve the measurement explanation and bit ordering.

For 45 minutes plus questions, keep the main sequence and spend the extra time on the VQE objective-to-Ising conversion, a live change to the circuit angles, and the full route graph in the supplied notebook. Use slide 19 to compare a modal answer with a rare feasible sample. Avoid extending the history section.

## Questions to rehearse

**Why use a quantum computer for four possibilities?** The four possibilities make the algorithm easy to check. This example demonstrates the programming workflow and makes no speed claim.

**Does the histogram prove entanglement?** This ideal circuit prepares an entangled GHZ state, but computational-basis counts alone could also come from a classical mixture. The shown histogram is not an entanglement certification.

**Why can the hardware count exceed the simulator count?** Both counts are finite samples. A difference of two occurrences in separate runs does not establish better hardware or estimate fidelity.

**Did VQE train on the device?** No. The notebook trained angles on the local simulator, then submitted one fixed circuit to the device.

**Does the `ab` term require entanglement?** No. It couples the objective variables, but the optimum in this example is a product basis state. CZ is part of the chosen ansatz.

**Why does QAOA say SUCCESS with only 1.9% feasible samples?** The optimizer can decode sampled candidates and return a good feasible one even when most measurements violate constraints. Always inspect the distribution as well as the returned objective.

**Does Grover search a Python list?** This notebook supplies a target oracle. Its example illustrates amplitude amplification. The usual search bound counts oracle calls and does not remove the cost of constructing the oracle or loading data.

## Before the conference

- Review every amber marker in the deck. `UPDATE` marks an API change, `CHECK BEFORE TALK` marks live platform or publication details, `SAVED RUN` identifies historical output, and `CORRECTION` marks a content mismatch.
- Confirm the IBM account, intended instance and accessible backend using the current account guide. Keep credentials off the projected screen.
- Keep the saved hardware output and a copy of the PDF available offline. Queue time is outside the talk schedule.
- Confirm the public repository contains the exact files being presented. The inspected workspace includes local changes, so a repository URL alone may point to older material.
- Confirm the name spelling and add a current affiliation only if desired. The old job titles and contact details were not carried over.
- Resolve or remove presenter review markers for the final public deck, while retaining the scientific qualifications and saved-run labels.

## Slide-by-slide speaker notes

### 1. Quantum Leap

Opening: “I will show you a small quantum program, read its output, and show the same workflow on a real device.” State that Python knowledge is enough. Avoid promises about business speedups.

Source: presentations/for_engineers/PythoNN/Q_PythoNN.pdf, p. 1; supplied conference title.

### 2. A quantum program in Python

Python constructs and submits a circuit. A simulator computes its behavior on a classical machine. A quantum processor executes the compiled gates. Both return measurement samples. A shot means one circuit execution followed by measurement. Transition: what do the gates act on?

Source: src/first_step/Q_Hello_World.ipynb, cells 4, 6, 7; src/optimization_problem/VQE_conference.ipynb, cells 11–12.

### 3. Qubits and measurement

A qubit can have complex amplitudes alpha and beta. Their squared magnitudes determine measurement probabilities. The H gate on a zero input gives equal probabilities. Measurement returns one classical bit. Explain phase only as a property gates can use to change later probabilities. Do not say the machine reads every answer simultaneously. The old “greater capacity” phrase hides this distinction.

Source: presentations/for_engineers/PythoNN/Q_PythoNN.pdf, pp. 5–8; presentations/for_engineers/2023_first_pres/Quantum.pptx, slide 7; src/first_step/Q_Hello_World.ipynb, cell 4.

### 4. The gates used in these notebooks

X flips a computational-basis value. H prepares equal probabilities from zero. CX flips its target when its control is one, stated for basis inputs. It can create entanglement on a superposed control. CCX has two controls. RY uses an adjustable angle. CZ changes a phase and can entangle suitable inputs. Avoid implying that CX copies arbitrary unknown quantum states.

Source: src/classic_on_quantum/half_adder.ipynb, cells 4–5; src/first_step/Q_Hello_World.ipynb, cell 4; src/optimization_problem/VQE_conference.ipynb, cells 2–5.

### 5. A half-adder

Use ordinary binary addition as a bridge. Inputs stay in q0 and q1. q2 stores the XOR sum and q3 stores the AND carry, both starting at zero. The notebook measures q2 into c0 and q3 into c1. Qiskit prints c1c0, hence 1+1 gives 10. This circuit demonstrates reversible logic, without a speedup claim. Local rehearsal checked all four input cases.

Source: src/classic_on_quantum/half_adder.ipynb, cells 3–6.

### 6. Hello World: three correlated qubits

Build the exact three-qubit circuit from the supplied Hello World notebook. H prepares the first qubit. Each CX correlates another qubit. Before measurement the ideal circuit prepares the GHZ state (|000> + |111>)/sqrt(2), which is entangled. The older decks use the two-qubit Bell version. Distinguish these variants. Computational-basis counts alone do not certify entanglement because a classical mixture can give the same histogram.

Source: src/first_step/Q_Hello_World.ipynb, cell 4; presentations/for_engineers/PythoNN/Q_PythoNN.pdf, p. 10; presentations/for_engineers/ItFest/Бейлак_Алиев_финал.pptx, slide 10.

### 7. Local simulation

Run the circuit from the previous slide. StatevectorSampler is a local ideal simulator in Qiskit. It produces sampled counts. measure_all creates the register named meas, which explains data.meas. The half-adder has register c instead, so use data.c for that circuit. Show this run live, allow about one minute including a question about expected counts. Documentation: https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.primitives.StatevectorSampler

Source: src/first_step/Q_Hello_World.ipynb, cell 6, migrated using StatevectorSampler already used in src/optimization_problem/VQE_conference.ipynb, cell 7.

### 8. Reading the counts

The notebook saved 537 occurrences of 000 and 487 of 111, totaling 1,024. This is a historical simulator result. An ideal circuit gives equal probabilities, but finite counts need not match. The updated local rehearsal gave 515 and 509. Never present either histogram as fresh hardware data. Ask why 001 is absent in the ideal simulator. Note that noise can introduce other strings on a device.

Source: src/first_step/Q_Hello_World.ipynb, cell 6, saved output.

### 9. A two-bit optimization problem

Introduce the supplied objective and enumerate four possibilities so the audience knows the correct answer before discussing VQE. q0 represents a and q1 represents b. 01 therefore means a=1 and b=0, with objective 3. Enumeration is the classical reference for this toy problem. The exercise shows the mechanism of a variational algorithm.

Source: src/optimization_problem/VQE_conference.ipynb, cells 1–3.

### 10. The VQE feedback loop

VQE means Variational Quantum Eigensolver. An ansatz is an adjustable trial circuit. The notebook uses RY rotations and CZ gates. SamplingVQE estimates a diagonal Ising cost from sampled outcomes. COBYLA changes angles on the classical CPU. The model conversion turns maximization into energy minimization. CZ is a circuit design choice: the ab term does not itself require an entangled optimal state. Here the optimum is a basis state. Documentation: https://qiskit-community.github.io/qiskit-algorithms/stubs/qiskit_algorithms.SamplingVQE.html

Source: src/optimization_problem/VQE_conference.ipynb, cells 2, 4, 6–7.

### 11. VQE in the supplied notebook

This is the central loop, with model construction and imports in the notebook and rehearsal script. small_problem is the objective on slide 9. cost_operator and small_ansatz come from cell 2. Show the seed and evaluation budget. The run uses 1,024 shots per sampled energy estimate and a COBYLA budget of 20 evaluations. The sampled cost need not improve at every evaluation. Run the supplied local rehearsal if there is time. Documentation: https://qiskit-community.github.io/qiskit-algorithms/stubs/qiskit_algorithms.SamplingVQE.html

Source: src/optimization_problem/VQE_conference.ipynb, cells 2, 7.

### 12. The measured answer

The saved simulator output has 984 occurrences of 01 out of 1,024. Group the remaining 40 under Other because the saved text explicitly reports the mode, not each remaining count. The most frequent bitstring directly decodes to the optimum. This differs from selecting a rare good candidate from many samples. Local rehearsal reproduced 984/1024 in this environment.

Source: src/optimization_problem/VQE_conference.ipynb, cells 7–9, saved output.

### 13. Submitting a cloud job

Prerequisite: configure an IBM Quantum Platform account and an accessible service instance using current instructions. QiskitRuntimeService() loads the saved account. Bind the trained angles before hardware execution: measured_circuit = small_ansatz.assign_parameters(small_result.optimal_point), then measured_circuit.measure_all(). Compile for the selected backend and submit one SamplerV2 job. Print and save job.job_id(). Read counts with job.result()[0].data.meas.get_counts(). Do not wait for a queue on stage. The supplied notebook defaults to retrieval of its existing job. No new QPU job was submitted while preparing this deck. Current account guide: https://quantum.cloud.ibm.com/docs/en/guides/initialize-account
Sampler API: https://quantum.cloud.ibm.com/docs/en/api/qiskit-ibm-runtime/sampler-v2
Service API: https://quantum.cloud.ibm.com/docs/en/api/qiskit-ibm-runtime/qiskit-runtime-service

Source: src/optimization_problem/VQE_conference.ipynb, cell 11; execution pattern from src/first_step/Q_Hello_World.ipynb, cell 7.

### 14. The saved hardware result

These counts come from the saved output of job dasegqjojkfs738p8fng on ibm_marrakesh. They were not fetched again for this draft. The angles were optimized on the local simulator and held fixed on the device. This is one hardware sampling job, not full VQE training on a QPU. 986 versus 984 occurrences of the mode does not establish a fidelity improvement or quantum advantage. Recheck the job metadata and backend name before the talk.

Source: src/optimization_problem/VQE_conference.ipynb, cells 11–13.

### 15. Grover: increasing a target probability

Use the supplied three-qubit target 010. The initial distribution assigns probability 1/8 to every string. The notebook applies one Grover iteration. An exact local statevector calculation gives 25/32 = 78.125% for 010. The target is built into a toy oracle. This example does not load or search a Python database. The asymptotic O(sqrt(N)) statement concerns oracle queries under the search model. Oracle implementation and data loading cost still matter. Documentation: https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.grover_operator
Query model: https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/grover-algorithm/unstructured-search

Source: src/grover/Grover.ipynb, cells 5–8; presentations/for_engineers/ItFest/Бейлак_Алиев_финал.pptx, slides 12–17.

### 16. Route optimization with QAOA

The current graph uses seven cities and eight directed edges, so the edge-based QUBO has eight binary variables and eight qubits. Start Moscow, end Florianopolis, with Baku required. The cheapest route follows Moscow, Baku, Doha, Florianopolis with toy cost 4+2+5=11. The notebook saved a successful candidate but only about 1.9% of all samples were feasible. Its text describes an older graph and seven qubits, which needs correction. The current code has no executed NetworkX baseline comparison despite its narrative promise. We independently enumerated the three feasible paths for this small graph: costs 11, 12, 12.

Source: src/traveling_salesman/travel_between_city/TSP.ipynb, cells 1, 3, 5, 9.

### 17. What these examples establish

Summarize what the supplied evidence actually supports. The circuits run and produce samples. A tiny objective can yield a dominant optimum in the saved VQE run. The saved hardware experiment executes fixed angles on a device. Grover illustrates amplitude amplification under a toy oracle. The route example exposes constraint handling and poor feasible sampling. None of these establishes a speed advantage. Keep this limit concise and tied to the examples.

Source: src/first_step/Q_Hello_World.ipynb, src/optimization_problem/VQE_conference.ipynb, src/grover/Grover.ipynb, src/traveling_salesman/travel_between_city/TSP.ipynb.

### 18. Code and questions

Closing: “You can build a circuit, sample it locally, and submit its compiled version to a quantum processor. The result is a distribution you need to interpret.” Point to the supplied repository. The GitHub link comes from the notebooks, but the current uncommitted notebook versions may not be published. Before sharing it publicly, verify that the exact rehearsal material is available at the intended revision. Invite questions.

Source: All five supplied notebooks; project repository linked in the source notebooks.

### 19. Backup: the larger VQE example

Five model variables comprise three binary choices plus two bounded integers. QUBO conversion introduces a total of fourteen binary variables. The saved solution is x1=1, x2=1, x3=0, x4=10, x5=5, objective 47. The constraint requires x4+x5 >= 15. This optimum can be verified directly for the toy model. MinimumEigenOptimizer chooses the best feasible decoded sample. The notebook states that the returned assignment is rare, but does not save a numerical frequency for it. Do not invent one or say that the modal string represents this answer.

Source: src/optimization_problem/VQE_conference.ipynb, cells 14–20.

### 20. Backup: API changes to review

The deprecated qiskit-ibm-provider / backend.run path applies to IBM cloud execution. Do not generalize the removal to every backend or to local Aer. Aer remains a separate simulator package. The draft uses StatevectorSampler for the ideal local examples, matching the current VQE notebook. qiskit[optimaze] in Grover is an invalid extra, not a valid dependency choice. Legacy Colab badges point to paths without src and should be checked. GroverOperator remains available in the installed 2.5.2 environment but is deprecated. Documentation: https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit
https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.primitives.StatevectorSampler
https://quantum.cloud.ibm.com/docs/en/api/qiskit-ibm-runtime/sampler-v2
https://quantum.cloud.ibm.com/docs/api/qiskit/2.2/qiskit.circuit.library.GroverOperator

Source: Legacy cells in Hello World, half_adder and Grover. Modern cells in VQE and TSP..

### 21. Backup: content that needs review

The older material includes historical hardware counts, job titles, contact details and broad QML labels. Osprey had 433 qubits in 2022. The ItFest timeline associates that figure with 2024, which should be corrected. Do not substitute a new largest-qubit claim unless needed and verified. The qubit wording needs measurement probabilities. The QML/QNN teaser has no corresponding implementation in the five supplied notebooks, so it is outside the core talk. The route markdown needs the current seven-city, eight-edge graph. The VQE claim that an ab interaction gives entanglement a necessary role is too strong: this optimum is a product basis state.

Source: presentations/for_engineers/2023_first_pres/Quantum.pptx, slides 5, 7–9, 16; presentations/for_engineers/ItFest/Бейлак_Алиев_финал.pptx, slides 3, 7; presentations/for_engineers/PythoNN/Q_PythoNN.pdf, pp. 3, 7, 12; src/traveling_salesman/travel_between_city/TSP.ipynb, markdown cells.

### 22. Reference links

These links support migration and accuracy checks, not additional case studies. Checked 27 September 2026. The detailed source audit maps findings to the supplied notebook cells and old slides. The legacy migration guide is archived and serves as evidence of the removed IBM execution path. Use current API pages for implementation.
sampler: https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.primitives.StatevectorSampler
runtime: https://quantum.cloud.ibm.com/docs/en/api/qiskit-ibm-runtime/sampler-v2
account: https://quantum.cloud.ibm.com/docs/en/guides/initialize-account
service: https://quantum.cloud.ibm.com/docs/en/api/qiskit-ibm-runtime/qiskit-runtime-service
bits: https://quantum.cloud.ibm.com/docs/en/guides/bit-ordering
grover: https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.grover_operator
deprecated: https://quantum.cloud.ibm.com/docs/api/qiskit/2.2/qiskit.circuit.library.GroverOperator
query: https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/grover-algorithm/unstructured-search
vqe: https://qiskit-community.github.io/qiskit-algorithms/stubs/qiskit_algorithms.SamplingVQE.html
qubo: https://qiskit-community.github.io/qiskit-optimization/tutorials/03_minimum_eigen_optimizer.html
install: https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit
osprey: https://research.ibm.com/blog/research-annual-letter-2022
migration: https://github.com/Qiskit/documentation/blob/2d2c2fcad47dd9e7ac1cc6807527dfccd796ea24/docs/migration-guides/qiskit-runtime.mdx
repo: https://github.com/beilak/qdev

Source: Official documentation used only to check and update supplied material.
