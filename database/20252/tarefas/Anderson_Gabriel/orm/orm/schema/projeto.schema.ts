import { z } from "zod";

export const EsquemaMudarLiderProjeto = z.object({
    codigo: z.int(),
    responsavel: z.int(),
})
