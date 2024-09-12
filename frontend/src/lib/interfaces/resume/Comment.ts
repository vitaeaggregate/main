export interface CommentHeader {
	id: number;
	title: string;
}
export interface Comment {
	id?: number | string;
	header?: CommentHeader | number;
	member?: number;
	description?: string;
	created_at?: string | Date;
	updated_at?: string | Date;
	can_delete?: boolean;
}
