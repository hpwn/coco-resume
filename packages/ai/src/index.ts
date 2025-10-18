export interface AiClientOptions {
  readonly model: string;
  readonly apiKey?: string;
}

export class AiClient {
  public constructor(private readonly options: AiClientOptions) {}

  public describe(): string {
    return `AI client configured for model "${this.options.model}"`;
  }
}
