<script lang="ts">
  import { goto } from "$app/navigation";
  import { writable } from "svelte/store";
  import { checkAccountAndRedirect } from "$lib/store";
  import { getAllResumes } from "$lib/api/resume";
  import type { Resume } from "$lib/interfaces/resume/Resume";
  import Search from "svelte-search";
  import Button from "$lib/components/Button.svelte";

  export const id = writable<number | null>(null);
  export const resumeId = writable<number | null>(null);
  let token: string | null = null;
  let resumeDisplay: Resume[] = [];
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
    resumeDisplay = [...resumes];
  };

  function handleCreateResumeClick() {
    goto("/my/resumes/new");
  }

  checkAccountAndRedirect(loadPage);
</script>

<section class="m-auto flex h-screen flex-col items-center">
  <Button on:click={handleCreateResumeClick}>Create Resume</Button>
  <h1>Community Resumes</h1>
  <Search bind:value={searchTerm} label="Search:" class="text-m m-2, border-1, border-solid p-2" />
  {#if searchTerm}
    <h2>Search Results</h2>
  {:else}
    <h2>Recommended Resumes</h2>
  {/if}
  <div class="text-center">
    {#each slicedResumes as resume}
      <ul>
        <li>
          <a href="/community/{resume.id}">{resume?.title}</a>
        </li>
      </ul>
    {/each}
  </div>
</section>
