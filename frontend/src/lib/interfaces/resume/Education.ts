export default interface Education {
	id?: number | string;
	// header?: number;
	degree?: string;
	institution?: string;
	city?: string;
	country?: string;
	start_date?: string | Date;
	end_date?: string | Date;
	description?: string;
}
