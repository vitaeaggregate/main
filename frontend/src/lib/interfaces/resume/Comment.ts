import type { Header } from "$lib/interfaces/resume/Header";

export interface CommentHeader extends Header {
	
}
export interface Comment extends BaseComment {
	id: number;
}



export interface BaseComment {

	member?: number;
	description?: string;
	created_at?: string | Date;
	updated_at?: string | Date;
}
