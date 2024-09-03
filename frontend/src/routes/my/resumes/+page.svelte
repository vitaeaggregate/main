<!-- <script>
	import Education from "$lib/components/resume/Education.svelte";
	import Interest from "$lib/components/resume/Interest.svelte";
	import Links from "$lib/components/resume/Links.svelte";
	import PersonalInfo from "$lib/components/resume/PersonalInfo.svelte";
	import Publication from "$lib/components/resume/Publication.svelte";
	import Skill from "$lib/components/resume/Skill.svelte";
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
<Reference></Reference> -->


<script lang="ts">
	import { goto } from "$app/navigation";
	import { PUBLIC_SERVER } from "$env/static/public";
	import type Resume from "$lib/interfaces/resume/Resume";
	import { fetchData } from "$lib/utils";
	import { error } from "@sveltejs/kit";
	import { onMount } from "svelte";
	import { writable } from "svelte/store";
	import { account } from "$lib/store";

		let resumes: Resume[] = [];

		export const id = writable<number | null>(null);

onMount(async () => {

	const requestInit: RequestInit = {
		method: "GET"
	};

	const response = await fetchData(`${PUBLIC_SERVER}/members/${$account.id}/resumes`, requestInit);

	if (!response.ok) {
		return error(response.status, response.statusText);
	}

	resumes = await response.json();
	console.log(resumes)
});
</script>

<div class="flex">
	{#each resumes as resume}
    <h2>{resume.title}</h2>
    <ul>
      {#each resume.languages as language}
        <li>{language}</li> {/each}
    </ul>
  {/each}
</div>