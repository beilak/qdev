# Source audit and update links

Reviewed 27 September 2026. Notebook cell numbers below are zero-based. Presentation slides and PDF pages are one-based. The examples and results in the draft come from the supplied materials. Official documentation supports compatibility checks and factual corrections. No external case studies or performance claims were added.

## Material reviewed

| Supplied material | What it contributes | Treatment in the draft |
|---|---|---|
| `Q_Hello_World.ipynb` (8 cells) | Three-qubit GHZ circuit, local counts, cloud submission | Main circuit and saved histogram. Local execution migrated. |
| `half_adder.ipynb` (7 cells) | XOR sum, AND carry, X/CX/CCX gates | One short bridge from ordinary logic to circuits. |
| `Grover.ipynb` (12 cells) | Three qubits, target `010`, one Grover iteration | Brief probability example. Deprecated operator flagged. |
| `VQE_conference.ipynb` (21 cells) | Small objective, SamplingVQE, saved QPU output, larger encoding | Central demonstration. Large example moves to backup. |
| `TSP.ipynb` (11 cells) | Route QUBO, QAOA, feasibility distribution | Brief application. Correct problem name and qubit count. |
| `Q_PythoNN.pdf` (13 pages) | Basic concepts, Bell circuit, simulation, QML teaser | Retain concept-to-code flow. Replace vague qubit wording. |
| ItFest deck (18 slides) | Hello World, gates, Grover oracle and results | Retain practical sequence. Use the smaller supplied Grover notebook. |
| `Quantum.pptx` (16 slides) | History, qubit overview, hardware chart, random-bit examples | Use introductory ideas. Omit dated hardware rankings and old contacts. |

The current VQE and route notebooks already use modern APIs. They should not be treated as untouched 2023 files. The three older notebooks contain legacy installation and execution code.

## API changes

