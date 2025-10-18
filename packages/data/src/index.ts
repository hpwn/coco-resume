export interface ResumeSection {
  readonly id: string;
  readonly title: string;
  readonly content: string;
}

export function createResumeSection(id: string, title: string, content: string): ResumeSection {
  return { id, title, content };
}
