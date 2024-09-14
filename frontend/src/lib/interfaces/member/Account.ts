export default interface Account {
  id: number;
  email: string;
  firebase_uid?: string;
  can_comment?: boolean;
  created_at?: string;
  updated_at?: string;
}
