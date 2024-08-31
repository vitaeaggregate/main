export default interface ProfessionalExp {
	id: number;
	resume: number;
	job_title: string;
	employer: string;
	city?: string;
	country?: string;
	start_date?: Date;
	end_date?: Date;
	description?: string;
}
