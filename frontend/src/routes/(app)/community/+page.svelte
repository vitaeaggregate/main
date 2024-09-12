<script lang="ts">
  import { goto } from "$app/navigation";
  import { account } from "$lib/store";
  import { getAllResumes } from "$lib/api/resume";
  import type { Resume } from "$lib/interfaces/resume/Resume";
  import Search from "svelte-search";
  import Button from "$lib/components/Button.svelte";

  let resumes: Resume[] = [];
  let searchTerm = "";
  let slicedResumes: Resume[] = [];

  $: filteredResumes = resumes.filter((resume) =>
    resume.title.toLowerCase().includes(searchTerm.toLowerCase())
  );

  $: if (filteredResumes) slicedResumes = filteredResumes.slice(0, 5);

  const loadPage = async () => (resumes = await getAllResumes());

  $: if ($account) loadPage();
</script>

<section class="flex flex-col items-center gap-3">
  <Button on:click={() => goto("/my/resumes/new")}>Create Resume</Button>
  <h1>Community Resumes</h1>
  <Search bind:value={searchTerm} label="Search:" class="text-m m-2, border-1, border-solid p-2" />
  {#if searchTerm}
    <h2>Search Results</h2>
  {:else}
    <h2>Recommended Resumes</h2>
  {/if}
  <div class="text-center">
    {#each slicedResumes as resume}
      <div>
        <a href="/community/{resume.id}">{resume?.title}</a>
      </div>
    {/each}
  </div>
</section>
