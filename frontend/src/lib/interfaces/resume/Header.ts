export interface Header extends BaseHeader {
  id: number;
}

export interface BaseHeader {
  member?: number;
  title?: string;
  created_at?: string;
  updated_at?: string;
}
