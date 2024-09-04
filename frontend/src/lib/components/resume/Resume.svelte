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
	import type Skill from "$lib/interfaces/resume/Skill";
	import type Education from "$lib/interfaces/resume/Education";
	import type Course from "$lib/interfaces/resume/Course";
	import type Language from "$lib/interfaces/resume/Language";
	import type Interest from "$lib/interfaces/resume/Interest";
	import type Project from "$lib/interfaces/resume/Project";
	import type Publication from "$lib/interfaces/resume/Publication";
	import type Award from "$lib/interfaces/resume/Award";
	import type Certificate from "$lib/interfaces/resume/Certificate";
	import type Reference from "$lib/interfaces/resume/Reference";

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

	$: {
		value = {
			title,
			is_shareable,
			personal_info,
			professional_exps,
			links,
			skills,
			educations,
			courses,
			languages,
			interests,
			projects,
			publications,
			awards,
			certificates,
			references
		};
	}
</script>

<div>
	<InputText label="Resume Name" bind:value={title} />
	<InputCheckBox label="Share" bind:value={is_shareable}></InputCheckBox>
	<PersonalInfoComponent bind:value={personal_info} />
	<!-- <button on:click={() => (links = [...links, {}])}>Add Link</button>
	{#each links as link, index}
		<LinkComponent bind:value={links[index]} />
		<button
			on:click={() => {
				console.log(index);
				links.splice(index, 1);
				links = [...links];
			}}>Delete</button
		>
	{/each} -->
</div>
