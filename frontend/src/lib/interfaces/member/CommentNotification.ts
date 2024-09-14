import type { Comment } from "$lib/interfaces/resume/Comment";
import type { Header } from "$lib/interfaces/resume/Header";

export default interface CommentNotification {
  id: number;
  comment: Comment;
  header: Header;
  created_at: Date | string;
  is_read: boolean;
}
