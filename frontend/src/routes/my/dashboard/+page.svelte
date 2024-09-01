<script lang="ts">
	import type Header from '$lib/interfaces/resume/Header';
    import { onMount } from 'svelte';
  
    let resumes: Header[] = [];

onMount(async () => {
  const response = await fetch(URL);
  // The URL should include the member id stored in the local storage
  const dataResume: Header[] = await response.json();

  resumes = dataResume;
    });
  </script>


<div class="grid grid-rows-2">
  <div><h1>Dashboard</h1></div>
  <div class="grid grid-cols-3 gap-20">
    <div><h2>User Info</h2>
      <p>Text</p>
    </div>
    <div><h2>Resumes</h2>
      {#each resumes as resume}
        <p>{resume.title}</p>
      {/each}
    </div>
    <div><h2>Community</h2>
      <p>Text</p>
    </div>
  </div>
</div>