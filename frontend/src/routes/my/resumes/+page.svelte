<script lang='ts'>
	import Education from "$lib/components/resume/Education.svelte";
	import Interest from "$lib/components/Interest.svelte";
	import Links from "$lib/components/Links.svelte";
	import PersonalInfo from "$lib/components/PersonalInfo.svelte";
	import Publication from "$lib/components/Publication.svelte";
	import Skill from "$lib/components/Skill.svelte";
	import Award from "$lib/components/resume/Award.svelte";
	import Certificate from "$lib/components/resume/Certificate.svelte";
	import Course from "$lib/components/resume/Course.svelte";
	import Language from "$lib/components/resume/Language.svelte";
	import ProfessionalExp from "$lib/components/resume/ProfessionalExp.svelte";
	import Project from "$lib/components/resume/Project.svelte";
	import Reference from "$lib/components/resume/Reference.svelte";
	import { addResume } from "$lib/api/resume";

	let personalInfo = {}
	let profExp = {};
	let link = {};
	let skill = {};
	let education = {};
	let course = {};
	let language = {};
	let interest = {};
	let project = {};
	let publication = {};
	let award = {};
	let certificate = {};
	let reference = {}

	function handleUpdate(event:CustomEvent) {
		personalInfo = event.detail;
		profExp = event.detail;
		link = event.detail;
		skill = event.detail;
		education = event.detail;
		course = event.detail;
		language = event.detail;
		interest = event.detail;
		project = event.detail;
		publication = event.detail;
		award = event.detail;
		certificate = event.detail;
		reference = event.detail;
	}

	function handleSubmit() {
		const resumeObject = {
			personal_info: personalInfo,
			professional_exp: profExp,
			links: link,
			skills: skill,
			education: education,
			courses: course,
			languages: language,
			interests: interest,
			projects: project,
			publications: publication,
			awards: award,
			certificates: certificate,
			references: reference,
		}
		addResume(resumeObject);
	}
</script>

<div>
	<h1>Resumes</h1>		
	<PersonalInfo on:update={handleUpdate}/>
	<Links on:update={handleUpdate}/>
	<Skill on:update={handleUpdate}/>
	<ProfessionalExp on:update={handleUpdate}/>
	<Education on:update={handleUpdate}/>
	<Course on:update={handleUpdate}/>
	<Language on:update={handleUpdate}/> 
	<Interest on:update={handleUpdate}/>
	<Project on:update={handleUpdate}/>
	<Publication on:update={handleUpdate}/>
	<Award on:update={handleUpdate}/>
	<Certificate on:update={handleUpdate}/>
	<Reference on:update={handleUpdate}/>

	<button on:click={handleSubmit}>Submit</button>
</div>
