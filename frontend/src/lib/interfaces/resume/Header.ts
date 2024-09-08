export interface Header extends BaseHeader {
	id: number;
	created_at: string;
	updated_at: string;
}

export interface BaseHeader {
	member?: number;
	title?: string;
}