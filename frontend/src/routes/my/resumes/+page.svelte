<script>
	import Education from "$lib/components/resume/Education.svelte";
	import Interest from "$lib/components/Interest.svelte";
	import Links from "$lib/components/Links.svelte";
	import PersonalInfo from "$lib/components/PersonalInfo.svelte";
	import Publication from "$lib/components/Publication.svelte";
	import Skill from "$lib/components/Skill.svelte";
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