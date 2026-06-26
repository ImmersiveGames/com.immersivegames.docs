---
name: immersive-framework-architecture-audit
description: Auditoria de boundaries, package ownership, nomenclatura pública e Inspector UX para o Immersive Framework sem alterar arquivos.
---

# Immersive Framework Architecture Audit

## Modo

- Não modificar arquivos.
- Não criar package.
- Não migrar código.
- Relatório objetivo com evidência por arquivo/classe/método.

## Objetivo

Separar o que é:

- package técnico genérico;
- framework core;
- módulo interno do framework;
- authoring/Inspector;
- editor tooling;
- referência antiga/Base 2.0;
- rejeitado por enquanto.

## Procurar

- package técnico absorvendo semântica de framework;
- framework core reimplementando primitive técnica já existente;
- nomes públicos ruins para usuário/Inspector;
- nomes que descrevem implementação em vez de intenção;
- manager/coordinator/processor genérico;
- singleton/global/bootstrap escondido;
- service locator;
- config global obrigatória;
- fallback silencioso;
- strings como identidade funcional;
- `UnityEngine` em runtime puro;
- Editor code em runtime assembly;
- adapter Unity contaminando package puro;
- Base 2.0 sendo copiado em vez de usado como referência.

## Classificação

Use categorias:

- `PackagePrimitive`
- `UnityAdapter`
- `FrameworkCore`
- `FrameworkModule`
- `Authoring`
- `EditorOnly`
- `ReferenceOnly`
- `RewriteRequired`
- `RejectForNow`

## Perguntas obrigatórias

- Isso faz sentido fora do Immersive Framework?
- Isso precisa conhecer Settings/Bootstrap/Module lifecycle?
- Isso é runtime puro, Unity adapter, Editor ou Authoring?
- Isso pertence a package técnico ou a `com.immersive.framework`?
- O nome faria sentido no Inspector para usuário Unity?
- Existe dependência ativa que justifique compatibilidade?
- O old Base 2.0 está sendo copiado sem redesign?

## Output

1. Resumo executivo.
2. Matriz curta por arquivo/símbolo:
   - responsabilidade;
   - categoria;
   - dependências;
   - risco;
   - destino recomendado;
   - decisão.
3. Allowed now.
4. Deferred/rejected.
5. Próximo corte seguro.
6. O que não mexer agora.
