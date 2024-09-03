<script lang="ts">
	import { goto } from "$app/navigation";
	import type Resume from "$lib/interfaces/resume/Resume";
	import { onMount } from "svelte";
	import { writable } from "svelte/store";
	import { account } from "$lib/store";
	import { getResumesByMemberId } from "$lib/api/resume";
	import { getCommentsByMemberId } from "$lib/api/comment";
	import type Comment from "$lib/interfaces/resume/Comment";

	export const id = writable<number | null>(null);

	let resumes: Resume[] | null = null;
	let comments: Comment[] | null = null;

	onMount(async () => {
		if (!$account) return goto("/login/test");

		resumes = await getResumesByMemberId($account.id);
		comments = await getCommentsByMemberId($account.id);
	});
</script>

<section class="">
	{#if $account}
		<div><h1>Dashboard</h1></div>
		<div>
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
								<p><strong>Title:</strong> {resume.title}</p>
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
