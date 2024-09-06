import type { BaseHeader } from "$lib/interfaces/resume/Header";
import type Award from "$lib/interfaces/resume/Award";
import type Certificate from "$lib/interfaces/resume/Certificate";
import type Interest from "$lib/interfaces/resume/Interest";
import type PersonalInfo from "$lib/interfaces/resume/PersonalInfo";
import type Course from "$lib/interfaces/resume/Course";
import type Education from "$lib/interfaces/resume/Education";
import type Language from "$lib/interfaces/resume/Language";
import type Link from "$lib/interfaces/resume/Link";
import type Project from "$lib/interfaces/resume/Project";
import type Reference from "$lib/interfaces/resume/Reference";
import type Skill from "$lib/interfaces/resume/Skill";
import type ProfessionalExp from "$lib/interfaces/resume/ProfessionalExp";
import type Publication from "$lib/interfaces/resume/Publication";

export interface Resume extends BaseResume {
	id: number;
	created_at: Date;
	updated_at: Date;
}

export interface BaseResume extends BaseHeader {
	title: string;
	personal_info: PersonalInfo;
	is_shareable: boolean;
	awards: Award[];
	certificates: Certificate[];
	courses: Course[];
	educations: Education[];
	interests: Interest[];
	languages: Language[];
	links: Link[];
	professional_exps: ProfessionalExp[];
	projects: Project[];
	references: Reference[];
	skills: Skill[];
	publications: Publication[];
}
