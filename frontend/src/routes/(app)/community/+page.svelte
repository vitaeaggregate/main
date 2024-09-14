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

  $: filteredResumes = resumes.filter((resume) =>
    resume.title.toLowerCase().includes(searchTerm.toLowerCase())
  );

  $: if (filteredResumes.length > 0) {
  const randomResumes = [];
  while (randomResumes.length < 5) {
    const randomIndex = Math.floor(Math.random() * filteredResumes.length);
    if (!randomResumes.includes(randomIndex)) {
      randomResumes.push(randomIndex);
    }
  }
  slicedResumes = randomResumes.map((index) => filteredResumes[index]);
} else {
  slicedResumes = [];
}

  const loadPage = async () => (resumes = await getAllResumes());

  $: if ($account) loadPage();

  let isFilteredByCreationDate = false;
  let isFilteredByUpdateDate = false;

function handleFilterByCreationDate() {
  if (!isFilteredByCreationDate) {
    filteredResumes = filteredResumes.sort((a, b) => b.created_at - a.created_at);
    isFilteredByCreationDate = true;
    isFilteredByUpdateDate = false;
  }
}

function handleFilterByUpdateDate() {
  if(!isFilteredByUpdateDate) {
    filteredResumes = filteredResumes.sort((a, b) => b.updated_at - a.updated_at);
    isFilteredByUpdateDate = true;
    isFilteredByCreationDate = false;
  }
}

</script>

<section class="flex flex-col gap-3">
  <div class="flex flex-row">
  <div class="bg-white mr-1 w-40 h-24 rounded-xl p-4 items-center">
    <ResumeIcon/><br />
    <Button on:click={() => goto("/my/resumes/new")} >Create Resume</Button>
  </div>
  <div class="bg-white mr-1 w-40 h-24 rounded-xl p-4 items-center">
    <RandomIcon/><br />
    <Button on:click={() => goto(`/community/${resumes[Math.floor(Math.random() * resumes.length)].id}`)} >Random</Button>
  </div>
</div>
  <h1>Community Resumes</h1>
  <Search bind:value={searchTerm} label="Search:" class="text-m m-2, border-1, border-solid p-2" />
  <div class="flex flex-row justify-center">
  <div class="bg-white mr-1 w-32 h-10 rounded-xl p-2 items-center"><Button on:click={handleFilterByCreationDate}>Date Created</Button></div>
  <div class="bg-white mr-1 w-32 h-10 rounded-xl p-2 items-center"><Button on:click={handleFilterByUpdateDate}>Date Updated</Button></div></div>
  {#if searchTerm}
    <h2>Search Results</h2>
  {:else}
    <h2>Recommended Resumes</h2>
  {/if}
  <div class="text-center">
    {#each slicedResumes as resume}
      <div class="bg-white rounded-xl p-4 mb-4">
        <a href="/community/{resume.id}">{resume?.title}</a><br /><br />
        <p><strong>Created:</strong> {resume.created_at && new TimeAgo("en-US").format(new Date(resume.created_at))}</p>
        <p><strong>Updated:</strong> {resume.updated_at && new TimeAgo("en-US").format(new Date(resume.updated_at))}</p>
      </div>
    {/each}
  </div>
</section>
