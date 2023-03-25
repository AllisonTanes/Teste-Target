
sp = float(6783643)
rj = float(3667866)
mg = float(2922988)
es = float(2716548)
outros = float(1984953)


total = float(sp + rj + mg + es + outros)

print('O faturamento total da distribuidora foi: R${:.2f}'.format(total))

psp = ((sp/total)*100)
prj = ((rj/total)*100)
pmg = ((mg/total)*100)
pes = ((es/total)*100)
poutros = ((outros /total)*100)

print('O percentual de faturamento de SP {:.2f}%'.format(psp))
print('O percentual de faturamento de RJ {:.2f}%'.format(prj))
print('O percentual de faturamento de MG {:.2f}%'.format(pmg))
print('O percentual de faturamento de ES {:.2f}%'.format(pes))
print('O percentual de faturamento de OUTROS {:.2f}%'.format(poutros))