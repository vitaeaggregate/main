<script>
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
</script>

<div>

	<h1>Resumes</h1>
	<Education></Education>
		
		<Interest/>
		<Links/>
		<PersonalInfo/>
		<Publication/>
		<Skill/>

</div>
<Education></Education>
<Project></Project>
<Language></Language>
<Course></Course>
<Award></Award>
<ProfessionalExp></ProfessionalExp>
<Certificate></Certificate>
<Reference></Reference>
