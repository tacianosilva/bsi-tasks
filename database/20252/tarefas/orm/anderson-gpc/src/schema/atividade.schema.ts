import {z} from 'zod';

export const AtividadeCreateInput = z.object({
  descricao: z.string(),
  projeto: z.number().int().nullable().optional(), 
  data_inicio: z.coerce.date(),  
  data_fim: z.coerce.date(),
});

