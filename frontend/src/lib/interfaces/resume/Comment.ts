export interface CommentHeader {
  id: number;
  title: string;
}
export interface Comment {
  id?: number | string;
  header?: number | string;
  header_info?: CommentHeader;
  member?: number;
  description?: string;
  created_at?: string;
  updated_at?: string;
  can_delete?: boolean;
}
