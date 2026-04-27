import { z } from "zod";

export const atividadeSchema = z.object({
  descricao: z.string().min(1, "Descrição obrigatória."),
  projeto: z.number().optional(),
  data_inicio: z.string().regex(/^\d{4}-\d{2}-\d{2}$/, "Data inválida (AAAA-MM-DD)."),
  data_fim: z.string().regex(/^\d{4}-\d{2}-\d{2}$/, "Data inválida (AAAA-MM-DD).")
});
