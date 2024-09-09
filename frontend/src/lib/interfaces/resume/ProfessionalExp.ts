export default interface ProfessionalExp {
	id?: number | string;
	// header?: number;
	job_title?: string;
	employer?: string;
	city?: string;
	country?: string;
	start_date?: string | Date;
	end_date?: string | Date;
	description?: string;
}
