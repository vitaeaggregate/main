export default interface PersonalInfo {
	id?: number | string;
	header?: number;
	full_name?: string;
	job_title?: string;
	email?: string;
	phone_number?: string;
	address?: string;
	date_of_birth?: string | Date;
	driving_license?: string;
	gender_pronoun?: string;
	marital_status?: string;
	nationality?: string;
}
