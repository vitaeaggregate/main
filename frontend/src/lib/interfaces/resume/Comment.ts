export interface Comment extends BaseComment {
	id: number;
}

export interface BaseComment {
	header?: number;
	member?: number;
	description?: string;
	created_at?: string | Date;
	updated_at?: string | Date;
}
