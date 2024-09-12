export interface CommentHeader {
	id: number;
	title: string;
}
export interface Comment {
	id?: number | string;
	header?: number;
	header_info?: CommentHeader;
	member?: number;
	description?: string;
	created_at?: string | Date;
	updated_at?: string | Date;
	can_delete?: boolean;
}