| Location | Finding | Action / draft slide | Authoritative reference |
|---|---|---|---|
| Hello World cell 2, half-adder cell 2, Grover cell 8 | `from qiskit import Aer` belongs to the older package layout. | Draft uses `StatevectorSampler` for ideal local sampling, consistent with the supplied VQE notebook. Slides 7 and 20. If keeping Aer, install its separate package and use its namespace. | [Qiskit installation](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit), [StatevectorSampler](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.primitives.StatevectorSampler) |
| Hello World cell 7, Grover cells 10–11 | `IBMProvider` and IBM cloud `backend.run` are obsolete. | Use the `QiskitRuntimeService` / `SamplerV2` pattern already present in VQE. Slide 13. This does not mean every third-party or local backend has removed `run`. | [Current SamplerV2 API](https://quantum.cloud.ibm.com/docs/en/api/qiskit-ibm-runtime/sampler-v2), [archived IBM migration guide](https://github.com/Qiskit/documentation/blob/2d2c2fcad47dd9e7ac1cc6807527dfccd796ea24/docs/migration-guides/qiskit-runtime.mdx) |
| Grover cell 6 | `GroverOperator` was deprecated in Qiskit 2.1. It still exists in the inspected 2.5.2 environment. | Use `grover_operator`. Slides 15 and 20. | [Deprecation notice](https://quantum.cloud.ibm.com/docs/api/qiskit/2.2/qiskit.circuit.library.GroverOperator), [replacement function](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.grover_operator) |
| Grover cell 1 | The extra `optimaze` is invalid. The saved pip output already warns about it. | Remove that installation line from a future notebook revision. Use a rehearsed environment before the talk. Slide 20. | [Qiskit installation guide](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit) |
| VQE cell 11 | Current Runtime API, `channel='ibm_quantum_platform'`, `instance='auto'`. The cell reads an API key locally. | Keep the current API. The shorter slide loads a previously saved account. Recheck instance access and available backends. | [Account initialization](https://quantum.cloud.ibm.com/docs/en/guides/initialize-account), [QiskitRuntimeService](https://quantum.cloud.ibm.com/docs/en/api/qiskit-ibm-runtime/qiskit-runtime-service) |
| Measurement reads across examples | Register names differ: `measure_all()` creates `meas`, while the half-adder explicitly uses `c`. | Use `.data.meas.get_counts()` or `.data.c.get_counts()` as appropriate. | [StatevectorSampler results example](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.primitives.StatevectorSampler) |
| Old Colab badges | Their GitHub paths omit the current `src/` prefix. Grover also points to a different location. | Verify public paths and the intended revision before sharing. Slide 18. | Repository paths inspected locally. Public file availability was not verified. |

The old migration guide now redirects to a GitHub archive and explicitly says it is no longer maintained. It documents why the old IBM access path changed. Current API references above guide the replacement code.

## Content corrections and interpretation

| Location | Finding | Treatment |
|---|---|---|
| PythoNN p. 7, ItFest slide 7, Quantum slide 7 | “Greater capacity” does not explain amplitudes or what measurement returns. | Slide 3 uses amplitudes, probabilities and one classical bit per measured qubit. Explain normalization verbally. |
| PythoNN and ItFest slides 10–11 versus Hello World notebook | The decks use a two-qubit Bell circuit. The notebook uses three-qubit GHZ. | Use the three-qubit notebook consistently. Slide 6 calls it an entangled GHZ state. |
| GHZ histogram | Correlated `000`/`111` counts alone do not certify entanglement. | Notes distinguish the ideal prepared state from what the histogram proves. |
| Half-adder cell 6 and VQE cells 7–9 | Displayed bit order can reverse the audience's interpretation. | Slides 5 and 9 explicitly decode rightmost `q0`/`c0`. See [IBM bit-ordering guide](https://quantum.cloud.ibm.com/docs/en/guides/bit-ordering). |
| VQE cell 4 | The wording suggests CZ is required to represent the `ab` interaction. | Explain CZ as an ansatz choice. The optimum here is a computational-basis product state, so the objective coupling does not prove entanglement is necessary. |
| VQE cells 2 and 7 | This is `SamplingVQE` for a diagonal Hamiltonian, rather than general observable estimation. | Name SamplingVQE in the code and explain measured costs. See [SamplingVQE API](https://qiskit-community.github.io/qiskit-algorithms/stubs/qiskit_algorithms.SamplingVQE.html). |
| VQE cells 11–13 | The device evaluates fixed angles trained locally. | Slides 13–14 do not imply full VQE training on the QPU. The saved job is `dasegqjojkfs738p8fng`, backend `ibm_marrakesh`. |
| VQE saved counts | Simulator mode 984/1,024, hardware mode 986/1,024. | Label both as saved results. The difference is not evidence that hardware is more accurate or that the run has quantum advantage. |
| VQE cells 14–20 | The 14-qubit result is the best feasible sampled candidate, not necessarily the mode. Its frequency is not provided numerically in saved text. | Slide 19 reports objective 47 with this qualification. Do not invent a probability. |
| Grover / old database story | The notebook supplies a target in a toy oracle. It does not encode or search an ordinary Python database. | Slide 15 uses amplitude amplification and qualifies complexity as oracle queries. See [IBM query-model explanation](https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/grover-algorithm/unstructured-search). |
| TSP filename and cell 0 | The current task is a constrained shortest path, not a tour visiting every city. | Slide 16 uses “Route optimization with QAOA.” |
| TSP cells 0, 2, 6, 8 | Prose names Moscow/Nizhny Novgorod/Yaroslavl and five cities/seven legs/seven qubits. | Current code has Moscow/Florianópolis/Baku, seven cities, eight edges and eight qubits. Correct these before showing notebook markdown. |
| TSP cell 4 | The narrative promises a classical NetworkX comparison, but the current code does not execute a separate baseline solve. | An independent local check enumerated costs 11, 12 and 12. Add the classical baseline to a future notebook revision. |
| TSP cell 9 | Only about 1.9% of saved samples are feasible, despite a successful returned route. | Keep the feasibility figure prominent. Do not present a good decoded candidate as a concentrated output distribution. See [Minimum Eigen Optimizer](https://qiskit-community.github.io/qiskit-optimization/tutorials/03_minimum_eigen_optimizer.html). |
| TSP general flow explanation | Positive edge costs discourage extra cycles, but a required-city constraint can allow a disconnected cycle in a more general cyclic graph. | The supplied graph is acyclic, so this issue does not change its three paths. Do not generalize the model to arbitrary graphs without checking connectivity. |
| ItFest slide 3, PythoNN p. 3, Quantum slides 5 and 8 | Osprey/433 qubits belongs to 2022. The ItFest timeline associates the figure with 2024. | Flag on slide 21. Keep as history if used. [IBM's 2022 retrospective](https://research.ibm.com/blog/research-annual-letter-2022) confirms the year. |
| Quantum slide 9 | Patent slide lacks usable evidence in the inspected material. | Omit rather than invent statistics. |
| PythoNN p. 12 | VQE/VCR/QML/QNN teaser exceeds the implementation covered by the five notebooks. | Keep VQE. Omit a separate QML claim or demo. |
| Earlier title and closing slides | Job titles, affiliation, telephone and email are historical. | Use only the presenter's name. Review current details before publication. |

## Result provenance

The draft retains original saved counts for Hello World and VQE. It does not relabel them as fresh experiments. Grover's probabilities are a new exact calculation of the supplied circuit: one iteration gives 25/32 for the marked state. The route cost check uses the current edge list. These are calculations from the user's material, not outside benchmark data.

The small local examples ran successfully with the inspected environment. The long QAOA and 14-qubit VQE optimizations were not rerun. Saved hardware results were not fetched again, and no QPU access was used. The supplied source notebooks and prior presentations were left unchanged.

## Complete cloud snippet for rehearsal

This follows the existing VQE example and assumes the small VQE cells have already produced `small_ansatz` and `small_result`. Configure the intended account before use. `QiskitRuntimeService()` loads saved account settings. The `.run(...)` call below submits a new device job, so showing the code does not require executing it on stage.

```python
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

measured_circuit = small_ansatz.assign_parameters(small_result.optimal_point)
measured_circuit.measure_all()
service = QiskitRuntimeService()
backend = service.least_busy(
    operational=True, simulator=False, min_num_qubits=2,
)
pm = generate_preset_pass_manager(backend=backend, optimization_level=3)
isa = pm.run(measured_circuit)
job = SamplerV2(mode=backend).run([isa], shots=1024)
print(job.job_id())
counts = job.result()[0].data.meas.get_counts()
```

To retrieve the notebook's existing job without submitting another one, use `service.job('dasegqjojkfs738p8fng')` with the authorized account. Keep the saved output available if retrieval fails.
