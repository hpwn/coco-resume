export type ExportFormat = 'pdf' | 'html';

export interface ExportOptions {
  readonly format: ExportFormat;
}

export function listSupportedFormats(): ExportFormat[] {
  return ['pdf', 'html'];
}

export function isFormatSupported(format: string): format is ExportFormat {
  return listSupportedFormats().includes(format as ExportFormat);
}
