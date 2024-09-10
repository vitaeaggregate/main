<script lang="ts">
	import { goto } from "$app/navigation";
	import { writable } from "svelte/store";
	import { checkAccountAndRedirect } from "$lib/store";
	import { getAllResumes } from "$lib/api/resume";
	import type { Resume } from "$lib/interfaces/resume/Resume"
	import Search from "svelte-search";

	export const id = writable<number | null>(null);
	export const resumeId = writable<number | null>(null);
	let token: string | null = null;
	let resumeDisplay:Resume[] = []
	let searchTerm = "";

  	$: filteredResumes =
    searchTerm && resumeDisplay
      ? resumeDisplay.filter((resume) =>
          resume.title.toLowerCase().includes(searchTerm.toLowerCase())
        )
      : resumeDisplay;

	$: slicedResumes = filteredResumes?.slice(0, 5); 

	const loadPage = async () => {
		token = sessionStorage.getItem("token");

		const resumes = await getAllResumes();
		resumeDisplay = [...resumes]
	};

	function handleCreateResumeClick() {
		goto('/my/resumes/new');
	}

	checkAccountAndRedirect(loadPage);
</script>

<section class="flex flex-col items-center justify-center h-screen">
	<button on:click={handleCreateResumeClick}>Create Resume</button>
	<br />
	<br />
	<h1>Community Resumes</h1>
	<br />
	<Search bind:value={searchTerm} label="Search"/>
<br />
	{#if searchTerm}
	<h2>Search Results</h2>
	{:else}
	<h2>Recommended Resumes</h2>
	{/if}
	<div class="text-center">
	  {#each slicedResumes as resume}
		<ul>
		  <li>
			<a href='/community/{resume.id}'>{resume.title}</a>
		  </li>
		</ul>
	  {/each}
	</div>
  </section>

<style>
	:global([data-svelte-search] input) {
  width: 100%;
  font-size: 1rem;
  padding: 0.5rem;
  margin: 0.5rem 0;
  border: 1px solid #e0e0e0;
  border-radius: 0.25rem;
}
</style>