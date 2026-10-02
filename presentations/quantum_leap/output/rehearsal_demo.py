"""Local rehearsal of the supplied notebooks. No credentials or QPU jobs.
Run from the repository root: .venv/bin/python presentations/quantum_leap/output/rehearsal_demo.py
"""
import json
import platform
from importlib.metadata import version
from pathlib import Path
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.quantum_info import Statevector
from qiskit.circuit.library import grover_operator, n_local
from qiskit_algorithms import SamplingVQE
from qiskit_algorithms.optimizers import COBYLA
from qiskit_algorithms.utils import algorithm_globals
from qiskit_optimization import QuadraticProgram


def rehearse():
    qc = QuantumCircuit(3)
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(0, 2)
    ideal = Statevector.from_instruction(qc).probabilities_dict()
    qc.measure_all()
    counts = StatevectorSampler(seed=42).run([qc], shots=1024).result()[0].data.meas.get_counts()
    assert set(counts) <= {'000', '111'} and sum(counts.values()) == 1024
    adders = {}
    for a in (0, 1):
        for b in (0, 1):
            adder = QuantumCircuit(4, 2)
            if a: adder.x(0)
            if b: adder.x(1)
            adder.cx(0, 2)
            adder.cx(1, 2)
            adder.ccx(0, 1, 3)
            adder.measure([2, 3], [0, 1])
            result = StatevectorSampler(seed=42).run([adder], shots=128).result()[0].data.c.get_counts()
            expected = f'{a & b}{a ^ b}'
            assert result == {expected: 128}
            adders[f'{a}+{b}'] = result
    init = QuantumCircuit(3)
    init.h([0, 1, 2])
    grover = init.compose(grover_operator(Statevector.from_label('010')))
    probabilities = Statevector.from_instruction(grover).probabilities_dict()
    assert abs(probabilities['010'] - 0.78125) < 1e-10
    grover.measure_all()
    grover_counts = StatevectorSampler(seed=42).run([grover], shots=1024).result()[0].data.meas.get_counts()
    small_problem = QuadraticProgram('Two-qubit VQE')
    small_problem.binary_var('a')
    small_problem.binary_var('b')
    small_problem.maximize(linear={'a': 3, 'b': 2}, quadratic={('a', 'b'): -4})
    cost_operator, offset = small_problem.to_ising()
    small_ansatz = n_local(2, 'ry', 'cz', reps=2, entanglement='full')
    algorithm_globals.random_seed = 1234
    energy = []
    vqe = SamplingVQE(
        sampler=StatevectorSampler(default_shots=1024, seed=1234),
        ansatz=small_ansatz, optimizer=COBYLA(maxiter=20),
        callback=lambda evaluation, parameters, mean, metadata: energy.append(float(mean)),
    )
    small_result = vqe.compute_minimum_eigenvalue(cost_operator)
    dist = small_result.eigenstate
    mode = max(dist, key=dist.get)
    a, b = int(mode[1]), int(mode[0])
    assert mode == '01' and small_problem.objective.evaluate([a, b]) == 3
    return {
        'python': platform.python_version(),
        'versions': {p: version(p) for p in ['qiskit', 'qiskit-ibm-runtime', 'qiskit-algorithms', 'qiskit-optimization']},
        'ghz_probabilities': ideal, 'ghz_counts': counts, 'half_adder': adders,
        'grover_probabilities': probabilities, 'grover_counts': grover_counts,
        'vqe_counts': {b: round(1024 * dist.get(b, 0)) for b in ['00', '01', '10', '11']},
        'vqe_energy': energy, 'vqe_mode': mode, 'vqe_objective': float(small_problem.objective.evaluate([a, b])),
        'qpu_accessed': False,
    }


if __name__ == '__main__':
    print(json.dumps(rehearse(), indent=2))
