<script lang="ts">
	import type Header from "$lib/interfaces/resume/Header";
	import { onMount } from "svelte";
	import { writable } from "svelte/store";

	export const id = writable<number | null>(null);

	let resumes: Header[] = [];

	onMount(async () => {
		const response = await fetch("http://localhost:8000/members/resumes");
		// The URL should include the member id stored in the local storage
		const dataResume: Header[] = await response.json();
		console.log(dataResume);

		resumes = [...dataResume];
	});
</script>

<div class="grid grid-rows-2">
	<div><h1>Dashboard</h1></div>
	<div class="grid grid-cols-3 gap-20">
		<div>
			<h2>User Info</h2>
			<p>Text</p>
		</div>
		<div>
			<h2>Resumes</h2>
			{#each resumes as resume}
				<p>{resume.title}</p>
			{/each}
		</div>
		<div>
			<h2>Community</h2>
			<p>Text</p>
		</div>
	</div>
</div>
