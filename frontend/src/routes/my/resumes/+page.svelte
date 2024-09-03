<script>
	import Education from "$lib/components/resume/Education.svelte";
	import Interest from "$lib/components/resume/Interest.svelte";
	import Links from "$lib/components/resume/Links.svelte";
	import PersonalInformation from "$lib/components/resume/PersonalInfo.svelte";
	import Publications from "$lib/components/resume/Publication.svelte";
	import Skills from "$lib/components/resume/Skill.svelte";
	import Awards from "$lib/components/resume/Award.svelte";
	import Certificates from "$lib/components/resume/Certificate.svelte";
	import Courses from "$lib/components/resume/Course.svelte";
	import Languages from "$lib/components/resume/Language.svelte";
	import ProfessionalExperience from "$lib/components/resume/ProfessionalExperience.svelte";
	import Projects from "$lib/components/resume/Project.svelte";
	import References from "$lib/components/resume/Reference.svelte";

	import { account } from "$lib/store";
	
	import type Resume from "$lib/interfaces/resume/Resume";
	import type PersonalInfo from "$lib/interfaces/resume/PersonalInfo";
	import type Link from "$lib/interfaces/resume/Link";
	import type ProfessionalExp from "$lib/interfaces/resume/ProfessionalExp";
	import type Skill from "$lib/interfaces/resume/Skill"
	import type Education from "$lib/interfaces/resume/Education";
	import type Course from "$lib/interfaces/resume/Course";
	import type Language from "$lib/interfaces/resume/Language";
	import type Interest from "$lib/interfaces/resume/Interest";
	import type Project from "$lib/interfaces/resume/Project";
	import type Publication from "$lib/interfaces/resume/Publication";
	import type Award from "$lib/interfaces/resume/Award";
	import type Certificate from "$lib/interfaces/resume/Certificate";
	import type Reference from "$lib/interfaces/resume/Reference";
	
	import { addResume } from "$lib/api/resume";
	import InputText from "$lib/components/InputText.svelte";

	export const id:number|null = null
	export const memberID:number|null = null;

	let personalInfo:PersonalInfo|null = null
	let profExp:ProfessionalExp|null = null;
	let link:Link|null= null;
	let skill:Skill|null= null;
	let education:Education|null = null;
	let course:Course|null = null;
	let language:Language|null = null;
	let interest:Interest|null = null;
	let project:Project|null = null;
	let publication:Publication|null = null;
	let award:Award|null = null;
	let certificate:Certificate|null = null;
	let reference:Reference|null = null;

	let title: string = '';

	// function handleUpdate(event:CustomEvent) {
	// 	// personalInfo = event.detail;
	// 	// profExp = event.detail;
	// 	// link = event.detail;
	// 	// skill = event.detail;
	// 	// education = event.detail;
	// 	// course = event.detail;
	// 	// language = event.detail;
	// 	// interest = event.detail;
	// 	// project = event.detail;
	// 	// publication = event.detail;
	// 	// award = event.detail;
	// 	// certificate = event.detail;
	// 	// reference = event.detail;
	// }

	function handleSubmit() {
		if (!$account) {
			return
		}
		if (!personalInfo) {
			return;
		}
		const resumeObject:Resume = {
			member: memberID? memberID: undefined,
			title: title,
			personal: personalInfo,
			professional_exps: profExp? [profExp] : undefined,
			links: link? [link]: undefined,
			skills: skill? [skill]: undefined,
			educations: education? [education]: undefined,
			courses: course? [course]: undefined,
			languages: language? [language]: undefined,
			interests: interest? [interest]: undefined,
			projects: project? [project]: undefined,
			publications: publication? [publication]: undefined,
			awards: award? [award]: undefined,
			certificates: certificate? [certificate]: undefined,
			references: reference? [reference]: undefined,
		}
		addResume($account.id, resumeObject);
	}
</script>

<div>
	<h1>Resumes</h1>
	
	<InputText label="Resume Name" bind:value={title}/>	
	<PersonalInformation on:update={(event) => personalInfo = event.detail}/>
	<Links on:update={(event) => link = event.detail}/>
	<Skills on:update={(event) => skill = event.detail}/>
	<ProfessionalExperience on:update={(event) => profExp = event.detail}/>
	<EducationExperience on:update={(event) => education = event.detail}/>
	<Courses on:update={(event) => course = event.detail}/>
	<Languages on:update={(event) => language = event.detail}/> 
	<Interests on:update={(event) => interest = event.detail}/>
	<Projects on:update={(event) => project = event.detail}/>
	<Publications on:update={(event) => publication = event.detail}/>
	<Awards on:update={(event) => award = event.detail}/>
	<Certificates on:update={(event) => certificate = event.detail}/>
	<References on:update={(event) => reference = event.detail}/>

	<button on:click={handleSubmit}>Submit</button>
</div>
<Education></Education>
<Project></Project>
<Language></Language>
<Course></Course>
<Award></Award>
<ProfessionalExp></ProfessionalExp>
<Certificate></Certificate>
<Reference></Reference>
