<script lang="ts">
	import { goto } from "$app/navigation";
	import type Resume from "$lib/interfaces/resume/Resume";
	import { onMount } from "svelte";
	import { writable } from "svelte/store";
	import { account } from "$lib/store";
	import { getResumesByMemberId } from "$lib/api/resume";
	import { getCommentsByMemberId } from "$lib/api/comment";
	import type Comment from "$lib/interfaces/resume/Comment";
	import { currentResume } from '$lib/store';

	export const id = writable<number | null>(null);
	export const resumeId = writable<number | null>(null)

	let resumes: Resume[] | null = null;
	let comments: Comment[] | null = null;

	onMount(async () => {
		if (!$account) return goto("/login/test");

		resumes = await getResumesByMemberId($account.id);
		comments = await getCommentsByMemberId($account.id);
	});

	const handleResumeClick = (resumeId: number | null) => {
  currentResume.update((current) => ({
    ...current,
    id: resumeId
  }));
};

  $: console.log($currentResume);
</script>

<section class="">
	{#if $account}
		<div class="mb-5"><h1 class=" bg-slate-200">Dashboard</h1></div>
		<div class="grid grid-cols-3 gap-8">
			<div>
				<h2>User Info</h2>
				<ul class="flex flex-col gap-5 p-5">
					<li class="rounded-lg border-2 p-2">
						<p><strong>Email: </strong>{$account.email}</p>
					</li>
				</ul>
				<p>{$account.email}</p>
			</div>
			<div>
				<h2>Resumes</h2>
				{#if resumes}
					<ul class="flex flex-col gap-5 p-5">
						{#each resumes as resume}
							<li class="rounded-lg border-2 p-2">
								<p><strong>Resume id:</strong> {resume.id}</p>
								<a href="/community" on:click={() => handleResumeClick(resume.id)}><strong>Title:</strong> {resume.title}</a>
							</li>
						{/each}
					</ul>
				{:else}
					<p>No Resumes</p>
				{/if}
			</div>
			<div>
				<h2>Community</h2>
				<h3>Comments</h3>
				{#if comments}
					<ul class="flex flex-col gap-5 p-5">
						{#each comments as comment}
							<li class="rounded-lg border-2 p-2">
								<p><strong>Resume id:</strong> {comment.resume}</p>
								<p><strong>Comment:</strong> {comment.description}</p>
							</li>
						{/each}
					</ul>
				{:else}
					<p>No Comments</p>
				{/if}
			</div>
		</div>
	{/if}
</section>
