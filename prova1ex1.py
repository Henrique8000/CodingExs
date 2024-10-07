
conta = float(input())

andre = conta // 3
carlos = conta // 3
eduardo = conta / 3

diferenca = (eduardo - carlos) + (eduardo - andre)

print(f"Andre: {andre:.2f}")
print(f"Carlos: {carlos:.2f}")
print(f"Eduardo: {eduardo:.2f}")

print(f"Com a diferença, Eduardo pagará: R${eduardo + diferenca:.2f}")