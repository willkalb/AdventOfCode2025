import Helper
from math import sqrt, pow
from operator import itemgetter
from math import prod

DAY = "8"

jb_poss: list[tuple[int, ...]] = [ tuple([ int(s) for s in l.split(",") ]) for l in Helper.get_input_lines(DAY) ]

jb_dists: list[tuple[int, int, float]] = []
for i_jb1 in range(0, len(jb_poss)):
    for i_jb2 in range(i_jb1 + 1, len(jb_poss)):
        jb_dists.append((i_jb1, i_jb2, sqrt(pow(jb_poss[i_jb1][0] - jb_poss[i_jb2][0], 2) + pow(jb_poss[i_jb1][1] - jb_poss[i_jb2][1], 2) + pow(jb_poss[i_jb1][2] - jb_poss[i_jb2][2], 2))))

jb_dists = sorted(jb_dists, key=itemgetter(2))

CONN_ALLOWED = 1000
jb_dists_1 = jb_dists[:CONN_ALLOWED]
circuits: list[list[tuple[int, int]]] = []
connections = 0
for jb_dist in jb_dists_1:
    if connections >= CONN_ALLOWED: 
        break

    connections += 1

    found_in_circuit = False
    circuit_match: list[int] = []
    for i, circuit in enumerate(circuits):
        if jb_dist[0] in [ i for t in circuit for i in t ] and jb_dist[1] in [ i for t in circuit for i in t ]:
            found_in_circuit = True
            continue
        
        if jb_dist[0] in [ i for t in circuit for i in t ] or jb_dist[1] in [ i for t in circuit for i in t ]:
            found_in_circuit = True
            circuit_match.append(i)
            circuit.append(jb_dist[:2])
            
    if len(circuit_match) == 2:
        circuits[circuit_match[0]] = circuits[circuit_match[0]] + circuits[circuit_match[1]]
        circuits[circuit_match[1]] = []

    if found_in_circuit:
        continue

    circuits.append([ jb_dist[:2] ])

score = prod([ len({ i for t in l for i in t }) for l in sorted([ c for c in circuits if len(c) > 0 ], key=lambda x: len(x), reverse=True)[:3] ])

print(f"\tPart 1: {score}")


jb_dists_2 = jb_dists
circuits = []
for jb_dist in jb_dists_2:
    if len(jb_poss) == len({ i for l in circuits for t in l for i in t }):
        break

    found_in_circuit = False
    circuit_match: list[int] = []
    for i, circuit in enumerate(circuits):
        if jb_dist[0] in [ i for t in circuit for i in t ] and jb_dist[1] in [ i for t in circuit for i in t ]:
            found_in_circuit = True
            continue
        
        if jb_dist[0] in [ i for t in circuit for i in t ] or jb_dist[1] in [ i for t in circuit for i in t ]:
            found_in_circuit = True
            circuit_match.append(i)
            circuit.append(jb_dist[:2])
            
    if len(circuit_match) == 2:
        circuits[circuit_match[0]] = circuits[circuit_match[0]] + circuits[circuit_match[1]]
        circuits[circuit_match[1]] = []

    if found_in_circuit:
        continue

    circuits.append([ jb_dist[:2] ])

score = prod([ t[0] for t in [ jb_poss[i] for i in [ c for c in circuits if len(c) > 0 ][0][-1] ] ])

print(f"\tPart 2: {score}")
