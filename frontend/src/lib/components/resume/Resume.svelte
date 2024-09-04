<script lang="ts">
	import EducationComponent from "$lib/components/resume/Education.svelte";
	import InterestComponent from "$lib/components/resume/Interest.svelte";
	import LinkComponent from "$lib/components/resume/Link.svelte";
	import PersonalInfoComponent from "$lib/components/resume/PersonalInfo.svelte";
	import PublicationComponent from "$lib/components/resume/Publication.svelte";
	import SkillComponent from "$lib/components/resume/Skill.svelte";
	import AwardComponent from "$lib/components/resume/Award.svelte";
	import CertificateComponent from "$lib/components/resume/Certificate.svelte";
	import CourseComponent from "$lib/components/resume/Course.svelte";
	import LanguageComponent from "$lib/components/resume/Language.svelte";
	import ProfessionalExpComponent from "$lib/components/resume/ProfessionalExperience.svelte";
	import ProjectComponent from "$lib/components/resume/Project.svelte";
	import ReferenceComponent from "$lib/components/resume/Reference.svelte";
	import InputText from "$lib/components/InputText.svelte";
	import InputCheckBox from "$lib/components/InputCheckBox.svelte";
	import type { BaseResume } from "$lib/interfaces/resume/Resume";
	import type PersonalInfo from "$lib/interfaces/resume/PersonalInfo";
	import type Link from "$lib/interfaces/resume/Link";
	import type ProfessionalExp from "$lib/interfaces/resume/ProfessionalExp";
	import type Education from "$lib/interfaces/resume/Education";
	import type Course from "$lib/interfaces/resume/Course";
	import type Language from "$lib/interfaces/resume/Language";
	import type Interest from "$lib/interfaces/resume/Interest";
	import type Project from "$lib/interfaces/resume/Project";
	import type Award from "$lib/interfaces/resume/Award";
	import type Reference from "$lib/interfaces/resume/Reference";
	import type Skill from "$lib/interfaces/resume/Skill";
	import type Publication from "$lib/interfaces/resume/Publication";
	import type Certificate from "$lib/interfaces/resume/Certificate";

	export const id: number | null = null;
	export let value: BaseResume | null = null;

	let title = "";
	let is_shareable = false;
	let personal_info: PersonalInfo = {};
	let professional_exps: ProfessionalExp[] = [];
	let links: Link[] = [];
	let skills: Skill[] = [];
	let educations: Education[] = [];
	let courses: Course[] = [];
	let languages: Language[] = [];
	let interests: Interest[] = [];
	let projects: Project[] = [];
	let publications: Publication[] = [];
	let awards: Award[] = [];
	let certificates: Certificate[] = [];
	let references: Reference[] = [];

	let professional_exp: ProfessionalExp = {};
	let link: Link = {};
	let skill: Skill = {};
	let education: Education = {};
	let course: Course = {};
	let language: Language = {};
	let interest: Interest = {};
	let project: Project = {};
	let publication: Publication = {};
	let award: Award = {};
	let certificate: Certificate = {};
	let reference: Reference = {};

	$: {
		value = {
			title,
			is_shareable,
			personal_info,
			professional_exps: [professional_exp],
			links: [link],
			skills: [skill],
			educations: [education],
			courses: [course],
			languages: [language],
			interests: [interest],
			projects: [project],
			publications: [publication],
			awards: [award],
			certificates: [certificate],
			references: [reference]
		};
	}
</script>

<div>
	<InputText label="Resume Name" bind:value={title} />
	<InputCheckBox label="Share" bind:value={is_shareable}></InputCheckBox>
	<PersonalInfoComponent bind:value={personal_info} />
	<EducationComponent bind:value={education}></EducationComponent>
	<InterestComponent bind:value={interest}></InterestComponent>
	<LinkComponent bind:value={link}></LinkComponent>
	<PublicationComponent bind:value={publication}></PublicationComponent>
	<SkillComponent bind:value={skill}></SkillComponent>
	<AwardComponent bind:value={award}></AwardComponent>
	<CertificateComponent bind:value={certificate}></CertificateComponent>
	<CourseComponent bind:value={course}></CourseComponent>
	<LanguageComponent bind:value={language}></LanguageComponent>
	<ProfessionalExpComponent bind:value={professional_exp}></ProfessionalExpComponent>
	<ProjectComponent bind:value={project}></ProjectComponent>
	<ReferenceComponent bind:value={reference}></ReferenceComponent>
</div>
