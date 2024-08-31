export default interface Account {
	id: number;
	email: string;
	firebase_uid?: string;
	can_comment: boolean;
	created_at: Date;
	updated_at: Date;
}
