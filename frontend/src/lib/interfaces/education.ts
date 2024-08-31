export default interface Education {
	id: number;
	resume: number;
	degree?: string;
	institution?: string;
	city?: string;
	country?: string;
	start_date?: Date;
	end_date?: Date;
	description?: string;
}
