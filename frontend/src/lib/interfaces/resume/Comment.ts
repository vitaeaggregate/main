export interface CommentHeader {
	id: number;
	title: string;
}
export interface Comment extends BaseComment {
	id: number;
}

export interface BaseComment {
	header?: CommentHeader;
	member?: number;
	description?: string;
	created_at?: string | Date;
	updated_at?: string | Date;
}
