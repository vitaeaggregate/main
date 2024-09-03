export interface Comment extends BaseComment {
	id: number;
}

export default interface BaseComment {
	id?: number;
	header?: number;
	member?: number;
	description?: string;
}
