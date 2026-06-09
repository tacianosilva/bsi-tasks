---
name: vue-frontend
description: Use ao desenvolver aplicações frontend com Vue 3, Vite e Vitest nas disciplinas de Programação Web e projetos do BSI/UFRN.
---

# Vue 3 + Vite + Vitest

## Perfil

Stack frontend moderna para construção de interfaces web. Utiliza Composition
API do Vue 3, Vite como bundler e Vitest para testes unitários.

## Estrutura de projeto recomendada

```
projeto/
├── index.html
├── vite.config.ts
├── vitest.config.ts
├── tsconfig.json
├── package.json
├── public/
├── src/
│   ├── main.ts
│   ├── App.vue
│   ├── components/
│   ├── composables/
│   ├── views/
│   ├── router/
│   ├── stores/
│   └── assets/
└── tests/
    ├── unit/
    └── e2e/
```

## Padrões adotados

- **Linguagem** TypeScript (strict mode)
- **API** Composition API com `<script setup>`
- **Roteamento** Vue Router
- **Estado** Pinia
- **Testes unitários** Vitest + @vue/test-utils
- **Testes e2e** Playwright ou Cypress
- **Estilo** SCSS ou Tailwind CSS

## Comandos frequentes

```bash
npm create vite@latest . -- --template vue-ts
npm run dev
npm run build
npm run test:unit
npm run lint
```

## Referências

- [Vue 3 Docs](https://vuejs.org/)
- [Vite Docs](https://vite.dev/)
- [Vitest Docs](https://vitest.dev/)
- [Pinia Docs](https://pinia.vuejs.org/)
- [Vue Router Docs](https://router.vuejs.org/)
