<script lang="ts">
	import { goto } from "$app/navigation";
	import { PUBLIC_SERVER } from "$env/static/public";
	import type Resume from "$lib/interfaces/resume/Resume";
	import { fetchData } from "$lib/utils";
	import { error } from "@sveltejs/kit";
	import { onMount } from "svelte";
	import { writable } from "svelte/store";
	import { account } from "$lib/store";
	import { resume } from "$lib/store";

	export const id = writable<number | null>(null);
	export const resumeId = writable<number | null>(null)

	let resumes: Resume[] = [];

	onMount(async () => {
		if (!$account) return goto("/login/test");

		const requestInit: RequestInit = {
			method: "GET"
		};

		const response = await fetchData(`${PUBLIC_SERVER}/members/${$account.id}/resumes`, requestInit);

		if (!response.ok) {
			return error(response.status, response.statusText);
		}

		resumes = await response.json();
	});
</script>

<section class="">
	{#if $account}
		<div class="mb-5"><h1 class=" bg-slate-200">Dashboard</h1></div>
		<div class="grid grid-cols-3 gap-8">
			<div>
				<h2>User Info</h2>
				<p>Welcome back <span class="font-bold">{$account.email}</span>!</p>
			</div>
			<div>
				<h2>Resumes</h2>
				<ul>
					{#each resumes as resume}
					<!-- Should have a link to the resume -->
						<li>- <a href="members/{$account.id}/resumes/{resume.id}">{resume.title}</a></li>
					{/each}
				</ul>
				<br />
				<a href="/resumes" class="hover:italic">Create new one?</a>
			</div>
			<div>
				<h2>Community</h2>
				<p>You have not left any comments anywhere.</p>
			</div>
		</div>
	{/if}
</section>
