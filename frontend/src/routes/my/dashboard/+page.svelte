<script lang="ts">
	import { goto } from "$app/navigation";
	import { PUBLIC_SERVER } from "$env/static/public";
	import type Resume from "$lib/interfaces/resume/Resume";
	import { fetchData } from "$lib/utils";
	import { error } from "@sveltejs/kit";
	import { onMount } from "svelte";
	import { writable } from "svelte/store";
	import { account } from "$lib/store";

	export const id = writable<number | null>(null);

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
		<div><h1>Dashboard</h1></div>
		<div>
			<div>
				<h2>User Info</h2>
				<p>{$account.email}</p>
			</div>
			<div>
				<h2>Resumes</h2>
				<ul>
					{#each resumes as resume}
						<li>- {resume.title}</li>
					{/each}
				</ul>
			</div>
			<div>
				<h2>Community</h2>
				<p>Text</p>
			</div>
		</div>
	{/if}
</section>
