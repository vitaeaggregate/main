export interface Comment extends BaseComment {
	id: number;
}

export interface BaseComment {
	header?: number;
	member?: number;
	description?: string;
}
