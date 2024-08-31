// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
declare global {
	namespace App {
		// interface Error {}
		// interface Locals {}
		// interface PageData {}
		// interface PageState {}
		// interface Platform {}
	}
}

interface Account {
	id: number;
	email: string;
	password: string;
	can_comment: boolean;
	created_at: Date;
	updated_at: Date;
}

interface Resume {
	id: number;
	member: number;
	title: string;
	created_at: Date;
	updated_at: Date;
}

interface PersonalInfo {
	id: number;
	resume: number;
	full_name: string;
	job_title: string;
	email?: string;
	phone_number?: string;
	address?: string;
	date_of_birth?: Date;
	driving_license?: string;
	gender_pronoun?: string;
	marital_status?: string;
	nationality?: string;
}

interface Interest {
	id: number;
	resume: number;
	name: string;
	description?: string;
}

interface Publication {
	id: number;
	resume: number;
	title: string;
	publisher?: string;
	date?: Date;
	description?: string;
}

interface Skill {
	id: number;
	resume: number;
	name: string;
	description?: string;
	skill_level?: string;
}

interface Education {
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

interface Link {
	id: number;
	resume: number;
	title: string;
	url: string;
}

interface ProfessionalExp {
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

interface Reference {
	id: number;
	resume: number;
	name: string;
	job_title?: string;
	organization?: string;
	email?: string;
	phone?: string;
}

interface Project {
	id: number;
	resume: number;
	title: string;
	sub_title?: string;
	start_date?: Date;
	end_date?: Date;
	description?: string;
}

interface Course {
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

interface Certificate {
	id: number;
	resume: number;
	name?: string;
	description?: string;
}

interface Award {
	id: number;
	resume: number;
	title?: string;
	issuer?: string;
	date?: Date;
	description?: string;
}

interface Language {
	id: number;
	resume: number;
	language: string;
	description: string;
	skill_level: string;
}

interface Comment {
	id: number;
	resume: number;
	member: number;
	description: string;
}

export {};
