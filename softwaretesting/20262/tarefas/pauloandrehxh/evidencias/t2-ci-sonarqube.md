# Evidência de CI e SonarScanner — T2

## Revisões verificadas

- [PR #11, integrado na main](https://github.com/pauloandrehxh/arena-ufrn/pull/11).
- Revisão final da branch: `89ac25f5d990cc0362fa9cf3149038bc623d3e0f`.
- Commit de merge: `3a5393ffbdf3fc292060276f5eae12e060c74a0c`.
- Merge registrado no GitHub: `2026-10-07T01:08:57Z` (06/10/2026, 22:08:57 em America/Fortaleza).
- [CI da revisão final do PR](https://github.com/pauloandrehxh/arena-ufrn/actions/runs/37555509413): concluído com `success`.
- [CI da main após merge](https://github.com/pauloandrehxh/arena-ufrn/actions/runs/37555641340): concluído com `success`.

## Transcrição dos logs reais da main

Obtidos com:

```bash
gh run view 37555641340 --repo pauloandrehxh/arena-ufrn --log
```

Trechos relevantes, sem secrets:

```text
Executar testes unitários:
Test Suites: 3 passed, 3 total
Tests:       70 passed, 70 total

Executar testes de integração:
Test Suites: 4 passed, 4 total
Tests:       64 passed, 64 total

Gerar cobertura:
All files | 77.99 | 71.25 | 90.32 | 77.99
Test Suites: 7 passed, 7 total
Tests:       134 passed, 134 total

Executar análise SonarQube:
2026-10-07T01:10:50.4588410Z
ANALYSIS SUCCESSFUL, you can find the results at:
https://labens.dct.ufrn.br/sonarqube/dashboard?id=arena-ufrn

2026-10-07T01:10:50.4610939Z
More about the report processing at
https://labens.dct.ufrn.br/sonarqube/api/ce/task?id=4f3d2799-6638-4da6-a0e2-a47d422bbbd8

2026-10-07T01:10:50.9947711Z
EXECUTION SUCCESS
```

As métricas Jest são, respectivamente, statements, branches, functions e lines.
Não são métricas consultadas no dashboard SonarQube.

## Correções dos apontamentos informados pelo discente

O usuário informou dois apontamentos vistos no LABENS após a análise do PR:

1. Mover `responderErro`, em `quadra.controller.js`, para o maior escopo possível:
   a função foi movida da factory para o escopo do módulo, pois não depende do service.
2. Regra `javascript:S7735`, em `reserva.service.js`: o ternário
   `data.date !== undefined ? ... : ...` foi invertido para condição positiva
   `data.date === undefined ? {} : ...`, sem mudar o comportamento.

Ambos foram corrigidos no [commit 89ac25f](https://github.com/pauloandrehxh/arena-ufrn/commit/89ac25f5d990cc0362fa9cf3149038bc623d3e0f).
Depois das correções, os 134 testes passaram localmente e no CI. O scanner
voltou a concluir com sucesso, tanto no PR quanto na main.

As correções anteriores de Luis no [PR #10](https://github.com/pauloandrehxh/arena-ufrn/pull/10)
foram integradas à branch de Paulo, preservando CORS restrito e catches sem
variável onde o erro não é usado. O merge de integração foi `65db27c`.

## Limites da evidência

Esta é evidência textual real de execução do scanner e das correções, não um
print do dashboard. A consulta anônima às métricas do LABENS ainda retornou 401.
Sem acesso autenticado, **Quality Gate e ausência de issues remanescentes não
foram verificados nesta sessão**. Não confundir `ANALYSIS SUCCESSFUL` com aprovação
do Quality Gate. Anexar prints ou exportação autenticada do dashboard para
completar essa verificação, caso exigida na avaliação.
