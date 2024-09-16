<script lang="ts">
  import { goto } from "$app/navigation";
  import { account } from "$lib/store";
  import { getAllResumes } from "$lib/api/resume";
  import type { Resume } from "$lib/interfaces/resume/Resume";
  import Search from "svelte-search";
  import Button from "$lib/components/Button.svelte";
  import ResumeIcon from "$lib/icons/ResumeIcon.svelte";
  import RandomIcon from "$lib/icons/RandomIcon.svelte";
  import TimeAgo from "javascript-time-ago";

  let resumes: Resume[] = [];
  let searchTerm = "";
  let slicedResumes: Resume[] = [];
  let isFilteredByCreationDate = false;
  let isFilteredByUpdateDate = false;
  let filteredResumes: Resume[] = [];

  const loadPage = async () => (resumes = await getAllResumes());

  function handleFilterByCreationDate() {
    if (!isFilteredByCreationDate) {
      filteredResumes = filteredResumes.sort((a, b) => {
        if (a.created_at && b.created_at) Date.parse(b.created_at) - Date.parse(a.created_at);
        if (!b.created_at) return 1;
        else return -1;
      });
      isFilteredByCreationDate = true;
      isFilteredByUpdateDate = false;
    }
  }

  function handleFilterByUpdateDate() {
    if (!isFilteredByUpdateDate) {
      filteredResumes = filteredResumes.sort((a, b) => {
        if (a.updated_at && b.updated_at) Date.parse(b.updated_at) - Date.parse(a.updated_at);
        if (!b.updated_at) return 1;
        else return -1;
      });
      isFilteredByUpdateDate = true;
      isFilteredByCreationDate = false;
    }
  }

  $: filteredResumes = resumes.filter((resume) => {
    if (resume.title) return resume.title.toLowerCase().includes(searchTerm.toLowerCase());
  });

  $: if (filteredResumes.length > 0) {
    const randomResumes: number[] = [];
    while (randomResumes.length < 5 && randomResumes.length < filteredResumes.length) {
      const randomIndex = Math.floor(Math.random() * filteredResumes.length);
      if (!randomResumes.includes(randomIndex)) {
        randomResumes.push(randomIndex);
      }
    }
    slicedResumes = randomResumes.map((index) => filteredResumes[index]);
  } else {
    slicedResumes = [];
  }

  $: if ($account) loadPage();
</script>

<section class="flex flex-col gap-3 text-center">
  <h1>Community Resumes</h1>
  <div class="flex justify-center gap-10">
    <Button on:click={() => goto("/my/resumes/new")} style="labeled-icon">
      <ResumeIcon />
      Create Resume
    </Button>
    <Button
      on:click={() => goto(`/community/${resumes[Math.floor(Math.random() * resumes.length)].id}`)}
      style="labeled-icon"
    >
      <RandomIcon />
      Random
    </Button>
  </div>
  <div class="flex flex-col gap-2">
    <h3>Search</h3>
    <Search
      bind:value={searchTerm}
      hideLabel={true}
      label="Search:"
      class="text-m m-2, border-1, rounded-xl border-solid p-2"
    />
  </div>
  <div class="flex justify-center gap-3">
    <div class="mr-1 h-10 w-32 items-center rounded-xl bg-white p-2 text-center">
      <Button on:click={handleFilterByCreationDate}>Date Created</Button>
    </div>
    <div class="mr-1 h-10 w-32 items-center rounded-xl bg-white p-2 text-center">
      <Button on:click={handleFilterByUpdateDate}>Date Updated</Button>
    </div>
  </div>
  {#if searchTerm}
    <h2>Search Results</h2>
  {:else}
    <h2>Recommended Resumes</h2>
  {/if}
  <div>
    {#each slicedResumes as resume}
      <div class="mb-4 rounded-xl bg-white p-4">
        <a href="/community/{resume.id}">{resume?.title}</a><br /><br />
        <p>
          <strong>Created:</strong>
          {resume.created_at && new TimeAgo("en-US").format(new Date(resume.created_at))}
        </p>
        <p>
          <strong>Updated:</strong>
          {resume.updated_at && new TimeAgo("en-US").format(new Date(resume.updated_at))}
        </p>
      </div>
    {/each}
  </div>
</section>
